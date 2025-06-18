from pathlib import Path

py_text=Path('Learning_Python.txt')
content=Path.read_text(py_text)
print(content)

print('='*50)

list_content =content.splitlines()

for i in list_content:
    print(i.replace('Python',"C"))

