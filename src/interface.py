import sys
from time import sleep

from src.control.drone_control import DroneControl
from src.sdk.drone_sdk import DroneSDK
from src.tracking.drone_tracking import DroneTracking

class DroneInterface:
    def __init__(self) -> None:
        """Initialise the drone interface -> provides access to drone state and video stream."""
        print("Interface init!")
        self.sdk = DroneSDK()
        self.tracking = DroneTracking()
        self.control = DroneControl()

    def close(self) -> None:
        """Close the drone interface."""
        print("Closing drone interface!")
        try:
            self.control.close()
            self.sdk.close()
            self.tracking.close()
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(1)

    def run(self) -> None:
        """Run the drone interface."""
        print("Running interface!")

        self.sdk.start_video()
        while True:
            try:
                self.sdk.get_state() # state may be older than latest image
                image = self.sdk.get_latest_image()
                bounding_box = self.tracking.track(image)
                command = self.control.control(self.sdk.state, (image, bounding_box))
                # self.sdk.send_command(command)
                print("Waiting for 5 seconds before next command... Press Ctrl+C to exit.\n")
                sleep(5)
            except KeyboardInterrupt:
                self.close()


def main() -> None:
    drone_interface = DroneInterface()
    drone_interface.run()

if __name__ == "__main__":
    main()


