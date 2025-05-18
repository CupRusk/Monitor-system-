import psutil
import platform
import socket
import time
import os
from colorama import Fore, Style

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

def get_system_info():
    color3 = Fore.CYAN
    print(color3 + "Начинаем мониторинг системы...")
    print(color3 + "Информация о системе:")
    print(color3 + f"ОС: {platform.system()} {platform.release()}")
    print(color3 + f"Имя хоста: {socket.gethostname()}")
    print(f"IP: {socket.gethostbyname(socket.gethostname())}")
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    sent = bytes_to_gb(net2.bytes_sent - net1.bytes_sent)
    recv = bytes_to_gb(net2.bytes_recv - net1.bytes_recv)

    print(Fore.BLACK + f"Сеть: ↑ {sent} GB/s | ↓ {recv} GB/s")


def monitor():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        get_system_info()

        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        color = Fore.GREEN if cpu < 50 else Fore.YELLOW if cpu < 80 else Fore.RED
        print(color + f"CPU: {cpu}%")

        color2 = Fore.GREEN if ram.percent < 50 else Fore.YELLOW if ram.percent < 80 else Fore.RED
        print(color2 + f"RAM: {ram.percent}% | Свободно: {bytes_to_gb(ram.available)} GB / Всего: {bytes_to_gb(ram.total)} GB")

        color3 = Fore.GREEN if disk.percent < 50 else Fore.YELLOW if disk.percent < 80 else Fore.RED
        print(color3 + f"Диск: {disk.percent}% | Свободно: {bytes_to_gb(disk.free)} GB / Всего: {bytes_to_gb(disk.total)} GB")


        time.sleep(1)

if __name__ == "__main__":
    monitor()
