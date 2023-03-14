import datetime
import urllib.request
from OpenSSL.crypto import load_crl, FILETYPE_ASN1

def lambda_handler(event, context):
    # Download CRL file from URL
    url = "http://cdp.geotrust.com/GeoTrustRSACA2018.crl"
    crl_file = urllib.request.urlopen(url).read()
    
    # Load CRL file into OpenSSL
    crl = load_crl(FILETYPE_ASN1, crl_file)
    
    # Get valid-to time from CRL
    valid_to = crl.get_nextUpdate()
    
    # Check if valid-to time is in the future
    if valid_to > datetime.datetime.now():
        return {"message": "Certificate Revocation List is valid."}
    else:
        return {"message": "Certificate Revocation List is expired."}
