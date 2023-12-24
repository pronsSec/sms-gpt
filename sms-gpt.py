from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai
import time
import threading
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


app = Flask(__name__)

# Twilio credentials
account_sid = 'GET FROM TWILIO'
auth_token = 'GET FROM TWILIO'
twilio_number = 'GET FROM TWILIO'
twilio_client = Client(account_sid, auth_token)

# OpenAI API Key
openai.api_key = 'GET FROM OPENAI'

def get_chatgpt_response(user_message):
    try:
        completion = openai.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {
                    "role": "user",
                    "content": 'Respond in 300 characters or less: ' + user_message,
                },
            ],
        )
        return completion.choices[0].message.content
    except RequestException as e:
        logging.error(f"Network-related error when calling OpenAI: {e}")
        return "Error in generating response due to network issue."
    except Exception as e:
        logging.error(f"Unexpected error in get_chatgpt_response: {e}")
        return "An unexpected error occurred."




def send_sms_response(response, recipient_number, twilio_client):
    max_sms_length = 159
    messages = [response[i:i + max_sms_length] for i in range(0, len(response), max_sms_length)]

    for msg in messages:
        twilio_client.messages.create(
            body=msg,
            from_=twilio_number,
            to=recipient_number
        )
        time.sleep(3)


def process_request_in_background(message, recipient_number, twilio_client):
    thread = threading.Thread(target=handle_long_running_task, args=(message, recipient_number, twilio_client))
    thread.start()


def handle_long_running_task(message, recipient_number, twilio_client):
    response = get_chatgpt_response(message)
    send_sms_response(response, recipient_number, twilio_client)



@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.form.get('Body')
    sender_number = request.form.get('From')  # Get the sender's phone number

    # Acknowledge the SMS immediately
    resp = MessagingResponse()
    resp.message("Received your message, processing it now. We'll send you the response shortly.")

    # Process the request in the background
    process_request_in_background(incoming_msg, sender_number, twilio_client)

    return str(resp)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
