# from onvif import ONVIFCamera
# from requests.auth import HTTPDigestAuth
# import ipaddress


# def scan_and_get_rtsp(ip_range, ports, username, password):
#     # Convert the IP strings to IPv4 objects
#     start_ip, end_ip = ip_range
#     start_ip = ipaddress.IPv4Address(start_ip)
#     end_ip = ipaddress.IPv4Address(end_ip)

#     # Iterate through the IP range and ports
#     for ip in range(int(start_ip), int(end_ip) + 1):
#         current_ip = ipaddress.IPv4Address(ip)
#         if current_ip.is_private:
#             for port in ports:
#                 try:
#                     # Create an ONVIF camera object for the current IP and port
#                     mycam = ONVIFCamera(str(current_ip), port, username, password)

#                     # Get the media service
#                     media = mycam.create_media_service()

#                     # Get the first media profile
#                     media_profile = media.GetProfiles()[0]

#                     # Create a request for the RTSP stream URI
#                     rtsp_request = media.create_type("GetStreamUri")
#                     rtsp_request.StreamSetup = {
#                         "Stream": "RTP-Unicast",
#                         "Transport": {"Protocol": "RTSP"},
#                     }
#                     rtsp_request.ProfileToken = media_profile.token

#                     # Get the RTSP stream URI
#                     rtsp_uri = media.GetStreamUri(rtsp_request)["Uri"]

#                     print(f"RTSP stream found at {current_ip}:{port}: {rtsp_uri}")
#                 except Exception as e:
#                     # print(f"Error with {current_ip}:{port}: {e}")
#                     continue


# # Define the IP range you want to scan
# start_ip = "192.168.1.151"  # Starting IP address
# end_ip = "192.168.1.254"  # Ending IP address
# ports = [80, 8080, 443, 8443]  # List of ports to check
# username = "admin"
# password = "12ka442ka1@#"

# # Call the function to scan the IP range and get RTSP streams on multiple ports
# scan_and_get_rtsp((start_ip, end_ip), ports, username, password)


import requests
import socket

# Prompt the user for server, username, password, and hostname input

username = "galasachin97@gmmail.com"
password = "sachingala"
hostname = "emai.ddns.net"

# Gets the current public IP of the host machine.
myip = requests.get("http://api.ipify.org").text

# Gets the existing DNS IP pointing to the hostname.
old_ip = socket.gethostbyname(hostname)
print("Old IP:", old_ip)


# No-IP API - dynamic DNS update.
# https://www.noip.com/integrate/request
def update_dns(config):
    auth = (config[0], config[1])  # Username and password for HTTP Basic Authentication
    params = {
        "hostname": config[2],
        "myip": config[3],
    }
    url = "https://dynupdate.no-ip.com/nic/update"
    r = requests.get(url, auth=auth, params=params)

    print("Response Status Code:", r.status_code)
    print("Response Content:", r.content)

    if r.status_code != requests.codes.ok:
        print("Update failed.")
    else:
        print("Update successful.")


# Update only when the IP is different.
if myip != old_ip:
    update_dns((username, password, hostname, myip))
