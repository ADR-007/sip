import asyncio

from aiohttp import ClientSession
import websockets
import json

ASTERISK_WEB_SOCKET_URL = 'ws://localhost:8088/ari/events?api_key=ariuser:1234&app=dialer&subscribeAll=true'
SERVER_WEB_HOOK_URL = 'http://localhost:8000/sip/webhook'


async def catch_and_send_events():
    async with websockets.connect(ASTERISK_WEB_SOCKET_URL) as web_socket, ClientSession() as session:
        while True:
            received = await web_socket.recv()
            print(received)
            as_json = json.loads(received)
            if as_json['type'] == 'PeerStatusChange':
                await session.post(SERVER_WEB_HOOK_URL, json={'username': as_json['endpoint']['resource'],
                                                              'state': as_json['endpoint']['state']})


asyncio.get_event_loop().run_until_complete(catch_and_send_events())
