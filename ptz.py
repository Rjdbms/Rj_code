from onvif import ONVIFCamera
from onvif import exceptions as onvif_exceptions
from requests.auth import HTTPDigestAuth
import ipaddress

# Define the PTZ movement options (adjust as needed)
PTZ_CONTINUOUS_MOVE = {
    "x": 1.0,  # Pan speed (range: -1.0 to 1.0, where 0.0 stops)
    "y": 0.0,  # Tilt speed (range: -1.0 to 1.0, where 0.0 stops)
    "z": 0.0,  # Zoom speed (range: -1.0 to 1.0, where 0.0 stops)
}


def scan_and_control_ptz(ip_range, port, username, password):
    # Convert the IP strings to IPv4 objects
    start_ip, end_ip = ip_range
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    # Iterate through the IP range
    for ip in range(int(start_ip), int(end_ip) + 1):
        current_ip = ipaddress.IPv4Address(ip)
        if current_ip.is_private:
            try:
                # Create an ONVIF camera object for the current IP
                mycam = ONVIFCamera(str(current_ip), port, username, password)

                # Get the PTZ service
                ptz = mycam.create_ptz_service()

                # Get PTZ configuration options
                request = ptz.create_type("GetConfigurationOptions")
                request.ConfigurationToken = ptz.GetConfigurations()[0].token
                ptz_configuration_options = ptz.GetConfigurationOptions(request)

                # Check if PTZ is supported
                if ptz_configuration_options.PTZConfiguration.PTZUsage == "Continuous":
                    # Perform continuous PTZ movement (e.g., pan right)
                    request = ptz.create_type("ContinuousMove")
                    request.ProfileToken = ptz.GetProfiles()[0].token
                    request.Velocity = PTZ_CONTINUOUS_MOVE
                    ptz.ContinuousMove(request)

                    # You can add more PTZ movements here if needed
                    # For example, to stop the movement:
                    # ptz.Stop({'ProfileToken': ptz.GetProfiles()[0].token})

                    print(f"PTZ movement performed at {current_ip}")

            except onvif_exceptions.ONVIFError as e:
                print(f"ONVIF error with {current_ip}: {e}")
            except Exception as ex:
                print(f"Error with {current_ip}: {ex}")


# Define the IP range you want to scan
start_ip = "192.168.1.160"  # Starting IP address
end_ip = "192.168.1.161"  # Ending IP address
port = 8554  # Typically 80 for HTTP and 443 for HTTPS
username = "admin"
password = "admin"

# Call the function to scan the IP range and control PTZ
scan_and_control_ptz((start_ip, end_ip), port, username, password)
