# import ifcfg

# print(ifcfg.interfaces())

import os

# Run ifconfig command
# ifconfig_output = os.popen("ifconfig").read()
# print("ifconfig Output:")
# print(ifconfig_output)

# # Run iwconfig command
# iwconfig_output = os.popen("iwconfig").read()
# print("iwconfig Output:")
# print(iwconfig_output)
import subprocess
import re
import netifaces as ni

interface = "wlx503eaaa6beb7"
interface_2 = "enp2s0"


# Function to get the IP address of the default network interface
def get_ip_address():
    try:
        # interface = ni.gateways()["default"][ni.AF_INET][1]
        ip_address_1 = ni.ifaddresses(interface)[ni.AF_INET][0]["addr"]
        ip_address_2 = ni.ifaddresses(interface_2)[ni.AF_INET][0]["addr"]
        return ip_address_1, ip_address_2
    except:
        return "Not Found"


# Run iwconfig command
iwconfig_output = subprocess.check_output(["iwconfig", interface]).decode("utf-8")
ifconfig_output = subprocess.check_output(["ifconfig", interface_2]).decode("utf-8")


# Regular expressions to extract information
essid_pattern = re.compile(r'ESSID:"(.*?)"')
frequency_pattern = re.compile(r"Frequency:(\d+\.\d+ [^\s]+)")
quality_pattern = re.compile(r"Quality=(\d+/\d+)")
signal_pattern = re.compile(r"Signal level=(-\d+ dBm)")
bitrate_pattern = re.compile(r"Bit Rate=(\d+ [^\s]+)")

# Extract information using regex
essid_match = essid_pattern.search(iwconfig_output)
frequency_match = frequency_pattern.search(iwconfig_output)
quality_match = quality_pattern.search(iwconfig_output)
signal_match = signal_pattern.search(iwconfig_output)
bitrate_match = bitrate_pattern.search(iwconfig_output)

# Create a dictionary with the extracted information
wifi_info = {
    "ip": get_ip_address(),
    "Essid": essid_match.group(1) if essid_match else "Not Found",
    "Frequency": frequency_match.group(1) if frequency_match else "Not Found",
    "Quality": quality_match.group(1) if quality_match else "Not Found",
    "Signal": signal_match.group(1) if signal_match else "Not Found",
    "BitRate": bitrate_match.group(1) if bitrate_match else "Not Found",
}

# lan_info = {"ip": get_ip_address()}

# Print the dictionary as JSON
import json

print(json.dumps(wifi_info, indent=4))
# print(json.dumps(lan_info, indent=4))
