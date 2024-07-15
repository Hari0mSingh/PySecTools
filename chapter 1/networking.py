# Networking Basics
# Concepts: Understanding HTTP/HTTPS protocols, understanding URL structures, basic networking concepts like IP addresses and ports.



import socket

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f'The IP address of {hostname} is {ip_address}')
    except socket.gaierror:
        print(f'Error: Unable to resolve hostname {hostname}')

# Example usage
hostname = 'www.google.com'
get_ip_address(hostname)

# Trying with an invalid hostname
invalid_hostname = 'invalid.hostname.example'
get_ip_address(invalid_hostname)
