import socket
import threading

BROADCAST_IP = '255.255.255.255'
PORT = 5005
BUFFER_SIZE = 1024

# Create and configure UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('0.0.0.0', PORT))  # Explicitly listen on all interfaces

running = True  # Global flag to control threads

def receive_messages():
    while running:
        try:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(f"\n[{addr[0]}] {data.decode()}\n> ", end='', flush=True)
        except OSError as e:
            if running:  # Only print error if we didn't intentionally close
                print(f"\nReceive error: {e}")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            break

print("🔒 SecureLink Chat Started")
print("Type your message below. Type 'exit' to quit.\n")

# Start receiver thread
receiver_thread = threading.Thread(target=receive_messages)
receiver_thread.daemon = True
receiver_thread.start()

try:
    while running:
        try:
            msg = input("> ")
            if msg.lower().strip() == "exit":
                running = False
                break
            sock.sendto(msg.encode(), (BROADCAST_IP, PORT))
        except KeyboardInterrupt:
            running = False
            break
finally:
    running = False
    sock.close()
    print("\nSecureLink Chat closed.")