import errno
import re
import socket
import datetime

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
