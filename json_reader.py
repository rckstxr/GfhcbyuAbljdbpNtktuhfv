import json

with open("cybersquatt_text.txt", "a") as w:
    with open("cybersquatt_messages.json", "r") as f:
        data = json.load(f)
        try:
            for i in range(len(data)):
                text_message = data[i]["message"]+'\n'
                w.writelines(text_message)
        except KeyError:
            print('Нет ключа "message"')
        else:
            i = i+1
        finally:
            f.close()
w.close()
