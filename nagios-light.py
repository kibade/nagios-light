import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Use GPIO pin 18 for the LED

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces
server_socket.listen(1)

while True:
    client_socket, addr = server_socket.accept()
    message = client_socket.recv(1024).decode()
    if message == 'ON':
        GPIO.output(18, GPIO.HIGH)  # Turn on the LED
    elif message == 'OFF':
        GPIO.output(18, GPIO.LOW)  # Turn off the LED
    client_socket.close()
