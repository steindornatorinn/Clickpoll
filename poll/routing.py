from channels.routing import route
from django.http import HttpResponse
from poll.consumers import poll_receive, poll_connect
channel_routing = [
    route('websocket.receive', poll_receive),
    route('websocket.connect', poll_connect),
]
