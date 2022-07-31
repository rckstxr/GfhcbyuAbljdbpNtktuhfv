import re

with open("final.txt", "w") as p:
    with open("cybersquatt_clear.txt", "r") as c:
        strings = c.readlines()
        for i in strings:
            clear = re.sub(r'\[\.\]', r'.', i)
            p.writelines(clear)
    c.close()
p.close()
