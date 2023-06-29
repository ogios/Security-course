import os
from course import getUndoneSeps

RUN = "python"
FILE = "./main.py"


def monitor():
    seps = getUndoneSeps()
    while seps:
        out = os.popen(f"{RUN} {FILE}")
        print(out.read())
        seps = getUndoneSeps()

if __name__ == "__main__":
    monitor()