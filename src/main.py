import argparse
import utils.config as config
import utils.ionos as ionos
import utils.net as net
import sys


def _load_args():
    parser = argparse.ArgumentParser(description="Update Ionos DynDNS record.")    
    parser.add_argument("-c", "--config",
                        help="Configuration file.",
                        type=str,
                        required=True)  
    return parser.parse_args()


def main():
    args = _load_args()

    _config = config.load(args.config)

    # Retrieve public IPv4
    pub_ip = net.get_public_ip(_config['net']['server'])

    # Exit if no ip is provided
    if pub_ip is None:
        print("Error - Unable to retrieve public IPv4.")
        sys.exit(1)
    print(f"Detected public IPv4: '{pub_ip}'.")

    api_key = ionos.gen_key(_config['ionos']['publicPrefix'], _config['ionos']['secret'])

    # Get user DNS Zones
    zones = ionos.get_zones(_config['ionos']['apiUrl'], api_key)

    # Exit if no zones retrieved
    if zones is None:
        print("Error - Unable to retrieve zones from client key.")
        sys.exit(1)

    zone_exists = False
    # Check if configured zone is part of user zones
    for zone in zones:

        if "id" not in zone:
            print(f"Unable to retrieve zone ID for zone: '{zone['name']}'.")
            continue

        # If zone is the zone configured
        if zone['name'] == _config['domainName']:
            print(f"Retrieving records for zone: '{zone['name']}'.")

            record_type = "A"

            # Get base web records for zone
            records = ionos.get_zone_records(_config['ionos']['apiUrl'], api_key, zone['id'], _config['domainName'], record_type)
            if records is None:
                print(f"Error - Unable to retrieve records from zone '{zone['name']}'.")
                sys.exit(1)

            # Check web records value
            for record in records['records']:

                if "id" not in record:
                    print(f"Error - Unable to retrieve record ID for record: '{record['name']}' type {record_type}.")
                    continue
                
                # If DNS record does not match public IPv4
                if record["content"] != pub_ip:
                    print(f"Public IPv4 value missmatch for record {record['name']} type {record_type}:")
                    print(f"\tcurrent value: {record['content']}")
                    print(f"\texpected value: {pub_ip}")

                    new_record = [
                        {
                            "name": record['name'],
                            "type": record_type,
                            "content": pub_ip,
                            "ttl": 3600,
                            "prio": 0,
                            "disabled": "false"
                        }
                    ]

                    # Update record
                    ionos.update_zone_record(_config['ionos']['apiUrl'], api_key, zone['id'], new_record)

                # If DNS record matches public IPv4 value.
                else:
                    print(f"Public IPv4 value matched for record {record['name']} type {record_type}:")
                    print(f"\tcurrent value: {record['content']}")
                    print(f"\texpected value: {pub_ip}")


if __name__ == "__main__":
    main()
