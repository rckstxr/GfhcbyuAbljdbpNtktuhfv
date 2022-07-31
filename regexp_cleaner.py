import re

regexp = re.compile('^.*\..*')
with open("cybersquatt_clear.txt", "a") as c:
    with open("cybersquatt_text.txt", "r") as r:
        strings = r.readlines()
        for i in strings:
            find_regexp = regexp.findall(i)
            try:
                if find_regexp[0]:
                    clear_line = find_regexp[0]+'\n'
                    c.writelines(clear_line)
            except:
                print('Значение не подходит под регулярное выражение')
    r.close()
c.close()
