import socket
import json
import config
import time


def send_msg(sock, msg):
    jmsg = json.dumps(msg)
    print msg
    sock.sendto(jmsg, (config.SERVER_IP, config.SERVER_PORT))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

send_msg(sock, config.MSG_BIND)


print "Hello"

while True:
    send_msg(sock, config.MSG_PING)
    time.sleep(config.PING_INTERVAL)
