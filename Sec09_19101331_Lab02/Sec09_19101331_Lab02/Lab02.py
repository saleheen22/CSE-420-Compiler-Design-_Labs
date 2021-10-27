t = int(input())


def mail_check(text):
    arht = text.find('@')
    dot = text.rfind('.')
    if 0 < arht < dot:
        tex1 = text[:arht].replace('-', '', len(text))+text[arht:]
        tex1 = tex1[:tex1.find('@')+1]+tex1[tex1.find('@')+1:].replace('.', '', len(tex1))
        tex1 = tex1.replace('.', '', len(tex1))
        if tex1[: tex1.find('@')].isalnum() and tex1[tex1.find('@') + 1:].isalpha():
            return True
    return False


def web_check(text):
    if text[:4] == 'www.' and text.rfind('.') > 4:
        d_name = text[4:text.rfind('.')]
        d_name = d_name.replace('-', '', len(d_name))
        d_name = d_name.replace('.', '', len(d_name))
        if d_name.isalnum():
            return True

    return False


for i in range(1, t + 1):
    text = input()
    if text[0].isalpha() and text[-1].isalpha():
        if mail_check(text):
            print('Email, ' + str(i))
        elif web_check(text):
            print('Web, ' + str(i))
        else:
            print("Invalid " + str(i))
    else:
        print("Invalid " + str(i))

