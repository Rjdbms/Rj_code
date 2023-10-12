# from onvif import ONVIFCamera
# from time import sleep
# from zeep import Transport


# # Import HTTPDigestAuth from requests library
# # from requests.auth import HTTPDigestAuth
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

# ip = "192.168.1.160"
# port = 80  # Typically 80 for HTTP and 443 for HTTPS
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

# camera info
from onvif import ONVIFCamera


# Define camera credentials and RTSP URI retrieval function
def get_camera_info_and_rtsp(ip, port, username, password):
    try:
        # Create an ONVIF camera object
        mycam = ONVIFCamera(ip, port, username, password)

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

        # Get camera information
        device_info = mycam.devicemgmt.GetDeviceInformation()

        # Extract and print camera information
        manufacturer = device_info.Manufacturer
        model = device_info.Model
        firmware_version = device_info.FirmwareVersion
        serial_number = device_info.SerialNumber

        print(f"Camera Info:")
        print(f"Manufacturer: {manufacturer}")
        print(f"Model: {model}")
        print(f"Firmware Version: {firmware_version}")
        print(f"Serial Number: {serial_number}")

        print(f"RTSP URI: {rtsp_uri}")

    except Exception as e:
        print(f"Error: {e}")


# Define camera credentials
ip = "192.168.1.160"
port = 8554  # Typically 80 for HTTP and 443 for HTTPS
username = "admin"
password = "admin"

# Call the function to get camera information and RTSP URI
get_camera_info_and_rtsp(ip, port, username, password)

# from onvif import ONVIFCamera


# # Define camera credentials and information retrieval function
# def get_camera_info(ip, port, username, password):
#     try:
#         # Create an ONVIF camera object
#         mycam = ONVIFCamera(ip, port, username, password)

#         # Get device information
#         device_info = mycam.devicemgmt.GetDeviceInformation()

#         # Extract and print camera information
#         manufacturer = device_info.Manufacturer
#         model = device_info.Model
#         firmware_version = device_info.FirmwareVersion
#         serial_number = device_info.SerialNumber
#         last_update = getattr(device_info.HardwareInformation, "ReleaseDate", "N/A")
#         country_of_origin = getattr(
#             device_info.HardwareInformation, "Manufacturer", "N/A"
#         )

#         print(f"Camera Info:")
#         print(f"Manufacturer: {manufacturer}")
#         print(f"Model: {model}")
#         print(f"Firmware Version: {firmware_version}")
#         print(f"Serial Number: {serial_number}")
#         print(f"Last Update Date: {last_update}")
#         print(f"Country of Origin: {country_of_origin}")

#     except Exception as e:
#         print(f"Error: {e}")


# # Define camera credentials
# ip = "192.168.1.151"
# port = 80  # Typically 80 for HTTP and 443 for HTTPS
# username = "admin"
# password = "12ka442ka1@#"

# # Call the function to get camera information
# get_camera_info(ip, port, username, password)
