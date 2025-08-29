from bs4 import BeautifulSoup


SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle"> This is a paragraph </p>
<p>This is a paragraph without class</p>
<ul>
<li>John</li>
<li>Ben</li>
<li>Amy</li>
<li>Suzy</li>
</ul>
</body>
</html>'''

simple_html = BeautifulSoup(SIMPLE_HTML,'html.parser')

print(simple_html.find('h1'))
print(simple_html.find('h1').string) ##Taking a text from certain element in HTML

def find_title():
    h1_tag = simple_html.find('h1')
    print(h1_tag.string)

find_title()

def find_list_items():
    list_items = simple_html.find_all('li')
    list_contents = [e.string for e in list_items]
    #print(list_items)
    print(list_contents)

find_list_items()

def find_subtitle():
    paragraph = simple_html.find('p' ,{'class' : 'subtitle'})
    print(paragraph.string)

find_subtitle()

def find_other_paragraph():
    paragraphs = simple_html.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class',[])]
    print(other_paragraph[0].string)

find_other_paragraph()

