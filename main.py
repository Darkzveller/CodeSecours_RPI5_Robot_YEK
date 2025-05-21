# import LIDAR
# import CAN
from lib import LIDAR, CAN

# Initialisation des fonctions des variables
# LIDAR.setup_lidar()
# CAN.setup_can()
test = False
valeur =300
poids_fort,poids_faible = CAN.separation_en_octets(valeur)
# poids_faible = valeur & 0xFF        # Masque sur les 8 bits de droite

print(f"Poids fort : {poids_fort} (0x{poids_fort:02X})")
print(f"Poids faible : {poids_faible} (0x{poids_faible:02X})")
i = 0 
f=0

# while (True) : 
    # i=i+1
    # print("i",i)