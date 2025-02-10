import socket

# Server details
SERVER_HOST = '127.0.0.1'  # Change this to the server's IP if running on different machines
SERVER_PORT = 5001         # Must match the server's port

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Open and send the image
image_path = "image.jpg"  # Change this to your image file
with open(image_path, "rb") as img_file:
    while chunk := img_file.read(1024):  # Read in chunks of 1024 bytes
        client_socket.sendall(chunk)

print("Image sent successfully.")
client_socket.close()