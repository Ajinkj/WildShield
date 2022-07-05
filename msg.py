from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

def snd(animal):
    wild= animal
    message = client.messages.create(
        body="Warning "+ wild +", detected.",
        from_=keys.twilio_number,
        to=keys.target_number
    )
    print(message.body)