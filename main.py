from realtime_service import RealtimeService


rt = RealtimeService('rt.tntapp.co', 2748)


@rt.bind('door-1')
def ken_face(data):
    if data['locked'] is True:
        print "led [ OFF    ]"
    else:
        print "led [     ON ]"

while True:
    pass
