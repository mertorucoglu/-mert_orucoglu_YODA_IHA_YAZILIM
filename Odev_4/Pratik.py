import cv2 
import time

p = []
baslangic = None

cam = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier("haar_face.xml")

while cam.isOpened():
    ret, frame = cam.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(frame_gray, 1.3, 3)

    if len(faces_rect) > 0:
        if baslangic is None:
            baslangic = time.time()

        gecen_zaman = time.time() - baslangic

        cv2.putText(frame, f"{gecen_zaman:.1f} s", (490, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        for (x, y, w, h) in faces_rect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            a = (x+w)
            ort = (x+a) //2
            b = (y+h)
            ort2 = (b+y) //2

            cv2.putText(frame, f"({ort}, {ort2})", (30,30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            p.append((ort, ort2))
            if len(p) > 60:
                p.pop(0)

    else:
        baslangic = None
        p.clear()

    for i in range(1, len(p)):
        cv2.line(frame, p[i - 1], p[i], (255, 0, 0), 2)


    cv2.imshow("detect", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
print(frame.shape)
cv2.destroyAllWindows()
