import os
import subprocess
import time

ip = input("Enter the IP Address : ")
result = subprocess.Popen(["ping", "-w", "2", ip]).wait()
print()
if result:
    print(ip, "inactive")
else:
    print(ip, "active")


def is_tool(program_check):
    for directory in os.environ['PATH'].split(os.pathsep):
        if os.path.exists(os.path.join(directory, program_check)):
            print(program_check[:-4], "exist in ", os.path.join(directory, program_check))
            return
    print(program_check[:-4], "not exist in this System")
    return


time.sleep(1)
print("\nChecking Programs . . .")
time.sleep(1)
while True:
    print("""\n\t1. Python\n\t2. kubectl\n\t3. AWS\nEnter the Program do you want to check ( 0 to exit ) :""")
    choice = int(input())
    Program_list = ["python.exe", "kubectl.exe", "aws.exe"]
    if choice == 0:
        print("Successfully Stopped . . .")
        exit(1)
    else:
        is_tool(Program_list[choice - 1])
