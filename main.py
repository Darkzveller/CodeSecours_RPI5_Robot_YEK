import time
import keyboard
from lib.CAN import CAN
from lib.LIDAR import LIDAR

# Initialisation des fonctions des 
# LIDAR.stop_lidar()
LIDAR.setup_lidar()
# CAN.setup_can()
test = False
valeur =300
poids_fort,poids_faible = CAN.separation_en_octets(valeur)
poids_faible = valeur & 0xFF        # Masque sur les 8 bits de droite

print(f"Poids fort : {poids_fort} (0x{poids_fort:02X})")
print(f"Poids faible : {poids_faible} (0x{poids_faible:02X})")
i = 0 


try:
    while True:
        i += 1
        LIDAR.read_lidar()
        print("i = ", i)
        time.sleep(0.0025)

except KeyboardInterrupt:
    print("Arret demand� par l'utilisateur.")
    LIDAR.stop_lidar()