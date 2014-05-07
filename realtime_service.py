import json
import socket
import thread
import threading

UDP_BUFFER_SIZE = 1024
PING_INTERVAL = 15.0


class RealtimeService:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.bound_channels = {}

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 0))

        self.ping_loop()
        thread.start_new_thread(self.service_requests, ())

    def bind(self, channel):
        def bind_inner(fn):
            self.bound_channels[channel] = fn
            self.send_event({'e': 'bind', 'ch': channel})

            def bind_inner_inner(*args, **kwargs):
                return fn(*args, **kwargs)

            return bind_inner_inner
        return bind_inner

    def service_requests(self):
        while True:
            buf, addr = self.sock.recvfrom(UDP_BUFFER_SIZE)
            event = json.loads(buf)

            if event['e'] == 'ping':
                pass
            elif event['e'] == 'data':
                ch = event['ch']
                if ch in self.bound_channels and self.bound_channels[ch]:
                    self.bound_channels[ch](event['data'])

    def ping_loop(self):
        threading.Timer(PING_INTERVAL, self.ping_loop).start()

        # Only ping if we actually have bound channels
        if len(self.bound_channels):
            self.send_event({'e': 'ping'})

    def send_event(self, event):
        self.sock.sendto(json.dumps(event), (self.host, self.port))
