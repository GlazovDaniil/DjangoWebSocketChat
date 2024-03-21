from django.urls import re_path
from chat.consumers import ChatConsumer, DefaultConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
    re_path(r"ws/$", DefaultConsumer.as_asgi()),
]