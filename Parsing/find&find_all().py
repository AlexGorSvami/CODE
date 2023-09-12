from  bs4 import BeautifulSoup

with open('lessons/index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

title = soup.title
print(title.text)
print(title.string)

page_h1 =  soup.find('h1')
print(page_h1)
print(page_h1.text)