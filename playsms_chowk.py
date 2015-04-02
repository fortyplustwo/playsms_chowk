from flask import Flask, request
from utils import send_to_playsms 
app = Flask(__name__)

import logging
from logging import DEBUG, handlers

rfh = handlers.RotatingFileHandler('./chowk.log')
rfh.setLevel(DEBUG)

#Now, add handlers to all loggers
loggers = [app.logger, logging.getLogger('utils')]

for l in loggers:
    l.addHandler(rfh)

@app.route('/receivesms/')
def receivesms():
    '''get the sms, put in a URL proper for playSMS and forward it'''
    
    try:
        msg = {}
        msg['from'] = request.args['from']
        msg['text'] = request.args['text']
        msg['smsc'] = request.args['backend']
        msg['args'] = request.args
        
        send_to_playsms(msg)

        return ('',200,[])
    except Exception as e:
        app.logger.debug("Exception occurred!")
        raise e

if __name__ == "__main__":
       app.run(debug = True, host = '0.0.0.0', port = 6000)
