import ezodf
import pandas as pd
import scrapy
import requests
import re
#import wget
import time
import json
import ntpath
import os
import subprocess


def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})


def birdname2url(birdname):
    query = birdname.replace(' ', '_')
    if(birdname == 'Rusty Blackbird '):
        query = 'Rusty_Blackbird'
    if(birdname == 'Cooper’s Hawk'):
        query = 'Coopers_Hawk'
    if(birdname == 'Ruby throated Hummingbird '):
        query = 'Ruby-throated_Hummingbird'
    if(birdname == 'Eastern Screech Owl'):
        query = 'Eastern_Screech-Owl'
    if(birdname == 'Tennessee Warbler '):
        query = 'Tennessee_Warbler'
    if(birdname == 'Wilson’s Warbler'):
        query = 'Wilsons_Warbler'
    return 'https://www.allaboutbirds.org/guide/{}'.format(query)

#FNULL = open(os.devnull, 'w')

def safedownload(url, target):
    filename = ntpath.basename(url)
    #value = os.system()
    value = subprocess.call('wget {}'.format(url), shell=True)
    if(not os.path.isfile(filename)):
        print('Failed to download {}'.format(url))
    else:
        subprocess.call('mv {} {}'.format(filename, target), shell=True)
        time.sleep(0.5)
    #try:
    #    wget.download(url, target)
    #    time.sleep(0.5)
    #except:
    #    print('Could not download {}'.format(url))
    #    pass


# Load the bird names we want to search
df = read_ods(filename='Birds_RockCreekPark.ods')
birdnamelist = df.iloc[:, 0].values

down = 0;
imgfolder = 'allaboutbirds/pictures/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

birddata = {}
for (count, birdname) in enumerate(birdnamelist):
    # main bird info page
    url = birdname2url(birdname)
    html = requests.get(url, headers=headers).content
    sel = scrapy.Selector(text=html)
    if not sel.css(' div.species-info h4::text').extract_first():
        print(' Could not find: {}'.format(birdname))
        continue
    print(' {}. Scraping info for: {}'.format(str(count+1), birdname))
    # species info
    data = {}
    data["common-name"] = sel.css(' div.species-info h4::text').extract_first().strip()
    data["scientific-name"] = sel.css(' div.species-info i::text').extract_first().strip()
    data["order"] = sel.css(' div.species-info ul.additional-info li::text')[0].extract().strip()
    data["family"] = sel.css(' div.species-info ul.additional-info li::text')[1].extract().strip()
    # LH menu
    lh_img_urls = sel.css(' div.row ul.LH-menu li img').xpath('@src').extract()
    data["lhs_headers"] = [txt.strip() for txt in sel.css(' div.row ul.LH-menu li a.text-label').xpath('span[1]/text()').extract()]
    data["lhs_texts"] = [txt.strip() for txt in sel.css(' div.row ul.LH-menu li a.text-label').xpath('span[2]/text()').extract()]
    if(down == 1):
        prefix = data["scientific-name"].replace(' ', '-')
        for i, imgurl in enumerate(lh_img_urls):
            imgurl = 'https://www.allaboutbirds.org'+imgurl
            safedownload(imgurl, '{}{}_{}_icon.png'.format(imgfolder, prefix, data["lhs_headers"][i]))
    # group
    data["group"] = sel.css(' div.silo-group span::text').extract_first().strip()
    #group_img_url = sel.css(' div.silo-group img').xpath('@src').extract_first()
    # move to id page
    url2 = url+'/id'
    html = requests.get(url2, headers=headers).content
    sel = scrapy.Selector(text=html)
    # get the links to the images
    data["imgs_text"] = sel.css(' div.slick-3 img').xpath('@alt').extract()
    data["imgs_url"] = [re.findall('https:[^\s]+720px.jpg', links)[0]
                        for links in sel.css(' div.slick-3 img').xpath('@data-interchange').extract()]
    data["measure-info"] = sel.css(' div.rel-size ul.add-info li::text').extract()
    if(down == 1):
        prefix = data["scientific-name"].replace(' ', '-')
        for i, imgurl in enumerate(data["imgs_url"]):
            safedownload(imgurl, '{}{}_{}.jpg'.format(imgfolder, prefix, i))
    birddata[birdname] = data
    del sel
    del html
    del data
    print('')
    time.sleep(0.5)


with open('allaboutbirds/Allaboutbirds_RockCreekPark_json.txt', 'w') as outfile:
    json.dump(birddata, outfile)
