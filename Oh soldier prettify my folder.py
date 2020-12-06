import os


def soldier(filepath, dict_file, form):
    toot = dict_file.split('.')
    lst = os.listdir(filepath)
    value = toot[1]
    for i in lst:
        f = i.split('.')
        un = f[1]
        if un == form:
            n = 1
            t = str(n) + "jpg"
            os.rename(i, t)
            n += 1
        elif value != un:
            os.rename(i, i.capitalize())
        elif (value == 'TXT') or (value == 'txt'):
            return i


soldier(r'C:\Users\Shivang Yadav\PycharmProject\firstprog', 'DIETH.TXT', 'jpg')
