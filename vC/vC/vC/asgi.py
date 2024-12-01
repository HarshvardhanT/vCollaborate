import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import a_rooms.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vC.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            a_rooms.routing.websocket_urlpatterns
        )
    )
})