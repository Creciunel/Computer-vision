import importlib.util
import os

# Verifică dacă OpenCV este deja instalat
try:
    importlib.util.find_spec('cv2')
    print("OpenCV is already installed.")
except ImportError:
    print("OpenCV is not installed. Installing...")

    # Instalează OpenCV folosind pip
    os.system("pip install opencv-python")

    # Verifică din nou dacă instalarea a avut succes
    try:
        importlib.util.find_spec('cv2')
        print("OpenCV has been successfully installed.")
    except ImportError:
        print("Error: Failed to install OpenCV.")

import cv2

# Inițializează camera
cap = cv2.VideoCapture(0)

# It's a good idea to check whether the camera is opened correctly
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Captură frame-uri de la camera
    ret, frame = cap.read()

    # Verifică dacă frame-ul a fost capturat corect
    if not ret:
        print("Error: Could not read frame.")
        break

    # Afișează frame-ul pe ecran
    cv2.imshow('Video', frame)

    # Așteaptă apăsarea tastei 'q' pentru a ieși din loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Eliberează resursele
cap.release()
cv2.destroyAllWindows()
