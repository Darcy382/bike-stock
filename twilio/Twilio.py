from twilio_secrets import TWILIO_SID, TWILIO_AUTH_TOKEN
from urllib import request, parse
import base64

TWILIO_CALL_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Calls.json"
TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"

RICK_ROLL_AUDIO = "http://demo.twilio.com/docs/voice.xml"
DEFAULT_MESSAGE = "Hello, this is a test message from Twilio"

class Twilio:

    default_from_num = "6282504270"
    
    @staticmethod
    def compile_and_send(url, params):
        data = parse.urlencode(params).encode()
        req = request.Request(url)
        authentication = "{}:{}".format(TWILIO_SID, TWILIO_AUTH_TOKEN)
        base64string = base64.b64encode(authentication.encode('utf-8'))
        req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))
        try: 
            with request.urlopen(req, data) as f:
                print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
        except Exception as e:
            print(e)

    @staticmethod
    def send_text(to_num, message=DEFAULT_MESSAGE, from_num=default_from_num):
        populated_url = TWILIO_SMS_URL.format(TWILIO_SID)
        post_params = {"To": "+1" + to_num,
                    "From": "+1" + from_num,
                    "Body": message
                    }
        Twilio.compile_and_send(populated_url, post_params)
        
    @staticmethod    
    def make_call(to_num, voice_url=RICK_ROLL_AUDIO, from_num=default_from_num):
        populated_url = TWILIO_CALL_URL.format(TWILIO_SID)
        post_params = {"To": "+1" + to_num,
                    "From": "+1" + from_num,
                    "Url": voice_url
                    }
        Twilio.compile_and_send(populated_url, post_params)