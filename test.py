import socket
from onvif import ONVIFCamera


# def discover_cameras():
#     camera_ports = [80, 8080]  # Common camera ports to check

#     for camera_port in camera_ports:
#         for i in range(1, 255):
#             ip = f"192.168.1.{i}"  # Change the network prefix as needed
#             try:
#                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                     s.settimeout(1)
#                     if s.connect_ex((ip, camera_port)) == 0:
#                         print(f"Camera found at {ip}:{camera_port}")

#             except (socket.timeout, ConnectionRefusedError):
#                 pass


# if __name__ == "__main__":
#     discover_cameras()


# import socket
# import requests


# def get_camera_info(ip, port):
#     url = f"http://{ip}:{port}/"  # Change the URL structure if needed
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Parse the response to extract camera information
#             # You may need to adjust this part based on the camera's web interface
#             camera_info = response.text
#             print(f"Camera found at {ip}:{port}")
#             print(f"Camera information: {camera_info}")
#     except requests.exceptions.RequestException:
#         pass


# import socket


# # Define a function to perform actions when a camera is discovered
# def get_camera_info(ip, port):
#     print(f"Camera discovered at {ip}:{port}")


# def discover_cameras():
#     camera_ports = [80, 8080]  # Common camera ports to check

#     for camera_port in camera_ports:
#         for i in range(1, 255):
#             ip = f"192.168.1.{i}"  # Change the network prefix as needed
#             try:
#                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                     s.settimeout(1)
#                     if s.connect_ex((ip, camera_port)) == 0:
#                         get_camera_info(ip, camera_port)  # Replace with desired actions
#                         # Stop searching once a camera is found
#             except (socket.timeout, ConnectionRefusedError):
#                 pass


# if __name__ == "__main__":
#     discover_cameras()

# # import socket
# # import requests
# # from bs4 import BeautifulSoup


# # def get_camera_info(ip, port):
# #     url = f"http://{ip}:{port}/"  # Change the URL structure if needed
# #     try:
# #         response = requests.get(url)
# #         if response.status_code == 200:
# #             soup = BeautifulSoup(response.text, "html.parser")

# #             # Print the entire HTML content for debugging
# #             print(soup.prettify())

# #             # Extract the camera company name (customize this part based on the camera's web interface)
# #             company_name_element = soup.find("span", {"class": "company-name"})
# #             if company_name_element:
# #                 company_name = company_name_element.text.strip()
# #             else:
# #                 company_name = "Company name not found"

# #             # Extract the RTSP link (customize this part based on the camera's web interface)
# #             rtsp_link_element = soup.find("a", {"class": "rtsp-link"})
# #             if rtsp_link_element:
# #                 rtsp_link = rtsp_link_element["href"].strip()
# #             else:
# #                 rtsp_link = "RTSP link not found"

# #             print(f"Camera found at {ip}:{port}")
# #             print(f"Company Name: {company_name}")
# #             print(f"RTSP Link: {rtsp_link}")
# #     except requests.exceptions.RequestException:
# #         pass


# # def discover_cameras():
# #     camera_ports = [80, 8080]  # Common camera ports to check

# #     for camera_port in camera_ports:
# #         for i in range(1, 255):
# #             ip = f"192.168.1.{i}"  # Change the network prefix as needed
# #             try:
# #                 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #                     s.settimeout(1)
# #                     if s.connect_ex((ip, camera_port)) == 0:
# #                         get_camera_info(ip, camera_port)  # Retrieve camera info
# #                         # return  # Stop searching once a camera is found
# #             except (socket.timeout, ConnectionRefusedError):
# #                 pass


# # if __name__ == "__main__":
# #     discover_cameras()

# # mycam = ONVIFCamera(ip, port, username,password)
# # media = mycam.create_media_service()
# # media_profile = media.GetProfiles()[0]
# # rstp = media.create_type('GetStreamUri')
# # rstp.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
# # rstp.ProfileToken = media_profile.token
# # rstp_uri = media.GetStreamUri(rstp)['Uri']
# # print(rstp_uri)

# # import ipaddress

# # # Define the IP range you want to scan
# # start_ip = "192.168.1.1"  # Starting IP address
# # end_ip = "192.168.1.254"  # Ending IP address

# # # Convert the IP strings to IPv4 objects
# # start_ip = ipaddress.IPv4Address(start_ip)
# # end_ip = ipaddress.IPv4Address(end_ip)

# # # Iterate through the IP range and print the reachable IP addresses
# # for ip in range(int(start_ip), int(end_ip) + 1):
# #     current_ip = ipaddress.IPv4Address(ip)
# #     response = current_ip.is_private
# #     if response:
# #         print(current_ip)

# from onvif import ONVIFCamera
# import ipaddress

# # Define the IP range you want to scan
# start_ip = "192.168.1.151"  # Starting IP address
# end_ip = "192.168.1.254"  # Ending IP address
# port = 80  # Typically 80 for HTTP and 443 for HTTPS
# username = "admin"
# password = "12ka442ka1@#"

# # Convert the IP strings to IPv4 objects
# start_ip = ipaddress.IPv4Address(start_ip)
# end_ip = ipaddress.IPv4Address(end_ip)

# # Iterate through the IP range
# for ip in range(int(start_ip), int(end_ip) + 1):
#     current_ip = ipaddress.IPv4Address(ip)
#     if current_ip.is_private:
#         try:
#             # Create an ONVIF camera object for the current IP
#             mycam = ONVIFCamera(str(current_ip), port, username, password)

#             # Get the media service
#             media = mycam.create_media_service()

#             # Get the first media profile
#             media_profile = media.GetProfiles()[0]
#             print(media_profile)
#             # Create a request for the RTSP stream URI
#             # rtsp_request = media.create_type("GetStreamUri")
#             # rtsp_request.StreamSetup = {
#             #     "Stream": "RTP-Unicast",
#             #     "Transport": {"Protocol": "RTSP"},
#             # }
#             # rtsp_request.ProfileToken = media_profile.token
#             rstp = media.create_type("GetStreamUri")
#             rstp.StreamSetup = {
#                 "Stream": "RTP-Unicast",
#                 "Transport": {"Protocol": "RTSP"},
#             }
#             rstp.ProfileToken = media_profile.token
#             rstp_uri = media.GetStreamUri(rstp)["Uri"]
#             print(rstp_uri)

#             # Get the RTSP stream URI
#             # rtsp_uri = media.GetStreamUri(rtsp_request)["Uri"]

#             # print(f"RTSP stream found at {current_ip}: {rtsp_uri}")
#         except:
#             # print(f"Error with {current_ip}")
#             continue

# # test

# from onvif import ONVIFCamera
# from requests.auth import HTTPDigestAuth
# import ipaddress


# def scan_and_get_rtsp(ip_range, port, username, password):
#     # Convert the IP strings to IPv4 objects
#     start_ip, end_ip = ip_range
#     start_ip = ipaddress.IPv4Address(start_ip)
#     end_ip = ipaddress.IPv4Address(end_ip)

#     # Iterate through the IP range
#     for ip in range(int(start_ip), int(end_ip) + 1):
#         current_ip = ipaddress.IPv4Address(ip)
#         if current_ip.is_private:
#             try:
#                 # Create an ONVIF camera object for the current IP
#                 mycam = ONVIFCamera(str(current_ip), port, username, password)

#                 # Get the media service
#                 media = mycam.create_media_service()

#                 # Get the first media profile
#                 media_profile = media.GetProfiles()[0]

#                 # Create a request for the RTSP stream URI
#                 rtsp_request = media.create_type("GetStreamUri")
#                 rtsp_request.StreamSetup = {
#                     "Stream": "RTP-Unicast",
#                     "Transport": {"Protocol": "RTSP"},
#                 }
#                 rtsp_request.ProfileToken = media_profile.token

#                 # Get the RTSP stream URI
#                 rtsp_uri = media.GetStreamUri(rtsp_request)["Uri"]

#                 print(f"RTSP stream found at {current_ip}: {rtsp_uri}")
#             except Exception as e:
#                 print(f"Error with {current_ip}: {e}")


# # Define the IP range you want to scan
# start_ip = "192.168.1.151"  # Starting IP address
# end_ip = "192.168.1.254"  # Ending IP address
# port = 80  # Typically 80 for HTTP and 443 for HTTPS
# username = "admin"
# password = "12ka442ka1@#"

# # Call the function to scan the IP range and get RTSP streams
# scan_and_get_rtsp((start_ip, end_ip), port, username, password)


# get rtsp

# ip = "192.168.1.151"
# port = [80, 8554, 443]  # Typically 80 for HTTP and 443 for HTTPS
# username = "admin"
# password = "admin"

# # Create an ONVIF camera object
# mycam = ONVIFCamera(ip, port, username, password)
# media = mycam.create_media_service()
# media_profile = media.GetProfiles()[0]
# rstp = media.create_type("GetStreamUri")
# rstp.StreamSetup = {"Stream": "RTP-Unicast", "Transport": {"Protocol": "RTSP"}}
# rstp.ProfileToken = media_profile.token
# rstp_uri = media.GetStreamUri(rstp)["Uri"]
# print(rstp_uri)

# from onvif import ONVIFCamera

# # Define camera information
# ip = "192.168.1.160"
# ports = [80, 8080, 443, 8]  # List of ports to check
# username = "admin"
# password = "admin"


# # Create a function to check the camera on a specific port
# def check_camera_on_port(ip, port, username, password):
#     try:
#         mycam = ONVIFCamera(ip, port, username, password)
#         media = mycam.create_media_service()
#         media_profile = media.GetProfiles()[0]
#         rstp = media.create_type("GetStreamUri")
#         rstp.StreamSetup = {"Stream": "RTP-Unicast", "Transport": {"Protocol": "RTSP"}}
#         rstp.ProfileToken = media_profile.token
#         rstp_uri = media.GetStreamUri(rstp)["Uri"]
#         print(f"Camera found on {ip}:{port}. Stream URI: {rstp_uri}")
#         return True
#     except Exception as e:
#         print(f"Camera not found on {ip}:{port}. Error: {str(e)}")
#         return False


# # Loop through the list of ports and check for the camera
# for port in ports:
#     if check_camera_on_port(ip, port, username, password):
#         break  # Exit the loop if the camera is found on any port


from onvif import ONVIFCamera
from requests.auth import HTTPDigestAuth
import ipaddress


def scan_and_get_rtsp(ip_range, ports, username, password):
    # Convert the IP strings to IPv4 objects
    start_ip, end_ip = ip_range
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    # Iterate through the IP range and ports
    for ip in range(int(start_ip), int(end_ip) + 1):
        current_ip = ipaddress.IPv4Address(ip)
        if current_ip.is_private:
            for port in ports:
                try:
                    # Create an ONVIF camera object for the current IP and port
                    mycam = ONVIFCamera(str(current_ip), port, username, password)

                    # Get the media service
                    media = mycam.create_media_service()

                    # Get the first media profile
                    media_profile = media.GetProfiles()[0]

                    # Create a request for the RTSP stream URI
                    rtsp_request = media.create_type("GetStreamUri")
                    rtsp_request.StreamSetup = {
                        "Stream": "RTP-Unicast",
                        "Transport": {"Protocol": "RTSP"},
                    }
                    rtsp_request.ProfileToken = media_profile.token

                    # Get the RTSP stream URI
                    rtsp_uri = media.GetStreamUri(rtsp_request)["Uri"]

                    print(f"RTSP stream found at {current_ip}:{port}: {rtsp_uri}")
                except Exception as e:
                    # print(f"Error with {current_ip}:{port}: {e}")
                    continue


# Define the IP range you want to scan
start_ip = "192.168.1.151"  # Starting IP address
end_ip = "192.168.1.254"  # Ending IP address
ports = [80, 8554]  # List of ports to check
username = "admin"
password = "12ka442ka1@#"

# Call the function to scan the IP range and get RTSP streams on multiple ports
scan_and_get_rtsp((start_ip, end_ip), ports, username, password)
