#  Simulation MODBUS TCP : PCC → Gateway → BIV 
**Avec trames JSON personnalisées, sécurité et supervision**


## Participants
- PCC (192.168.1.xx) : envoie une trame JSON toutes les 5s
- Gateway (192.168.1.xx) : écoute, vérifie la clé, supervise, relaie au BIV
- BIV (192.168.1.xx) : affiche les trames reçues

## Adress IP Config:
- Pour avoir le code fonctionnel remplace notre adresse IP par celles de votre PC ou localhost
*Si IP de PC: ``ipconfig `` command dans terminal
*Si localhost: 127.0.0.1


## Trame JSON envoyée
{
    "type": "horaire",
    "key": "cle1234",
    "data": "Tram A à 10h15"
}

## Sécurité
- Authentification par clé ("cle1234")
- Contrôle IP à implémenter si besoin

## Supervision (dans la passerelle)
- Temps de réponse mesuré
- Alerte si > 1 seconde

## Étapes d'exécution (dans cet ordre, chacun dans un terminal)

1. Lancer le serveur PCC :
   python pcc_sender.py

2. Lancer la passerelle :
   python gateway_server.py

2. Lancer le client BIV (recoie les horaires):
   python biv_receiver.py



Chaque script utilise ports 5000 (TCP) et 5001 (BIV). 

## Bibliothèque requise : 
   pymodbus 3.x ``pip install pymodbus``