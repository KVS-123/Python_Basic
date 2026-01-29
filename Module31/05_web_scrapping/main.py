import re

with open('examples.html', 'r') as f:
    text = f.read()

pattern = re.compile(r'<h3>.+</h3>')
result = [i[4:-5] for i in pattern.findall(text)]
print(result)