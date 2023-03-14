import datetime
import requests
import OpenSSL.crypto as crypto

crl_url = 'http://cdp.geotrust.com/GeoTrustRSACA2018.crl'
response = requests.get(crl_url)
crl_data = response.content

# Parse the CRL file
crl = crypto.load_crl(crypto.FILETYPE_ASN1, crl_data)

# Check the validity of the CRL
now = datetime.datetime.utcnow()
next_update = crl.get_nextUpdate().decode()
next_update_datetime = datetime.datetime.strptime(next_update, '%Y%m%d%H%M%SZ')
is_valid = now < next_update_datetime

if is_valid:
    print("Certificate revocation list is valid.")
else:
    print("Certificate revocation list is not valid.")