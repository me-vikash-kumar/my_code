from pathlib import Path

py_text=Path('Learning_Python.txt')
<<<<<<< HEAD

content=py_text.read_text()

print(content)

print('='*90)
for i in content.splitlines():
    print(i.replace("Python","C"))
=======
content=Path.read_text(py_text)
print(content)

print('='*50)

list_content =content.splitlines()

for i in list_content:
    print(i.replace('Python',"C"))

>>>>>>> 68262f93a26588fd9221c95484b2c4ed3982dead
