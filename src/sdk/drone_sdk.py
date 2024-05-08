import cv2
import threading
import time
import sys
from queue import LifoQueue
from src.sdk.udp.udp import UDPSocket

LOCAL_IP = ''
DRONE_IP = "192.168.10.1"
COMMAND_PORT = 8889
STATE_PORT = 8890
VIDEO_PORT = 11111


class DroneSDK:
    def __init__(self) -> None:
        """Initialise the drone SDK."""
        print("SDK init!")
        self.state_server = UDPSocket(udp_ip=LOCAL_IP, udp_port=STATE_PORT, socket_type="server")
        # self.video_server = UDPSocket(udp_ip=LOCAL_IP, udp_port=VIDEO_PORT, socket_type="server")
        self.command_client = UDPSocket(udp_ip=DRONE_IP, udp_port=COMMAND_PORT, socket_type="client")
        self.send_command("command") # start SDK mode

        self.video_thread = threading.Thread(target=self._get_video, daemon=True)
        self.frame_stack = LifoQueue(maxsize=1)

        # TODO
        # self.return_code_thread = threading.Thread(target=self._get_return_code)
        # self.return_code_thread.start()

    def close(self) -> None:
        """Close the drone SDK."""
        print("Closing drone SDK!")
        if self.video_thread.is_alive():
            self.stop_video()

    def send_command(self, command) -> None:
        """Send a command to the drone."""
        print("Sending command: ", command)
        self.command_client.send_message(command)
        # TODO
        # return_code = self._get_return_code()

        # return return_code

    def get_state(self) -> None:
        """Get the drone state."""
        print("Getting drone state!")
        self.state = self.state_server.receive_message()
        print(self.state)

    def _get_video(self) -> None:
        self.video_source  = f"udp://@{LOCAL_IP}:{VIDEO_PORT}"
        self.video = cv2.VideoCapture(self.video_source)
        if not self.video.isOpened():
            print("Could not open video. Exiting...")
            sys.exit(1)

        while True:
            try:
                ret, frame = self.video.read() 
                if ret:
                    # cv2.imshow('frame', frame) # debugging and visualisation
                    self.frame = frame
                # cv2.waitKey(1) # debugging and visualisation

            except Exception:
                pass

    def _release_video(self) -> None:
        self.video.release()
        cv2.destroyAllWindows()

    def start_video(self) -> None:
        """Start the video stream."""
        print("Starting video stream!")
        self.send_command("streamon")
        
        if self.video_thread.is_alive() is False:
            self.video_thread.start()
        
        while not hasattr(self, "frame"):
            time.sleep(1)
            print("Waiting for video initialisation...")

    def stop_video(self):
        """Stop the video stream."""
        print("Stopping video stream!")
        self._release_video()
        self.send_command('streamoff')
        self.video_thread.join()

    def get_latest_frame(self) -> None:
        """Get the latest frame from the drone."""
        return self.frame
    
    def save_frame(self, frame_array) -> None:
        cv2.imwrite("frame.png", frame_array)
        