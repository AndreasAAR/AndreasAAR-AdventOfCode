import os
here = os.path.dirname(os.path.abspath(__file__))

        
def star1():
    with open(here+"/data.txt", "r") as file:
        hori = 0
        dep = 0
        for line in file:
                type,val = line.replace("\n","").split(" ")
                hori += int(val) if type == "forward" else 0
                dep -= int(val) if type == "up"  else  0
                dep += int(val) if type == "down" else 0
        print(dep*hori)

def star2():
    with open(here+"/data.txt", "r") as file:
        hori = 0
        dep = 0
        aim = 0
        for line in file:
                type, val = line.replace("\n", "").split(" ")
                val = int(val)
                aim -= val if type == "up" else 0
                aim += val if type == "down" else 0
                hori += val if type == "forward" else 0
                dep += aim*val if (aim != 0 and type == "forward") else 0
        print(dep*hori)

star2()