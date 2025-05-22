import ID_CAN as id
import can
bus =None
def setup_can():
    global bus
    print('Intialisation de CAN HAT')
    # Initialise le bus CAN avec l'interface 'socketcan' sur le canal 'can0' à 1 Mbps
    bus = can.interface.Bus(channel='can0', interface='socketcan', bitrate=1000000)


def send(id, data0, data1, data2, data3, data4, data5, data6, data7):
    global bus
    if bus is None:
        raise RuntimeError("Le bus CAN n'est pas initialisé, appelle d'abord setup_can()")

    # Crée une liste des 8 octets de données à envoyer
    data = [data0, data1, data2, data3, data4, data5, data6, data7]

    # Création d'un message CAN :
    # - arbitration_id : l'identifiant du message CAN
    # - data : la liste d'octets à envoyer
    # - is_extended_id : False signifie que l'ID est standard (11 bits)
    msg = can.Message(arbitration_id=id, data=data, is_extended_id=False)

    try:
        # Envoi du message CAN sur le bus avec bus.send()
        # Cette fonction bloque jusqu'à ce que le message soit transmis ou qu'une erreur survienne
        bus.send(msg)
        print(f"Message envoyé : ID={id}, data={data}")
    except can.CanError:
        # Cette exception est levée si l'envoi échoue (ex : bus occupé, matériel indisponible)
        print("Erreur lors de l'envoi du message CAN")

def read(timeout=0.0025):# 2.5 ms = 0.0025 s
    global bus
    if bus is None:
        raise RuntimeError("Le bus CAN n'est pas initialisé, appelle d'abord setup_can()")

    # Reception d'un message CAN avec un délai timeout (en secondes)
    # bus.recv() attend un message ou renvoie None si le délai est dépassé
    msg = bus.recv(timeout)

    if msg is None:
        # Aucun message reçu dans le délai imparti
        print("Aucun message reçu dans le délai imparti")
        return None
    else:
        # Affichage des informations du message reçu
        print(f"Message reçu : ID={msg.arbitration_id}, data={list(msg.data)}")
        # Retourne l'objet message reçu pour traitement ultérieur
        return msg

def separation_en_octets(valeur):
    """
    Prend une valeur entière 16 bits (0-65535)
    et renvoie un tuple (poids_fort, poids_faible).
    """
    poids_fort = (valeur >> 8) & 0xFF
    poids_faible = valeur & 0xFF
    return poids_fort, poids_faible

def fusion_octets(poids_fort, poids_faible):
    """
    Prend deux octets (entiers 0-255) : poids fort et poids faible
    et renvoie la valeur entière 16 bits recomposée.
    """
    valeur = (poids_fort << 8) | poids_faible
    return valeur
