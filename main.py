import sys, os, datetime

from apps.notepad import Notepad

os.system("cls")
version = (0, 1, 1, 0)

print("""█████ █   █ █████ █   █ █████ █     █     
  █   █   █ █     █   █ █     █     █     
  █   █████ █████ █████ ████  █     █     
  █   █   █     █ █   █ █     █     █     
  █   █   █ █████ █   █ █████ █████ █████ """)
print(f"THShell Version {version}\n")

while True:
    command = input("THshell > ")


    if command == "sysinfo":
        print(f"THshell Version {version}")
    elif command == "exit":
        sys.exit()
    elif command == "clear":
        os.system("cls")
    elif command == "time":
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    elif command == "notepad":
        Notepad()
    else:
        print("command not found.")