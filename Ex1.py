import re
d={}
with open('color_names.txt','r') as p:
    for line in p.readlines():
        #print(line)
        #x=re.match("%w+",line)
        #print(x)
        m = re.findall(r'\w+',line)
        #print(m)
        n = re.findall(r'\d+',line)
        rgb_code =(n[0],n[1],n[2])
        d[m[0]]=rgb_code

        
        #print(n)
        
