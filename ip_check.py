import ipaddress


def is_ip_address(hostname):
    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False


print(is_ip_address("185.23.45.91"))
print(is_ip_address("google.com"))
print(is_ip_address("192.168.1.1"))
print(is_ip_address("999.999.999.999"))