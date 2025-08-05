from pathlib import Path

py_text=Path('Learning_Python.txt')

content=py_text.read_text()

print(content)

print('='*90)
for i in content.splitlines():
    print(i.replace("Python","C"))