# Importation des bibliothèques pour le LiDAR
from rplidar import RPLidar
import time
lidar = None
scan_iterator = None


# Fonction de lecture des données du LiDAR
def read_lidar():
    global lidar
    global scan_iterator
    scan = next(scan_iterator)  # récupère un scan depuis l'itérateur existant, non bloquant ici
    for (_, angle, distance) in scan:
        # print(f'Angle: {angle:.2f}°, Distance: {distance:.2f} mm')
        if 0 < distance < 300:
            print(f'Stop! Object detected at {distance:.2f} mm, angle {angle:.2f}°')

# Fonction pour arrêter le LiDAR proprement
def stop_lidar():
    global lidar,scan_iterator  # on précise qu'on utilise la variable globale
    lidar.stop_motor()
    lidar.stop()
    time.sleep(1)
    lidar.disconnect()
    print('stop lidar')
    print('\n')

# Fonction d'initialisation du LiDAR
def setup_lidar():
    global lidar,scan_iterator  # on précise qu'on utilise la variable globale
    lidar = RPLidar('/dev/ttyUSB0', baudrate=256000)
    print(lidar.get_info())
    print('lidar',lidar)
    lidar.start_motor()
    scan_iterator = lidar.iter_scans()  # une seule fois ici
    time.sleep(2)
    print('Initialisation du lidar')
    print('\n')

