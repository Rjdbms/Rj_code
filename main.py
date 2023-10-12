from onvif import ONVIFCamera
from requests.auth import HTTPDigestAuth
import ipaddress
import threading


camera_data = {}


def fetch_rtsp(current_ip):
    try:
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

        print(f"RTSP stream found at {current_ip}: {rtsp_uri}")
        if rtsp_uri:
            camera_data[current_ip] = rtsp_uri
    except Exception as e:
        pass


def scan_and_get_rtsp(ip_range, port, username, password):
    # Convert the IP strings to IPv4 objects
    start_ip, end_ip = ip_range
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    # Iterate through the IP range
    for ip in range(int(start_ip), int(end_ip) + 1):
        current_ip = ipaddress.IPv4Address(ip)
        if current_ip.is_private:
            # Create an ONVIF camera object for the current IP

            # except Exception as e:
            #     print(f"Error with {current_ip}: {e}")
            x = threading.Thread(
                target=fetch_rtsp,
                args=(current_ip,),
                daemon=True,
            )
            x.start()
            x.join()


# Define the IP range you want to scan
start_ip = "192.168.1.151"  # Starting IP address
end_ip = "192.168.1.168"  # Ending IP address
port = 80  # Typically 80 for HTTP and 443 for HTTPS
username = "admin"
password = "12ka442ka1@#"
if __name__ == "__main__":
    # Call the function to scan the IP range and get RTSP streams
    scan_and_get_rtsp((start_ip, end_ip), port, username, password)
    print(camera_data)
