from djitellopy import tello

dron = tello.Tello()

dron.connect()
dron.streamon()
dron.takeoff()
