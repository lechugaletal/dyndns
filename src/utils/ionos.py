import requests
from typing import Dict, Any
import json


def gen_key(public_prefix: str, secret: str) -> str:
    """Build API Key format."""

    return f"{public_prefix}.{secret}" 


def get_zones(api_url: str, api_key: str) -> str:
    """Fetch DNS zones from IONOS API."""

    headers  = {
        "accept": "application/json",
        "X-API-Key": api_key
    }

    response = requests.get(api_url, headers=headers)
    content = response.json()

    if response.status_code == 200:
        return content
    else:
        print(f"Error retrieving domain zones: [{response.status_code}] {content}")
        return None


def get_zone_records(api_url: str, api_key: str, zone_id: str, suffix: str, record_type: str) -> Dict[str, Any]:
    """Fetch DNS records from IONOS API."""
    
    url = f"{api_url}/{zone_id}"
    params = {
        "suffix": suffix,
        "recordType": record_type
    }
    
    headers = {
        "accept": "application/json",
        "X-API-Key": api_key
    }
    
    response = requests.get(url, headers=headers, params=params)
    content = response.json()

    if response.status_code == 200:
        return content
    else:
        print(f"Error retrieving zone records: [{response.status_code}] {content}")
        return None


def update_zone_record(api_url: str, api_key: str, zone_id: str, records: list) -> str:
    """Update provided DNS records from IONOS API."""

    url = f"{api_url}/{zone_id}"

    headers = {
        "accept": "*/*",
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }
    
    response = requests.patch(url, headers=headers, data=json.dumps(records))
    
    if response.status_code in [200, 204]:  # 204 means no content, successful update
        return {"success": True, "status": response.status_code}
    else:
        return {"success": False, "status": response.status_code, "error": response.text}
