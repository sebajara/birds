from bs4 import BeautifulSoup
import requests
import wget
import time
import ezodf
import pandas as pd
import json

parentsite = 'https://www.audubon.org'


def birdnameequal(name1, name2):
    # for now something super simple, but can make more sophisticated in
    # the future
    return (name1.lower() == name2.lower())


def searchAudubonBird(birdname):
    url = 'https://www.audubon.org/bird-guide?search_api_views_fulltext='+birdname+'&field_bird_family_tid=All&field_bird_region_tid=All'
    # Search for birds matching the name
    searchSoup = BeautifulSoup(requests.get(url).text, "html5lib")
    # Focus on the card-illustrations for the link and common-name for matching
    links = [parentsite+link.a['href'] for link in
             searchSoup.findAll('div', attrs={"class": 'bird-card-illustration'})]
    names = [h4.text.strip() for h4 in
             searchSoup.findAll('h4', attrs={"class": 'common-name'})]
    # Number of results (should be 1)
    nresults = len(links)
    if(nresults >= 1):
        if(nresults == 1):
            return (
                BeautifulSoup(requests.get(links[0]).text, "html5lib"),
                searchSoup.findAll('div', attrs={"class": 'bird-card-illustration'})[0].img['src']
            )
        else:
            submatch = [i for i in range(nresults)
                        if birdnameequal(birdname, names[i])]
            if(len(submatch) == 1):
                return (
                    BeautifulSoup(requests.get(links[submatch[0]]).text, "html5lib"),
                    searchSoup.findAll('div', attrs={"class": 'bird-card-illustration'})[submatch[0]].img['src']
                )
            else:
                print('In bird {}: wrong name matching'.format(birdname))
    else:
        print("No matches for bird: "+birdname)


#birdSoup, artimgurl = searchAudubonBird('Eastern Bluebird')
        

def getFieldGuideInfo(birdname, down=False,
                      imgfolder='audubon/pictures/', audiofolder='audubon/songs/'):
    birdSoup, artimgurl = searchAudubonBird(birdname)
    birdinfodict = {}
    # ==== Parsing text
    # names at the top
    birdinfodict["Common name"] = birdSoup.findAll('h1', attrs={"class": 'common-name'})[0].text.strip()
    birdinfodict["Scientific name"] = birdSoup.findAll('p', attrs={"class": 'scientific-name'})[0].text.strip()
    # brief summary text
    birdinfodict["Description"] = birdSoup.findAll('div', attrs={"class": 'hide-for-tiny hide-for-small hide-for-medium'})[0].text.strip()
    # top table with info
    table = birdSoup.findAll('table', attrs={"class": "collapse"})[0].find_all('tr')
    birdinfodict["Conservation"] = table[0].find_all('td')[0].text.strip()
    birdinfodict["Family"] = table[1].find_all('td')[0].text.strip()
    birdinfodict["Habitat"] = table[2].find_all('td')[0].text.strip()
    # more info from the table
    infotable = birdSoup.findAll('section', attrs={"class": 'bird-guide-section left-col sans'})
    infoheaders = infotable[0].findAll('h5')
    infotext = infotable[0].findAll('p')
    for h, p in zip(infoheaders, infotext):
        birdinfodict[h.text.strip()] = p.text.strip()
    # migration text
    birdinfodict["Migration"] = birdSoup.findAll('section', attrs={"id": 'bird-migration'})[0].p.text.strip()
    # Getting images
    # map image
    birdmapurl = birdSoup.findAll('section', attrs={"id": 'bird-map'})[0].findAll('img')[0]['src']
    birdmapurl = birdmapurl.replace('%27','\'') # for quotes
    # pictures
    birdimgsurls = []
    birdimgscredits = []
    if(birdSoup.findAll('ul', attrs={"class": 'row grid-gallery__thumbs'})):
        imgtable = birdSoup.findAll('ul', attrs={"class": 'row grid-gallery__thumbs'})[0].find_all('li')
        for row in imgtable:
            birdimgsurls.append(row.a['href'])
            # TODO: replace by regex
            credit = row.img['data-credit'].strip()
            credit = credit.replace('Photo:   ', '')
            credit = credit.replace('/', '_')
            credit = credit.replace('&amp;', '')
            credit = credit.replace(' ', '-')
            birdimgscredits.append(credit)
    # Getting audio
    audiotable = birdSoup.findAll('div', attrs={"class": 'field-name-field-bird-audio'})[0].find_all('li')
    birdaudiourls = []
    birdaudionames = []
    for row in audiotable:
        name = row.a.text.strip()
        name = name.replace('#', '')
        name = name.replace('&', 'and')
        name = name.replace(' ', '-')
        birdaudionames.append(name)
        birdaudiourls.append(row.a['href'])
    if(down):
        prefix = birdinfodict["Scientific name"].replace(' ', '-')
        wget.download(artimgurl, '{}{}_art.jpg'.format(imgfolder, prefix))
        time.sleep(1)
        wget.download(birdmapurl, '{}{}_map.jpg'.format(imgfolder, prefix))
        time.sleep(1)
        for i, url in enumerate(birdimgsurls):
            try:
                wget.download(url, '{}{}_{}_{}.jpg'.format(imgfolder, prefix, i, birdimgscredits[i]))
                time.sleep(1)
            except:
                pass
        for i, url in enumerate(birdaudiourls):
            try:
                wget.download(url, '{}{}_{}_{}.mp3'.format(audiofolder, prefix, i, birdaudionames[i]))
                time.sleep(1)
            except:
                pass
    return(birdinfodict)


def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})


# Load the data we want to search
df = read_ods(filename='Birds_RockCreekPark.ods')
birdnamelist = df.iloc[:, 0].values

# First let's check that all names have search results
matcheslist = []
for count, birdname in enumerate(birdnamelist):
    url = 'https://www.audubon.org/bird-guide?search_api_views_fulltext='+birdname+'&field_bird_family_tid=All&field_bird_region_tid=All'
    # Search for birds matching the name
    searchSoup = BeautifulSoup(requests.get(url).text, "html5lib")
    # Focus on the card-illustrations for the link and common-name for matching
    links = [parentsite+link.a['href'] for link in
                  searchSoup.findAll('div', attrs={"class": 'bird-card-illustration'})]
    names = [h4.text.strip() for h4 in
                  searchSoup.findAll('h4', attrs={"class": 'common-name'})]
    # Number of results (should be 1)
    nresults = len(links)
    print('{}. Number of matches for {}: {}'.format(str(count), birdname, nresults))
    if(nresults >= 1):
        # Get the ulr for the field-guide info
        matcheslist.append(names)
    else:
        matcheslist.append([])
nmatcheslist = [len(names) for names in matcheslist]
nomatches = [birdnamelist[i] for i in range(len(birdnamelist)) if nmatcheslist[i] == 0]
print('Birds with no match:')
print(nomatches)
multiplematches = [birdnamelist[i] for i in range(len(birdnamelist)) if nmatcheslist[i] > 1]
mutipleanswers = [matcheslist[i] for i in range(len(birdnamelist)) if nmatcheslist[i] > 1]
print('Birds with multiple matches:')
for bname, matches in zip(multiplematches, mutipleanswers):
    print('{} -> {}'.format(bname, matches))
    submatch = [ans for ans in matches if birdnameequal(bname, ans)]
    print('   Good match: {}'.format(submatch))

# Search, get the info for each bird, and and download images and audio
info = {}
for i, birdname in enumerate(birdnamelist):
    print("Getting bird {}: {}".format(str(i), birdname))
    #birdinfodict = getFieldGuideInfo(birdname)
    #info[birdinfodict["Scientific name"]] = birdinfodict
    if(i > 38):
        birdinfodict = getFieldGuideInfo(birdname, down=True)
        time.sleep(1)
        print("\n")

with open('audubon/Audubon_RockCreekPark_json.txt', 'w') as outfile:
    json.dump(info, outfile)



