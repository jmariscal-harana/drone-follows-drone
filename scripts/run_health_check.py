from src.interface import DroneInterface
from time import sleep
def main():
    drone_interface: DroneInterface = DroneInterface()

    # Check drone status
    drone_interface.sdk.get_state()
    print(drone_interface.sdk.state)
    sleep(3)

    # Start video stream
    drone_interface.sdk.start_video()
    sleep(3)
    print(drone_interface.sdk.frame)

    # Stop everything
    drone_interface.close()


main()