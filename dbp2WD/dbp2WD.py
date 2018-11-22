import requests, json
from pathlib import Path

def main():
    #Add code here to ask user to choose a TXT file from their computer
    Filepath = Path("C:/Users/Terry/Desktop/Test.txt")
    content=list()
    WDList=list()
    content = readTXTFile(Filepath)
    for x in content:
       WDList.append(getWD(x))
    exporttoTXT(content,WDList)
    

def exporttoTXT(dbps, wdids):
        #Take the two lists and combine into a single text file
        dictionary = dict(zip(dbps, wdids))
        print(dictionary)

def readTXTFile(path):
    with open(path, encoding='utf-16') as f:
        contentIn= f.readlines()
        contentIn = [x.strip() for x in contentIn]
      #  content = contentIn.replace(u'\ufeff', '')
        print(contentIn)
        return contentIn

    #use this to read in a text file with a list of DBpedia ID's.

def getWD(dbp_id):
    #Function to call the Wikipedia API
    #using the dbPedia ID as reference
    #Will create response in JSON
    # which can be used to get the Q number.

    url="https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&titles=" + dbp_id + "&format=json"
    r= requests.get(url)
    data = r.json()
    page = data['query']['pages']
    for key in page:
        WDID= page[key]['pageprops']['wikibase_item']
    return WDID


if __name__ == "__main__":
    main()