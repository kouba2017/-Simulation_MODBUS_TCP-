import socket
import json
import time

GATEWAY_IP = '192.168.1.100'
GATEWAY_PORT = 5000
BIV_IP = '192.168.1.100'
BIV_PORT = 5001
CLE_VALID = 'cle1234'

def envoyer_au_biv(trame):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((BIV_IP, BIV_PORT))
            s.sendall(json.dumps(trame).encode('utf-8'))
        print("[GATEWAY] Trame relayée au BIV.")
    except Exception as e:
        print(f"[GATEWAY] Erreur vers BIV : {e}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((GATEWAY_IP, GATEWAY_PORT))
    server.listen()

    print("[GATEWAY] En écoute sur le port 5000...")

    while True:
        conn, addr = server.accept()
        with conn:
            print(f"[GATEWAY] Connexion de {addr}")
            data = conn.recv(1024)
            start = time.time()
            try:
                trame = json.loads(data.decode('utf-8'))

                if trame.get("key") != CLE_VALID:
                    print("[GATEWAY] Clé invalide, trame rejetée.")
                    continue

                print(f"[GATEWAY] Trame reçue : {trame}")
                envoyer_au_biv(trame)

                delay = time.time() - start
                print(f"[GATEWAY] Temps de traitement : {delay:.3f}s")
                if delay > 1.0:
                    print("⚠️ Alerte : traitement lent")
            except Exception as e:
                print(f"[GATEWAY] Erreur : {e}")