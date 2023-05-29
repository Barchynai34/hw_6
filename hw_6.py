import re
class Data:
    def __init__(self, full_name, email, file_name, color) -> None:
        self.full_name = full_name
        self.email = email
        self.file_name = file_name
        self.color = color


    @property
    def full_name(self):
        return self.full_name
    
    @full_name.setter
    def full_name(self, new_full_name):
        self.full_name = new_full_name



    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, new_email):
        self.email = new_email


    @property
    def file_name(self):
        return self.file_name
    
    @file_name.setter
    def file_name(self, new_file_name):
        self.file_name = new_file_name


    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self, new_color):
        self.color = new_color


with open ('mock_data.txt', 'r', encoding="utf-8") as file:
    content = file.readlines()
    for line in content:
        print(re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", line))


full_name = re.findall(r"[А-Я][а-я]+\s+[А-Я]\.[А-Я]\.", content)
print(full_name)

email =  re.match(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", content)
print(email)

file_name = ['mock_data.txt','abcdEFGHI.htm']
for filename in file_name:
    print(filename, bool(re.search(r'^[A-Za-z]{1,8}\.[A-Za-z]{1,3}$', filename)), sep = ' => ')

color = re.match (r'[0-9A-Fa-f]{6}', input('Введите проверяемую строку: '))
if a == None:
    print('Строка не является идентификатором цвета')
else:
    print('Введенная строка - идентификатор цвета')
