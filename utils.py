from requests import get
from settings import username, webservices_token, smsc, recvnum, output_format, app, url
import logging
#configure our logger
logger = logging.getLogger(__name__) #thus, utils.logger 

def make_text_playsms_compatible(t):
    '''Makes the msg text such that is compatible for processing inside playsms'''

    #TODO: Ensure that this happens only in case of msgs with keyword and nothing else
    #if the text doesnt' start with an @, add it.
    if not t[0] == '@':
        t = '@' + t

    return t

def send_to_playsms(msg = {}):
    '''sends a given message to the RapidPro server
    Parameters  Name or description
    Operation   inject
    Mandatory   u h from msg recvnum smsc
    Optional    format
    Returns     return codes
    '''

    try:
        
        data = { #the data to be sent in the body of the request
                'app'       : app,
                'from'      : msg['from'],
                'msg'       : msg['text'],
                'recvnum'   : recvnum,
                'smsc'      : msg['smsc'],
                'u'         : username,
                'h'         : webservices_token,
                'op'        : 'inject',
        }

        r = get(url=url, params = data)
        logger.debug("Sending request to RapidPro server at %s", r.url)
        logger.debug("Data inside request to RapidPro server is %s", data)
        logger.debug("The response we got from RapidPro is %s", r.text)

        r.raise_for_status() #Will raise an exception with the HTTP code ONLY IF the HTTP status was NOT 200
        return True
    except Exception as e:
        logger.debug("Exception %s occurred", e)
        raise e
