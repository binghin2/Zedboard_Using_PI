import cv2
import socket
import pickle
import struct

# 카메라 캡처
cap = cv2.VideoCapture(0)  

# ZedBoard와 연결될 IP 주소 및 포트
ZEDBOARD_IP = "192.168.1.100"  # ZedBoard IP 주소
PORT = 22

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ZEDBOARD_IP, PORT))
connection = client_socket.makefile('wb')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지를 바이너리 형태로 변환하여 전송
    data = pickle.dumps(frame)
    size = len(data)
    client_socket.sendall(struct.pack(">L", size) + data)

# 종료
cap.release()
client_socket.close()
