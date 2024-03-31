from djitellopy import tello
import time

dron = tello.Tello()
dron.connect()
print(dron.get_battery())

dron.streamon()
dron.takeoff()

dron.send_rc_control(0, 15, 30, 0)

time.sleep(3)

dron.land()
