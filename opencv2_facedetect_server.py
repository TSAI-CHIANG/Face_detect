import socket
import cv2
import numpy as np


# Set up the socket server
host = 'localhost'  # or the IP address of the machine running Unity
port = 12345        # port number where the Unity app will listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print('Waiting for a connection...')
connection, client_address = server.accept()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    frame = cv2.resize(frame, (540, 320))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        radius = min(w, h) // 1.5
        cv2.circle(frame, center, int(radius) ,(192, 192, 192), 1) #radius
    
        data = f"{center[0]},{center[1]},{radius}\n"
        connection.sendall(data.encode('utf-8'))

    cv2.imshow('AIConversationTool', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
connection.close()



# import asyncio
# import websockets
# import cv2

# async def face_server(websocket, path):
#     cap = cv2.VideoCapture(0)
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     print("Server is running, waiting for a connection...")

#     try:
#         while True:
#             ret, frame = cap.read()
#             if ret:
#                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#                 for (x, y, w, h) in faces:
#                     await websocket.send(f"{x},{y},{w},{h}")

#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#     finally:
#         cap.release()
#         print("Releasing camera and closing server.")

# async def main():
#     start_server = websockets.serve(face_server, "localhost", 8765)
#     print("Starting the WebSocket server at ws://localhost:8765")
#     await start_server
#     await asyncio.Future()  # Run forever

# try:
#     asyncio.run(main())
# except KeyboardInterrupt:
#     print("Server shutdown manually.")






# import cv2
# import numpy as np 


# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)
# # faces = face_cascade.detectMultiScale(gray)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Cannot receive frame")
#         break
#     frame = cv2.resize(frame,(540,320))              # 縮小尺寸，避免尺寸過大導致效能不好
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
#     faces = face_cascade.detectMultiScale(gray)     # 偵測人臉

    
#     for (x, y, w, h) in faces:
#         # 設置圓心座標和半徑
#         center = (x + w // 2, y + h // 2)
#         radius = min(w, h) // 2

#         # cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 255, 100), 2)   # 標記人臉
#         cv2.circle(frame, center, int(radius) ,(192, 192, 192), 1) #radius

#     cv2.imshow('oxxostudio', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()









