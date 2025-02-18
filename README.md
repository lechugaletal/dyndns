# DynDNS

This project helps to automatically sync DNS `A` records: `www.domain.tld`, `domain.tld` with a dynamic public IPv4 value using Ionos API REST as DNS provider.

## How to run

The utility needs a config file with the following spec:
```yaml
ionos:
  apiUrl: "https://api.hosting.ionos.com/dns/v1/zones"
  publicPrefix: "1234" 
  secret: "aabbccdd-1234"
domainName: "domain.tld"
net:
  server: "https://ifconfig.me"

```

Ionos API Credentials can be created following the official [documentation](https://developer.hosting.ionos.com/docs/getstarted).

Can be run as follows:

```bash
python src/main.py -c ./test.yaml
Detected public IPv4: '1.2.3.4'.
Retrieving records for zone: 'domain.tld'.
Public IPv4 value matched for record domain.tld type A:
        current value: 1.2.3.4
        expected value: 1.2.3.4
Public IPv4 value matched for record www.domain.tld type A:
        current value: 1.2.3.4
        expected value: 1.2.3.4
```
