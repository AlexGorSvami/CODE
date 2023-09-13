from  bs4 import BeautifulSoup

# with open('lessons/index.html') as file:
#     src = file.read()

# soup = BeautifulSoup(src, 'lxml')

# title = soup.title
# print(title.text)
# print(title.string)

# page_h1 =  soup.find('h1')
# print(page_h1)
# print(page_h1.text)


# html_doc = """
# <html>
#     <head>
#         <title>Example Page</title>
#     </head>
#     <body>
#         <h1>Hello World</h1>
#         <p class="info">This is a paragraph.</p>
#         <p class="info">This is another paragraph.</p>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# first_h1 = soup.find('h1')
# print(first_h1)
# print(first_h1.text)

# first_p = soup.find('p', {'class': 'info'})
# print(first_p)
# print(first_p.text)

# html1 = """
# <html>
#     <body>
#         <h1>Заголовок 1</h1>
#         <p class="text-class">Текст 1</p>
#         <p class="text-class">Текст 2</p>
#         <p id="text-id">Текст 3</p>
#         <a href="https://google.com">Google</a>
#         <a href="https://yandex.ru">Yandex</a>
#     </body>
# </html>
# """

# soup1 = BeautifulSoup(html1, 'html.parser')
# result = soup1.find_all('a', href=True)
# for tag  in result:
#     print(tag['href'], tag.text)


# html = """
# <html>
#     <body>
#         <h1>Example Page</h1>
#         <p>This is some text.</p>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 2</li>
#             <li>Item 3</li>
#         </ul>
#         <p>This is some more text.</p>
#         <p>This is even more text.</p>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html, 'html.parser')
# all_text = soup.get_text()
# print(all_text)

# html = """
# <html>
#     <body>
#         <h1>Заголовок 1</h1>
#         <p class="text-class">Текст 1</p>
#         <p class="text-class">Текст 2</p>
#         <p id="text-id">Текст 3</p>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html, 'lxml')
# result = soup.select('p.text-class')
# for tag in result:
#     print(tag.text)
# print('------------------')
# result = soup.select('p#text-id')
# for tag in result:
#     print(tag.text)
# print('------------------')
# result = soup.select('body p')
# for tag in result:
#     print(tag.text)


# html = """
# <html>
#   <body>
#     <p class="highlight">This is a highlighted paragraph.</p>
#     <p>This is a normal paragraph.</p>
#     <div id="div1">
#       <p>This is a paragraph in a div.</p>
#     </div>
#   </body>
# </html>
# """

# soup = BeautifulSoup(html, 'lxml')
# highlighted_pars = soup.select('.highlight')
# for para in highlighted_pars:
#     print(para.text)
# print('-------------------')

# div_pars = soup.select('#div1 p')
# for i in div_pars:
#     print(i.text)


# html = """
# <html>
#   <body>
#     <div id="div1">
#       <p class="highlight">This is a highlighted paragraph in div1.</p>
#       <p>This is a normal paragraph in div1.</p>
#     </div>
#     <div id="div2">
#       <p class="highlight">This is a highlighted paragraph in div2.</p>
#       <p>This is a normal paragraph in div2.</p>
#     </div>
#   </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")

# # Выберем все параграфы с классом "highlight", которые 
# # находятся внутри элементов с идентификатором "div1" или "div2"
# highlighted_paras = soup.select("#div1 .highlight, #div2 .highlight")
# print("Highlighted paragraphs:")
# for para in highlighted_paras:
#     print(para.text)


# html = """
# <html>
#   <body>
#     <div id="div1">
#       <p class="highlight">This is a highlighted paragraph in div1.</p>
#       <p>This is a normal paragraph in div1.</p>
#     </div>
#     <div id="div2">
#       <p class="highlight">This is a highlighted paragraph in div2.</p>
#       <p>This is a normal paragraph in div2.</p>
#     </div>
#   </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")
# highlighted_paras = soup.select("p[class='highlight']")
# for para in highlighted_paras:
#     print(para.text)

# print(soup.select_one("p[class='highlight']").text)


# html_doc = """
# <html>
#     <head>
#         <title>Page Title</title>
#     </head>
#     <body>
#         <div class="container">
#             <p>This is a paragraph.</p>
#             <p>This is another paragraph.</p>
#         </div>
#         <div class="container">
#             <p>This is a third paragraph.</p>
#             <p>This is a fourth paragraph.</p>
#         </div>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# first_container = soup.select_one('.container p')
# print(first_container.text)

# html = """
# <html>
#   <body>
#     <p>This is a paragraph.</p>
#   </body>
# </html>
# """

# soup = BeautifulSoup(html, "html.parser")
# p_element = soup.find('p')
# parent  =  p_element.parent
# print(parent.name)


# html_doc = """
# <html>
#   <head>
#     <title>Example Page</title>
#   </head>
#   <body>
#     <p>This is a paragraph.</p>
#   </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# p_tag = soup.find('p')
# body_tag = p_tag.parent
# print(body_tag)


# html_doc = """
# <html>
#   <head>
#     <title>Example Page</title>
#   </head>
#   <body>
#     <div class="content">
#       <p>This is some content.</p>
#       <p>This is some more content.</p>
#     </div>
#   </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')
# content = soup.find('div', {'class': 'content'})

# for child in content.children:
#     print(child)

# html = """
# <html>
#     <body>
#         <h1>Example Page</h1>
#         <p>This is some text.</p>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 2</li>
#             <li>Item 3</li>
#         </ul>
#     </body>
# </html>
# """


# soup = BeautifulSoup(html, 'html.parser')

# header = soup.h1
# next_subling = header.next_sibling
# while next_subling:
#     print(next_subling)
#     next_subling = next_subling.next_sibling


# html = """
# <html>
#     <body>
#         <h1>Example Page</h1>
#         <p>This is some text.</p>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 2</li>
#             <li>Item 3</li>
#         </ul>
#         <p>This is some more text.</p>
#         <p>This is even more text.</p>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html, 'html.parser')

# last_list_item = soup.find_all('li')[-1]

# previous_sibling = last_list_item.previous_sibling
# while previous_sibling:
#     print(previous_sibling)
#     previous_sibling = previous_sibling.previous_sibling


# html = """
# <html>
#     <body>
#         <h1>Example Page</h1>
#         <p>This is some text.</p>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 2</li>
#             <li>Item 3</li>
#         </ul>
#         <p>This is some more text.</p>
#         <p>This is even more text.</p>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html, 'html.parser')

# first_p = soup.li
# print(first_p)
# next_el = first_p.next_element
# while next_el:
#     print(next_el)
#     next_el = next_el.next_element

# last_p = soup.find_all('p')[-1]
# previous_el = last_p.previous_element
# print(previous_el)
# print(previous_el.previous_element)

# html_doc = """
# <html>
#     <head>
#         <title>Example Page</title>
#     </head>
#     <body>
#         <div id="main">
#             <h1>Hello World</h1>
#             <p class="info">This is a paragraph.</p>
#             <p class="info">This is another paragraph.</p>
#             <ul>
#                 <li>Item 1</li>
#                 <li>Item 2</li>
#                 <li>Item 3</li>
#             </ul>
#         </div>
#         <div id="secondary">
#             <p>Some additional information.</p>
#         </div>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')

# main_div = soup.find('div', {'id':'main'})
# info_p = main_div.find('p', {'class': 'info'})
# info_p.decompose()
# h1 = main_div.find('h1').extract()
# new_h1 = soup.new_tag('h1', class_='new_class_tag')
# new_h1.string = 'Welcome'
# soup.body.insert(0, new_h1)
# print(main_div)
# print(h1)
# print(soup)


html_doc = """
<body>
  <p>Some text</p>
</body>
"""

soup = BeautifulSoup('html_doc', 'lxml')

p_tag = soup.body.p
p_tag.wrap(soup.new_tag('div', class_='wrap_tag'))

print(soup)