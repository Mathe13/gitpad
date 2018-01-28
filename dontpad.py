import requests
import re

#req=requests.get(url="http://dontpad.com/teste.body.json?lastUpdate=0")


def get_data(page_name,key):
    url=""
    if key=="NONE":
        url="http://dontpad.com/"+page_name+".body.json?lastUpdate=0"
    else:
        url="http://dontpad.com/"+key+"/"+page_name+".body.json?lastUpdate=0"
    req=requests.get(url=url)
    index=re.search(pattern=r'"body":',string=req.text)
    #data=req.text[int(index[0]):]
    return(req.text[(int(index.span()[0])+8):-2])

def post_data(page_name,content):
    req=requests.post(url="http://dontpad.com/"+page_name,data={"text" : content})
    pass
if (__name__=='__main__'):
    print("cod finalizado")
