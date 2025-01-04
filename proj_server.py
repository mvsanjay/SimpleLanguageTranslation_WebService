import socket
import json
from googletrans import Translator
import threading

# Function to handle each client connection
def handle_client(client_socket, addr):
    print(f"Connection from {addr} has been established.")

    try:
        # Receive data from the client
        data = client_socket.recv(1024)

        if data:
            # Load JSON data
            json_data = json.loads(data.decode('utf-8'))

            # Extract text and target language
            text = json_data.get('text')
            target_language = json_data.get('target_language')

            # Initialize translator
            translator = Translator()

            # Translate the text
            translated_text = translator.translate(text, dest=target_language).text

            # Prepare response data as JSON
            response_data = {'translated_text': translated_text}
            response = json.dumps(response_data).encode('utf-8')

            # Send translated text back to the client
            client_socket.sendall(response)

        else:
            # Handle empty data
            error_response = {'error': 'No data received'}.encode('utf-8')
            client_socket.sendall(error_response)

    except Exception as e:
        # Handle errors
        error_response = {'error': str(e)}.encode('utf-8')
        client_socket.sendall(error_response)

    finally:
        # Close the client socket
        client_socket.close()

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '192.168.1.14'  # Replace with your server's IP address
port = 8000
server_socket.bind((host, port))

# Start listening for connections
server_socket.listen(3)

print(f"Translation service is up and running on {host}:{port}...")

# Accept connections and handle clients in a loop
while True:
    # Accept incoming client connections
    client_socket, addr = server_socket.accept()

    # Start a new thread for each incoming connection
    threading.Thread(target=handle_client, args=(client_socket, addr)).start()