import os
here = os.path.dirname(os.path.abspath(__file__))
f = list(map(int, open(here+"/data.txt", "r").read().split("\n")))

num_inc = 0
prev = ""
for i in range(2,len(f)):
        print(f[i-2: i+1])
        current = sum(f[i-2: i+1])
        if prev != "":
            if prev < current:
                num_inc +=1 
        prev =  current  

print(num_inc)