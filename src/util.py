import errno
import re
import socket

from enum import Enum
from socket import error as socket_error


# regex
num_regex = re.compile(r"(\d+)")


# load the ip address from the running machine
# Reference: https://github.com/yahoo/TensorFlowOnSpark/blob/e2f5cc45f95812d163e75b6ddb9c4661261d3bb0/tensorflowonspark/util.py#L41
def get_ip_address():
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

    if text is "" or not num_regex.match(text):
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
