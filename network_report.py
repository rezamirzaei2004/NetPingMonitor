import subprocess
from datetime import datetime

devices = {"google.com","4.2.2.4"}

def ping(host):
    param = "-n"if subprocess.os.name == "nt" else "-c"
    command = ["ping",param,"1",host]
    try:
        subprocess.check_output(command)
        return True
    except subprocess.CalledProcessError:
        return False
def report(devices):
    rline=[]
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rline.append(f"status report -{date} \n")

    for device in devices:
        status ="online" if ping(device) else "offline"
        line = f"{device}:{status}"
        print(line)
        rline.append(line)

    return "\n".join(rline)

def save (report,file_name = "report.txt"):
    with open (file_name,"w") as f:
        f.write(report)
    print(f"\nsave to {file_name}")


if __name__=="__main__":
    report=report(devices)
    save(report)