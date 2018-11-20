import urllib, json
def main():
    print ("Hello")
    getWD("Test")

def getWD(dbp_id):
    #Function to call the Wikipedia API
    #using the dbPedia ID as reference
    #Will create response in JSON
    # which can be used to get the Q number.

    url= "https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&titles=Arnolfini_portrait&format=json"
    response = urllib.urlopen(url)

    data = json.loads(response.read())
    print(data)