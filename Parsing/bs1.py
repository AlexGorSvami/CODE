from bs4 import BeautifulSoup

with open('/home/alex/CODE/Parsing/lessons/index.html') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')

print(soup)