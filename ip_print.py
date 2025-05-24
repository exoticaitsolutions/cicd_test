import time
import socket
import platform
import datetime

def get_system_info():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        hostname = 'Unknown'
        ip_address = 'Unknown'

    os_info = platform.system() + " " + platform.release()
    python_version = platform.python_version()

    return {
        'hostname': hostname,
        'ip_address': ip_address,
        'os': os_info,
        'python_version': python_version
    }

def main():
    info = get_system_info()
    print("=== System Info ===")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print("===================\n")

    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] IP: {info['ip_address']} Host: {info['hostname']}")
        time.sleep(1)

if __name__ == "__main__":
    main()
