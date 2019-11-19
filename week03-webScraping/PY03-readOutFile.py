from bs4 import BeautifulSoup

with open("../Week 2/Lab/carviewer2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
print(soup.tr)

rows = soup.findAll("tr")
for row in rows:
    print("------")
    print(row)

for row in rows:
    cols = row.findAll("td")
    for col in cols:
        print(col.text)

dataList = []
for col in cols:
    dataList.append(col.text)
print(dataList)