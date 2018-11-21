import requests, json


def main():
    print ("Hello")
    getWD("Arnolfini_portrait")
    getWD("No._5,_1948")

def getWD(dbp_id):
    #Function to call the Wikipedia API
    #using the dbPedia ID as reference
    #Will create response in JSON
    # which can be used to get the Q number.

    url="https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&titles=" + dbp_id + "&format=json"
    r= requests.get(url)
    data = r.json()
    print(len(data))
    #print(data['query']['pages']['1036801']['pageprops']['wikibase_item'])
    #Need to iterate over the next bit to get pass the page ID - which we may not know
    page = data['query']['pages']
    for key in page:
        WDID= page[key]['pageprops']['wikibase_item']
        print(WDID)


if __name__ == "__main__":
    main()