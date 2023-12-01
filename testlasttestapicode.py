from django.shortcuts import render

# Create your views here.
# views.py
# Import the GetPassword and GetPanStatus classes from the correct modules within the app
from .service.get_password import GetPassword
from .service.get_pan_status import GetPanStatus
from .client.cvl_rest_inquiry_client import CVLRestInquiryClient
# Import the necessary modules
import zeep
from zeep import Client
from lxml import etree
import xml.etree.ElementTree as ET
from django.http import HttpResponse

################ SOAP FUNCTIONS to get/post data - called by MAIN FUNCTIONS

## fire SOAP query to get password for Order API endpoint
## used by create_transaction_bse() and cancel_transaction_bse()
def soap_get_password_order(client):
   
    method_url = "https://krapancheck.cvlindia.com/ICVLRestInquiry/GetPassword"
    svc_url = 'https://krapancheck.cvlindia.com/CVLRestInquiry.svc'
    client.service._binding_options['address'] = 'https://krapancheck.cvlindia.com/CVLRestInquiry.svc'
    header_value = soap_set_wsa_headers(method_url, svc_url)
    response = client.service.GetPassword(password='Cvlkra@1234',passKey='04051998',_soapheaders=[header_value])
    element_str = etree.tostring(response, pretty_print=True, encoding='utf-8').decode('utf-8')
    root = ET.fromstring(element_str)

    password = root.find('.//APP_GET_PASS').text
    print("I am PAssword ====>", password)
    if (password):
        pass_dict = {'password': password, 'passkey': '04051998'}
        return pass_dict
    else:
        raise Exception(
            "Not able to find the password"
        )

def soap_get_pan(client, pass_dict):

    method_url = "https://pancheck.www.kracvl.com/ICVLPanInquiry/SolicitPANDetailsFetchALLKRA"
    svc_url = 'https://krapancheck.cvlindia.com/CVLRestInquiry.svc'
    client.service._binding_options['address'] = 'https://krapancheck.cvlindia.com/CVLRestInquiry.svc'
    header_value = soap_set_wsa_headers(method_url, svc_url)
    response = client.service.GetPanStatus(
        panNo='ABCDF2345U',
        # AAACN6682J
        userName='WEBADMIN',
        posCode='5100147231',
        password=pass_dict['password'],
        passKey=pass_dict['passkey'],
        _soapheaders=[header_value])
    # import pdb; pdb.set_trace()
    element_str = etree.tostring(response,pretty_print=True, encoding='utf-8').decode('utf-8')
    root = ET.fromstring(element_str)
    # import pdb ; pdb.set_trace()
    print("I am root =====>", root)
    status = root.find('.//APP_STATUS').text
    return element_str
    if (status == '200'):
        pan_details = {'pan_no': root.find('.//APP_PAN_NO').text}
        return element_str
    else:
        raise Exception(
            "Not able to find the password"
        )

# every soap query to bse must have wsa headers set 
def soap_set_wsa_headers(method_url, svc_url):
    header = zeep.xsd.Element('Header', zeep.xsd.ComplexType([
        zeep.xsd.Element('{http://www.w3.org/2005/08/addressing}Action', zeep.xsd.String()),
        zeep.xsd.Element('{http://www.w3.org/2005/08/addressing}To', zeep.xsd.String())
        ])
    )
    header_value = header(Action=method_url, To=svc_url)
    return header_value

def my_view(request):
    try:
        # Create a Zeep client for your SOAP service
        client = Client(wsdl='https://krapancheck.cvlindia.com/CVLRestInquiry.svc?wsdl')

        # get the password for posting order
        pass_dict = soap_get_password_order(client)

        pass_dict_pan = soap_get_pan(client, pass_dict)

        print("I am data =====>", pass_dict_pan)

        return HttpResponse(pass_dict_pan)

    except Exception as e:
        # Handle any exceptions that may occur during the API calls
        error_message = f"Error: {str(e)}"
        return HttpResponse(error_message, status=500)