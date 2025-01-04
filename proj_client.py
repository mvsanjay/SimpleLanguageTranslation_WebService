import json
import socket
import threading

def handle_connection(client_socket):
    """
    Handles the communication with the server.
    Receives the translated text from the server and prints it.
    """
    try:
        # Receive data from the server
        response = client_socket.recv(1024).decode("utf-8")

        if response:
            # Load JSON response
            response_data = json.loads(response)

            # Extract translated text
            translated_text = response_data.get("translated_text", "")

            # Print the translated text
            print("Translated Text:", translated_text)

        else:
            print("Error: No response received from the server.")

    except Exception as e:
        print("Error: Failed to receive response from the server:", str(e))

    finally:
        # Close the client socket
        client_socket.close()


# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host IP address and port
host = '192.168.1.14'  # Replace with the server's IP address
port = 8000

try:
    # Connect to the server
    client_socket.connect((host, port))

    # Input text to be translated
    text = input("Enter text to be translated: ")

    # Target language (default is English)
    target_language = input("Enter target language (default is 'en'): ") or 'en'

    # Prepare data as JSON
    data = {
        "text": text,
        "target_language": target_language
    }
    data = json.dumps(data).encode("utf-8")

    # Send data to the server
    client_socket.send(data)

    # Create a thread to handle the socket connection
    connection_thread = threading.Thread(target=handle_connection, args=(client_socket,))
    connection_thread.start()

    # Do other work while waiting for the response
    print("Waiting for response from server...")

    # Continue working while the thread is running
    connection_thread.join()

except Exception as e:
    print("Error: Could not connect to the server.", str(e))

finally:
    # Close client socket
    client_socket.close()