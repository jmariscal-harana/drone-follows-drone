import socket
import time
import sys

class UDPSocket:
    """A UDP socket"""
    def __init__(self, udp_ip="127.0.0.1", udp_port=5005, socket_type="server") -> None:
        """Create a UDP client or server socket."""
        if socket_type not in ["server", "client"]:
            print(f"Invalid socket type {socket_type}")
            sys.exit(1)

        print(f"Creating a UDP {socket_type} socket with IPv4 {udp_ip} and port {udp_port}...")
        self.udp_ip = udp_ip
        self.udp_port = udp_port
        self.socket_type = socket_type

        self.socket = socket.socket(socket.AF_INET, # IPv4
                                  socket.SOCK_DGRAM) # UDP
        if self.socket_type == "server":
            self.socket.bind((self.udp_ip, self.udp_port))
        elif self.socket_type == "client":
            self.socket.connect((self.udp_ip, self.udp_port))
        print(f"UDP {self.socket_type} socket created.\n")

    def close(self) -> None:
        """Closes the UDP socket"""
        print("Closing UDP socket...")
        self.socket.close()

    def send_message(self, message) -> None:
        """Sends a message to the UDP socket"""
        # print("Sent message: ", message)
        self.socket.send(bytes(message, 'utf-8'))

    def receive_message(self, buffer_size=1024) -> str:
        """Receives a message from the UDP socket"""
        data, _ = self.socket.recvfrom(buffer_size)
        # print("Received message: ", data.decode('utf-8'))

        return data.decode('utf-8')

def test_udp() -> None:
    """Test socket functionality"""
    udp_server = UDPSocket(udp_ip="127.0.0.1", udp_port=5005, socket_type="server")
    udp_client = UDPSocket(udp_ip="127.0.0.1", udp_port=5005, socket_type="client")

    seq = 0
    while True:
        try:
            seq += 1
            message = f"Hi\t[{seq}]"
            udp_client.send_message(message)
            udp_server.receive_message()
            time.sleep(1)
            print("Waiting for 1 second before sending next message... Press Ctrl+C to exit.")
        except KeyboardInterrupt:
            udp_client.close()
            udp_server.close()
            sys.exit()

def main() -> None: # pylint: disable=missing-docstring
    test_udp()

if __name__ == "__main__":
    main()