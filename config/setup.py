import subprocess

# Create a virtual enviroment and install required dependencies
def setup():
    command = subprocess.run(r"python -m venv ..\venv && ..\venv\Scripts\activate && pip install -r requirements.txt" , shell=True, text=True, capture_output=True)

    # Print results
    print(command.stdout, command.stderr)

if __name__ == "__main__":
    setup()
