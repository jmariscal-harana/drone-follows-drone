import sys
from time import sleep

from src.control.drone_control import DroneControl
from src.sdk.drone_sdk import DroneSDK
from src.tracker.drone_tracker import DroneTracker

class DroneInterface:
    def __init__(self) -> None:
        """Initialise the drone interface -> provides access to drone state and video stream."""
        print("Interface init!")

        self.video_rate = 5  # frames per second

        self.sdk = DroneSDK()
        self.tracker = DroneTracker(tracker_type="MIL")
        self.control = DroneControl(self.sdk)

    def close(self) -> None:
        """Close the drone interface."""
        print("Closing drone interface!")
        try:
            self.control.close()
            self.tracker.close()
            self.sdk.close()
            sys.exit(0)
        except Exception as e:
            print(e)
            sys.exit(1)

    def run(self) -> None:
        """Run the drone interface."""
        print("Running interface!")

        try:
            self.sdk.start_video()

            input("Press ENTER to initialise tracker:")
            frame = self.sdk.get_latest_frame()
            self.tracker.track(frame)
            
            control_i = 0
            while self.sdk.video_thread.is_alive():
                frame = self.sdk.get_latest_frame()
                bounding_box = self.tracker.track(frame)
                # if control_i % 10 == 0:  # send command every 10 frames
                #     self.control.control((frame, bounding_box))
                # control_i += 1
                sleep(1 / self.video_rate)

        except KeyboardInterrupt:
            self.close()


def main() -> None:
    drone_interface = DroneInterface()
    drone_interface.run()

if __name__ == "__main__":
    main()
