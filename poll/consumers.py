from django.http import HttpResponse
from channels.handler import AsgiHandler

def poll_receive(message):

    # Check if the amount of clicks is humanly achievable and not negative

    # Check that the data is definitely a integer

    # Read the poll that sent the message

    # Read which option the votes are intended for

    # Add the new clicks to the database

    # Read the new clicks from the database

    # TODO: add some functionality instead of always sending 5 clicks

    clicks = 5
    message.reply_channel.send({
        'clicks': message.content[clicks],
    })

def poll_connect(message):
    # Allow anyone to connect to a poll
    message.reply_channel.send({'accept':True})
