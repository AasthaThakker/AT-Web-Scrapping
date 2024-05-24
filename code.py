import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")

# ----- SCRAPING THE CONTENT USING BEAUTIFUL SOUP ----- #

r = requests.get(url)
htmlcontent = r.content  # Here HTML is the variable
soup = BeautifulSoup(htmlcontent, 'html.parser')

# ----- PRINTING OUT HTML PAGE IN HTMLCONTENT.HTML FILE ----- #

# Save the output in a file named "htmlcontent.html"
with open("htmlcontent.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
print("HTML content saved in: htmlcontent.html")

# -----  PRINTING OUT HTML CONTENT IN HTMLTEXT.TXT --- #

with open("htmltext.txt", "w",encoding="utf-8") as file:
    file.write(soup.get_text())
print("Text content of HTML page is saved at: htmltext.txt")

# ----- PRINTING OUT LINKS FROM THE HTML PAGE IN LINKS.TXT ----- # 

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        all_links.add(url + link.get('href'))

with open("links.txt", "w",encoding="utf-8") as file:
    for link in all_links:
        file.write(link+"\n")     

print("Anchor links saved in: links.txt")
