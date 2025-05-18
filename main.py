import psutil
import platform
import socket
import time
import os

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

def get_system_info():
    print("Начинаем мониторинг системы...")
    print("Информация о системе:")
    print(f"ОС: {platform.system()} {platform.release()}")
    print(f"Имя хоста: {socket.gethostname()}")
    print(f"IP: {socket.gethostbyname(socket.gethostname())}")

def monitor():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        get_system_info()

        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        print(f"\n🧠 CPU: {cpu}%")
        print(f"💾 RAM: {bytes_to_gb(ram.used)}/{bytes_to_gb(ram.total)} GB ({ram.percent}%)")
        print(f"📂 Disk: {bytes_to_gb(disk.used)}/{bytes_to_gb(disk.total)} GB ({disk.percent}%)")

        time.sleep(1)

if __name__ == "__main__":
    monitor()
