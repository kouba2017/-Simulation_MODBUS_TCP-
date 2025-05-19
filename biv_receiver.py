import socket
import json

BIV_IP = '192.168.1.100'
BIV_PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((BIV_IP, BIV_PORT))
    server.listen()

    print("[BIV] En attente de trames sur le port 5000...")

    while True:
        conn, addr = server.accept()
        with conn:
            print(f"[BIV] Connexion de {addr}")
            data = conn.recv(1024)
            try:
                trame = json.loads(data.decode('utf-8'))
                print(f"[BIV] Trame reçue : {trame}")
            except Exception as e:
                print(f"[BIV] Erreur de décodage : {e}")