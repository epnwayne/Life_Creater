import requests
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"
#ACCESS_TOKEN = "EAAOt02CRdcoBAPSl4Rt1ISAouRFR7kHEe1dJws0Mox38j8lxILtnH4lDh7g6rgMDTHq7BlrYNMHrCLea8tGZC1yuhc5ttsKcLY2pzINiIMOHGmHVZA8VeHskVERwade1nMw2L9GN10WZArMCMHTzkXHyLCjJDkSwR4th6h39wZDZD"
ACCESS_TOKEN = os.environ['FB_TOKEN']


#server to request
def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
