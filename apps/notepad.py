
import os

def Notepad():
    while True:
        command = input("Notepad > ")
        if command == "exit":
            break
        elif command == "clear":
            os.system("cls")
        elif command == "file":
            filename = input("File Name > ")
            file = open(f"{filename}.txt", "a+")

            while True:
                cmd = input(f"{filename}.txt > ")

                if cmd == "exit":
                    break
                elif cmd[0:7] == "append ":
                    l = len(file.read())
                    file.seek(l)
                    file.write(cmd[7:len(cmd)])
                elif cmd == "view":
                    file.seek(0)
                    print(file.read())
                elif cmd == "clear":
                    file = open(f"{filename}.txt", "w+")
                else:
                    print("Command not found.")
        else:
            print("Command not found.")