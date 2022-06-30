import requests
from bs4 import BeautifulSoup

res=requests.get("https://www.coingecko.com/")
cres=BeautifulSoup(res.text,'html.parser')
find_allc=cres.find_all('td', class_="td-change7d")
find_alln=cres.find_all('td', class_="py-0 coin-name cg-sticky-col cg-sticky-third-col px-0 tw-max-w-40 tw-w-40")

variation7d=[]
for i in find_allc:
    var=i.find("span").text

    var=var.replace('%\n','')
    var=var.replace('%','')
    variation7d.append(float(var))

currency=[]
for i in find_alln:
    var=i.a.text
    var=var.replace('\n','',2)
    currency.append(var)

dict_from_list = dict(zip(currency, variation7d))


bestcr=""
bestperf=0
worstcr=""
worstperf=0

for key, value in dict_from_list.items():
    if value >bestperf:
        bestperf=value
        bestcr=key
    if value< worstperf:
        worstperf=value
        worstcr=key

worstperf=str(worstperf)
bestperf=str(bestperf)

print("More info on "+bestcr+" the crypto that went up " +bestperf+" percent over the past 7 days")
print("https://www.google.com/search?q="+bestcr+"+crypto"+"+news")
print("More info on "+worstcr+" the crypto that went down " +worstperf+" percent over the past 7 days")
print("https://www.google.com/search?q="+worstcr+"+crypto"+"+news")
