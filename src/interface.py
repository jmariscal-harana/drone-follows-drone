import sys
from time import sleep

from src.control.drone_control import DroneControl
from src.sdk.drone_sdk import DroneSDK
from src.tracker.drone_tracker import DroneTracker

class DroneInterface:
    def __init__(self) -> None:
        """Initialise the drone interface -> provides access to drone state and video stream."""
        print("Interface init!")
        self.sdk = DroneSDK()
        self.tracker = DroneTracker(tracker_type="BOOSTING")
        self.control = DroneControl()

    def close(self) -> None:
        """Close the drone interface."""
        print("Closing drone interface!")
        try:
            self.control.close()
            self.sdk.close()
            self.tracker.close()
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(1)

    def run(self) -> None:
        """Run the drone interface."""
        print("Running interface!")

        self.sdk.start_video()
        input("Press enter to initialise tracker:")
        frame = self.sdk.get_latest_frame()
        self.tracker.track(frame)

        while True:
            try:
                self.sdk.get_state() # state may be older than latest frame
                frame = self.sdk.get_latest_frame()
                bounding_box = self.tracker.track(frame)
                command = self.control.control(self.sdk.state, (frame, bounding_box))
                # self.sdk.send_command(command)
                print("Waiting for 5 seconds before next command... Press Ctrl+C to exit.\n")
                sleep(0.1)
            except KeyboardInterrupt:
                self.close()


def main() -> None:
    drone_interface = DroneInterface()
    drone_interface.run()

if __name__ == "__main__":
    main()


