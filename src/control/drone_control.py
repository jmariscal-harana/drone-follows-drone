class DroneControl:
    def __init__(self) -> None:
        """Initialise the drone control algorithm."""
        print("Control init!")

    def close(self) -> None:
        """Close the drone control algorithm."""
        print("Closing drone control!")

    def control(self, state, inputs) -> None:
        """Send commands to the drone."""
        print("Controlling drone!")