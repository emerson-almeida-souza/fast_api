from socket import socket, AF_INET, SOCK_DGRAM

def return_my_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

print(return_my_ip())