# --> WEB SCRAPING

from urllib.request import urlopen  # penerapan library BeautifulSoup
from bs4 import BeautifulSoup

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print("Judul halaman (menggunakan BeautifulSoup):", soup.title.string)

url = "http://python.org/"  
page = urlopen(url)
html = page.read().decode("utf-8")

start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
print("Judul halaman (menggunakan pencarian manual):", title)
