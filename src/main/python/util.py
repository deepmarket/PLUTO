import errno
import re
import socket
import docker

from enum import Enum
from socket import error as socket_error


# regex
num_regex = re.compile(r"(\d+)")


# load the ip address from the running machine
# Reference: https://github.com/yahoo/TensorFlowOnSpark/blob/e2f5cc45f95812d163e75b6ddb9c4661261d3bb0/tensorflowonspark/util.py#L41
def get_local_ip_address():
    """Simple utility to get host IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except socket_error as sockerr:
        if sockerr.errno != errno.ENETUNREACH:
          raise sockerr
        ip_address = socket.gethostbyname(socket.getfqdn())
    finally:
        s.close()
    return ip_address


def config_input_check(text:str, available:int, res:Enum):

    if not text or not num_regex.match(text):
        return res.EMPTY_ERROR
    else:
        try:
            num = int(text)

            if num > available:
                return res.RANGE_ERROR
            else:
                return res.SUCCESS
        except ValueError:
            return res.INT_ERROR


def build_docker_container(detached=True, container_path='samgomena/deepshare_worker', version='latest', container_name='deepshare_worker'):
    """creates and runs a docker container from:
    https://hub.docker.com/u/samgomena/repository/docker/samgomena/deepshare_worker
    Returns the container ID if successful, False if not
    """
    docker_client = check_and_instantiate_docker_client()
    try:
        container = docker_client.containers.run(f'{container_path}:{version}', detach=detached, name=container_name)
    except docker.errors.ContainerError as e:
        print('error spinning up the container! Check docker install')
        print(e)
        return False
    except docker.errors.APIError as e:
        print('error talking to docker server API, try again later')
        return False
    except docker.errors.DockerException as e:
        print('something went wrong with docker')
        print(e)
        return False
    return container.id


def check_and_instantiate_docker_client():
    """Return a docker client or raise exception. Called at startup to make
    Sure that docker is configured correctly. Called on-demand for returning
    Docker client"""
    try:
        docker_client = docker.from_env()
    except docker.errors.DockerException as e:
        print(e)
        print('unsuccessful instantiation of docker client')
        raise e
    return docker_client


def destroy_docker_container(container_id):
    try:
        docker_client = docker.from_env()
        container = docker_client.containers.get(container_id)
        container.kill()
        docker_client.containers.prune()
    except docker.errors.DockerException as e:
        print(e)
        print(f'unsuccessful deletion of docker container {container_id}')
        raise e
