import requests
import re


def get_public_ip(server: str) -> str:
    """Fetches the public IP address from ifconfig.me and validates it as a public IPv4."""
    
    try:
        response = requests.get(server, timeout=5)
        response.raise_for_status()
        
        ip_address = response.text.strip()
        
        # Regular expression for a valid IPv4 address
        ipv4_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        
        if not re.match(ipv4_pattern, ip_address):
            print("Error - Retrieved invalid IPv4 address format.")
            return None
        
        # Check if it's a public IPv4 (not in private/reserved ranges)
        private_ip_ranges = [
            (10, 0, 0, 0, 10, 255, 255, 255),
            (172, 16, 0, 0, 172, 31, 255, 255),
            (192, 168, 0, 0, 192, 168, 255, 255),
            (127, 0, 0, 0, 127, 255, 255, 255),
            (169, 254, 0, 0, 169, 254, 255, 255)
        ]
        
        ip_parts = tuple(map(int, ip_address.split(".")))
        
        for start1, start2, start3, start4, end1, end2, end3, end4 in private_ip_ranges:
            if (start1 <= ip_parts[0] <= end1 and
                start2 <= ip_parts[1] <= end2 and
                start3 <= ip_parts[2] <= end3 and
                start4 <= ip_parts[3] <= end4):
                print("Error - Detected private IP, not a public IPv4")
                return None

        # Return valid public IPv4
        return ip_address
    
    except requests.RequestException as e:
        print(f"Error -  Unable to fetching IP: {str(e)}")
        return None
