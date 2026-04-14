import socket

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Hello! The IP address for {hostname} is {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve hostname: {hostname}")

if __name__ == "__main__":
    resolve_hostname("example.com")