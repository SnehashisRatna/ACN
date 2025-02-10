import socket

# Server configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5001       # Port to listen on

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive the image data
with open("received_image.jpg", "wb") as img_file:
    while True:
        data = conn.recv(1024)  # Receive data in chunks
        if not data:
            break
        img_file.write(data)

print("Image received successfully.")
conn.close()
server_socket.close()