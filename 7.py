from datetime import datetime

try:
    with open("test.log") as f:
        with open("log_backup.txt", "w") as f1:
            for x in f.readlines():
                f1.write((datetime.now().strftime("%m-%d %H:%M:%S.%f")[:-3] + " " + x))
    print("Log Read Successfully")
except:
    print("Log File Not Found ")
