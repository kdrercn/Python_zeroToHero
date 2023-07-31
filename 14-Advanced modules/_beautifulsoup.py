html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

<h1 id="header">
        Python Kursu
      </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")   

result = soup.prettify() # htmlyi düzenler
result = soup.title
result = soup.head
result = soup.body

result = soup.title.string

result = soup.h1
result = soup.h2.string # ilk h2yi alır

result = soup.find_all("h2") # tüm h2leri alır
result = soup.find_all("h2")[0]

result = soup.div # ilk divi alır
result = soup.find_all("div")
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren() # div içi
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all("a")

for link in result:
    print(link.get("href"))

# print(result)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/