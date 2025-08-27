import sys, os, datetime


os.system("cls")
version = (0, 1, 0, 0)

print("""█████ █   █ █████ █   █ █████ █     █     
  █   █   █ █     █   █ █     █     █     
  █   █████ █████ █████ ████  █     █     
  █   █   █     █ █   █ █     █     █     
  █   █   █ █████ █   █ █████ █████ █████ """)
print(f"THShell Version {version}\n")



def sysinfo():
    print(f"Version {version}")

def exit():
    sys.exit()

while True:
    command = input("THshell > ")


    if command == "sysinfo":
        sysinfo()
    elif command == "exit":
        exit()
    elif command == "clear":
        os.system("cls")
    elif command == "time":
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("command not found.")