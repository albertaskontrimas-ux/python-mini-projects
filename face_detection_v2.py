import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    face_count = len(faces)

    # 🔴 jei yra veidas → reakcija
    if face_count > 0:
        color = (0, 0, 255)  # raudona
        message = "HELLO HUMAN"
    else:
        color = (0, 255, 0)  # žalia
        message = "NO FACE"

    # piešiam rėmelius
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    # tekstas
    cv2.putText(frame, message, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.putText(frame, f'Faces: {face_count}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('AI Camera', frame)

    if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
        break

cap.release()
cv2.destroyAllWindows()