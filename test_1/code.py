#!/usr/bin/env python
import asyncio
import datetime
import random
import json
import websocket
import numpy as np

IP = '192.168.10.224'
PORT = 5678


def format_time():
    t = datetime.datetime.now().time()
    s = t.strftime('%H:%M:%S.%f')
    return s[:-3]

async def time(websocket, path):
    while True:
        #now = datetime.datetime.utcnow().isoformat() + 'Z'
        data = {'datetime': str(format_time()),
                'ticker': 'ticker',
                'value': str(random.randint(100,1000)),
                'volume': str(random.randint(1,10))}
        await websocket.send(json.dumps(data))
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, IP, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()