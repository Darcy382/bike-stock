from constants import BIKE_KEY, CANYON_URL
from get_stock import get_html, find_stock
from twilio.Twilio import Twilio
from secrets import MY_PHONE_NUMBER
import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("bike-stock")

def get_old_stock():
    return table.get_item(Key={'bike-name': BIKE_KEY})['Item']['stock']
    
def lambda_handler(event, context):
    try:
        canyon_html = get_html(CANYON_URL)
        sizes_list = find_stock(canyon_html)
        old_stock = get_old_stock()
        if old_stock != ("\n").join(sizes_list):
            # Twilio.send_text(MY_PHONE_NUMBER, "ALERT: Canyon has updated their stock" + "\n".join(sizes_list))
            Twilio.make_call(MY_PHONE_NUMBER)
            table.put_item(Item={'bike-name': BIKE_KEY, 'stock': ("\n").join(sizes_list)})
        return {
            'statusCode': 200,
            'body': json.dumps(sizes_list)
        }
    except Exception as e:
        # Twilio.send_text("bike-stock-check failed with with: {}".format(e))
        Twilio.make_call(MY_PHONE_NUMBER)
        
