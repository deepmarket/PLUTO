# import socket
# from socket import AF_INET, SOCK_DGRAM
#
#
# def main():
#     client_socket = socket.socket(AF_INET, SOCK_DGRAM)
#     client_socket.settimeout(1)
#     server_host = 'google.com'
#     server_port = 443
#
#     while True:
#         client_socket.sendto(b"message", (server_host, server_port))
#         try:
#             reply, server_address_info = client_socket.recvfrom(1024)
#             print(reply)
#         except socket.timeout:
#             print("socket timeout")
#
#
# if __name__ == "__main__":
#     main()
#

from socket import socket, AF_INET, SOCK_STREAM

# result = conn.connect_ex(('131.252.209.102', 8080))
for port in range(80, 60000):
    conn = socket(AF_INET, SOCK_STREAM)
    result = conn.connect_ex(('localhost', port))
    if result == 0:
        print("Port is open")
        print(f"Port {port} is open")
    else:
        del conn, result
    # else:
    #     # print("Port is not open")
    #     print(f"Port {port} is not open")
