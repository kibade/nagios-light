import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.100.4', 12345))  # Replace with the Pi's IP
client_socket.sendall(b'OFF')  # Send command to turn on the LED
client_socket.close()
