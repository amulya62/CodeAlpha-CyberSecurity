import socket

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("localhost", 9999))

# Send message
client.send("Hello Server!".encode())

# Receive reply
message = client.recv(1024).decode()
print("Server replied:", message)

# Close connection
client.close()