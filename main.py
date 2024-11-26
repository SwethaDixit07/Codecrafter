import socket

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 4221))
    server_socket.listen(1)
    
    # Wait for client
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

if __name__ == "__main__":
    main()
