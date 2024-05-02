import cv2
import os

putanja_za_cuvanje = 'C:/Users/Administrator/PycharmProjects/tello_dron_slike'
output_filename = putanja_za_cuvanje + 'output.mp4'

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

os.startfile(output_filename)
