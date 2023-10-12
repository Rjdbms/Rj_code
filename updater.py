# import requests, socket

# Server = input("Enter server name: ")
# username = input("Enter Username: ")
# password = input("Enter password: ")
# hostname = input("Enter hostname: ")  # your domain name hosted in no-ip.com

# # Gets the current public IP of the host machine.
# myip = requests.get("http://api.ipify.org").text

# # Gets the existing dns ip pointing to the hostname.
# old_ip = socket.gethostbyname(hostname)
# print(old_ip)


# # Noip API - dynamic DNS update.
# # https://www.noip.com/integrate/request.
# def update_dns(config):
#     r = requests.get(
#         "http://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(
#             *config
#         )
#     )

#     if r.status_code != requests.codes.ok:
#         print(r.content)

#     pass


# # Update only when ip is different.
# if myip != old_ip:
#     update_dns((username, password, hostname, myip))
# pass
# import requests
# import socket

# server = input("Enter server name: ")
# username = input("Enter Username: ")
# password = input("Enter password: ")
# hostname = input("Enter hostname: ")

# # Gets the current public IP of the host machine.
# myip = requests.get("http://api.ipify.org").text

# # Gets the existing DNS IP pointing to the hostname.
# old_ip = socket.gethostbyname(hostname)
# print("Old IP:", old_ip)


# # No-IP API - dynamic DNS update.
# # https://www.noip.com/integrate/request
# def update_dns(config):
#     auth = (config[0], config[1])  # Username and password for HTTP Basic Authentication
#     params = {
#         "hostname": config[2],
#         "myip": config[3],
#     }
#     url = "https://dynupdate.no-ip.com/nic/update"
#     r = requests.get(url, auth=auth, params=params)

#     if r.status_code != requests.codes.ok:
#         print("Update failed. Response:", r.content)
#     else:
#         print("Update successful. Response:", r.content)


# # Update only when the IP is different.
# if myip != old_ip:
#     update_dns((username, password, hostname, myip))
import requests, socket

username = "galasachin97@gmail.com"
password = "sachingala"
hostname = "emai.ddns.net"  # your domain name hosted in no-ip.com

# Gets the current public IP of the host machine.
myip = requests.get("http://api.ipify.org").text
print(myip)
# Gets the existing dns ip pointing to the hostname.
old_ip = socket.gethostbyname(hostname)
print(old_ip)


# Noip API - dynamic DNS update.
# https://www.noip.com/integrate/request.
def update_dns(config):
    r = requests.get(
        "http://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(
            *config
        )
    )

    if r.status_code != requests.codes.ok:
        print(r.content)
    pass


print(myip)
print(old_ip)
# Update only when ip is different.
if myip != old_ip:
    update_dns((username, password, hostname, myip))
pass
