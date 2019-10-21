import errno
import re
import socket
import docker
import datetime
from requests.exceptions import ConnectionError as RequestsConnectionError

from enum import Enum
from socket import error as socket_error


# regex
num_regex = re.compile(r"(\d+)")
email_verification_regex = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.IGNORECASE
)

def get_ip_address():
    """
    Simple utility to get host IP address.
    Reference: https://github.com/yahoo/TensorFlowOnSpark/blob/e2f5cc45f95812d163e75b6ddb9c4661261d3bb0/tensorflowonspark/util.py#L41
    """
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


def config_input_check(text: str, available: int, res: Enum):
    """
    Resource machine config input check
    :param text: required. config input text
    :param res; required. return message package
    """

    if not text:
        return res.EMPTY_ERROR

    if not num_regex.match(text):
        return res.INT_ERROR
    else:
        try:
            num = int(text)

            if num > available:
                return res.RANGE_ERROR
            else:
                return res.SUCCESS
        except ValueError:
            return res.INT_ERROR


def spin_up_docker_container(detached=True, container_path='samgomena/deepshare_worker', version='latest', memory=None, cpus=None):
    """creates and runs a docker container from:
    https://hub.docker.com/u/samgomena/repository/docker/samgomena/deepshare_worker
    Returns the container ID if successful, False if not
    """
    docker_clt = docker_client()
    memory += "g" # add unit
    nano_cpus = int(cpus) * (10**9)
    try:
        container = docker_clt.containers.run(f'{container_path}:{version}', detach=detached, nano_cpus=nano_cpus, mem_limit=memory)
    except docker.errors.ContainerError as e:
        print('error spinning up the container! Check docker install')
        print(e)
        return False
    except docker.errors.APIError as e:
        print('error talking to docker server API, try again later')
        return False
    except (docker.errors.DockerException, RequestsConnectionError) as e:
        print('something went wrong with docker')
        print(e)
        return False
    return container.short_id


def docker_client():
    """Return a docker client or raise exception. Called at startup to make
    Sure that docker is configured correctly. Called on-demand for returning
    Docker client"""
    try:
        docker_clt = docker.from_env()
        docker_clt.ping()
    except (docker.errors.DockerException, RequestsConnectionError) as e:
        print(e)
        print('unsuccessful instantiation of docker client')
        raise docker.errors.DockerException
    return docker_clt


def destroy_docker_container(container_id):
    try:
        docker_clt = docker.from_env()
        container = docker_clt.containers.get(container_id)
        container.kill()
        docker_clt.containers.prune()
    except (docker.errors.DockerException, RequestsConnectionError) as e:
        print(e)
        print(f'unsuccessful deletion of docker container {container_id}')
        raise docker.errors.DockerException


def job_input_check(text: int, res: Enum):
    """
    Job input check
    :param text: required. input text
    :param res: required. return message package
    """

    if not text:
        return res.EMPTY_ERROR

    if not num_regex.match(text):
        return res.INT_ERROR
    else:
        try:
            num = int(text)

            return res.SUCCESS
        except ValueError:
            return res.INT_ERROR


def email_verification_check(text: str, res: Enum):
    """
    Verify if input email is valid
    :param text: required. email input
    :param res: required. return message package
    """

    if not text:
        return res.INVALID_ERROR

    if not email_verification_regex.match(text):
        return res.INVALID_ERROR

    return res.SUCCESS


def add_greeting():
    """
    :return: a greeting base on real time of the day
    """
    now = datetime.datetime.now()

    if now.hour < 12:
        return "Good morning"
    elif 12 <= now.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"
