# Importation des bibliothèques pour le LiDAR
from rplidar import RPLidar
import time
lidar = None

# Fonction d'initialisation du LiDAR
def setup_lidar():
    global lidar  # on précise qu'on utilise la variable globale
    lidar = RPLidar("COM6", baudrate=256000)
    print(lidar.get_info())
    lidar.start_motor()
    time.sleep(1)
    print('Initialisation du lidar')


# Fonction de lecture des données du LiDAR
def read_lidar():
    global lidar  # on précise qu'on utilise la variable globale

    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            print(f'Angle: {angle:.2f}°, Distance: {distance:.2f} mm')
            if 0 < distance < 300:
                print(f'Stop! Object detected at {distance:.2f} mm, angle {angle:.2f}°')

# Fonction pour arrêter le LiDAR proprement
def stop_lidar_fonctionnement():
    global lidar  # on précise qu'on utilise la variable globale
    lidar.stop_motor()
    lidar.stop()
    time.sleep(1)
    lidar.disconnect()

