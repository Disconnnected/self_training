from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


"""
<html>
<head>
<title>Profile: Aphrodite</title>  
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/aphrodite.gif" />
<h2>Name: Aphrodite</h2>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html>
"""


# url = "http://olympus.realpython.org/profiles/aphrodite"
# url = "http://olympus.realpython.org/profiles/poseidon"
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>", "", title)

# title_index = html.find("<title>")
# start_index = title_index + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]
# print(title)

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
x = soup.get_text()
x = soup.find_all("img")
image1, image2 = soup.find_all("img")
x = image1.name

print(x)




