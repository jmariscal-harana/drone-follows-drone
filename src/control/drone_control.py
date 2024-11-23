from src.sdk.drone_sdk import DroneSDK
from time import sleep
class DroneControl:
    def __init__(self, sdk: DroneSDK) -> None:
        """Initialise the drone control algorithm."""
        print("Control init...")

        self.sdk = sdk

    def close(self) -> None:
        """Close the drone control algorithm."""
        print("Closing drone control!")

        self.sdk.send_command("land")

    def control(self, inputs) -> None:
        """Send commands to the drone."""
        print("Controlling drone!")

        # TODO: Implement drone control logic here
        command = "takeoff"
        
        self.sdk.send_command(command)