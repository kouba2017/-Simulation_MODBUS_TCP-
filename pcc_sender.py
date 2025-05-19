import socket
import json
import time

GATEWAY_IP = '192.168.1.100'
GATEWAY_PORT = 5000

while True:
    trame = {
        "type": "horaire",
        "key": "cle1234",
        "data": "Tram A à 10h15",
    }
    message = json.dumps(trame).encode('utf-8')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((GATEWAY_IP, GATEWAY_PORT))
            s.sendall(message)
            print("[PCC] Trame envoyée à la passerelle.")
        except Exception as e:
            print(f"[PCC] Erreur de connexion : {e}")

    time.sleep(5)