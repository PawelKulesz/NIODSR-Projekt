# Projekt ROS 2 - Sterowanie Robotem TurtleBot

Projekt NIODSR. Sterowanie robocikiem.

## Funkcjonalności
### Obsługa kodów Aruco
- Jazda do przodu poprzez pokazanie kodu Aruco w górnej części ekranu
- Jazda do tyłu poprzez pokazanie kodu Aruco w dolnej części ekranu
- Postój robota gdy kamera nie widzi żadnego kodu Aruco

## Wymagania
- ROS 2 Humble
- Pakiety symulacyjne: `ros-humble-turtlebot3-gazebo`
- Biblioteki Python: `opencv-python`, `cv_bridge`

## Instalacja
cd ~/ros2_ws/src <br />
git clone https://github.com/PawelKulesz/NIODSR-Projekt <br />

sudo apt update <br />
sudo apt install python3-opencv python3-numpy ros-humble-turtlebot3-gazebo <br />

cd ~/ros2_ws <br />
colcon build --packages-select camera_subscriber <br />

source install/setup.bash <br />

### Uruchomienie
#### Terminal 1:
- source /opt/ros/humble/setup.bash
- export TURTLEBOT3_MODEL=burger
- ros2 launch turtlebot3_gazebo empty_world.launch.py

#### Terminal 2:
- cd ~/ros2_ws
- source install/setup.bash
- ros2 launch camera_subscriber project.launch.py

