import ezodf
import pandas as pd
import json
import re
import numpy as np
import matplotlib.image as mpimg

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})


def birdimgfile(sciname, index):
    prefix = sciname.replace(' ', '-')
    imgfolder = 'pictures/'
    return '{}{}_{}.jpg'.format(imgfolder, prefix, index)


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


def getlenght(measure_info):
    if(not measure_info):
        return np.nan
    else:
        info_str = ' '.join(measure_info)
        length_strs = [lstr.split('-')
                       for lstr in re.findall('Length:.*?\((\d+(?:-\d+){0,1}) cm\)', info_str)]
        values = [int(n) for pair in length_strs for n in pair ]
        return(np.mean(values))
    re.findall('Length:.*?\((\d+(?:-\d+){0,1}) cm\)', 'Length: 3.1-4.7 in (8-12 cm)')
#lenlist = [len(birddata[name]['measure-info']) for name in birdnames]
#lenlist.index(3)
#measure_info = birddata[birdnames[111]]['measure-info']


with open('allaboutbirds/Allaboutbirds_RockCreekPark_Selected_json.txt') as json_file:
    birddata = json.load(json_file)

birdnames = list(birddata.keys())

data2 = {'name': [],
         'sciname': [],
         'family': [],
         'order': [],
         'genus': [],
         'group': [],
         'length': [],
         'selected_imgs': [],
         'selected_imgs_text': [],
         'mini_info_headers': [],
         'mini_info_text': [],
         'url': []}
for birdname in list(birddata.keys()):
    info = birddata[birdname]
    url = birdname2url(birdname)
    names = info['common-name'].split(' ')
    sciname = info['scientific-name']
    name = names[-1] + ", " + " ".join(names[:-1])
    order = info['order']
    family = info['family']
    genus = sciname.split(' ')[1]
    group = info['group']
    selected_imgs = info['Selected']
    selected_imgs_text = info['Selected_text']
    mini_info_headers = info['lhs_headers']
    mini_info_text = info['lhs_texts']
    length = getlenght(info['measure-info'])
    data2['name'].append(name)
    data2['sciname'].append(sciname)
    data2['family'].append(family)
    data2['order'].append(order)
    data2['genus'].append(genus)
    data2['group'].append(group)
    data2['length'].append(length)
    data2['selected_imgs'].append(selected_imgs)
    data2['selected_imgs_text'].append(selected_imgs_text)
    data2['mini_info_headers'].append(mini_info_headers)
    data2['mini_info_text'].append(mini_info_text)
    data2['url'].append(url)
    

df = pd.DataFrame(data2)

df.loc[df['name'] == 'Bobwhite, Northern','length'] = 22.86

df2 = df.dropna()

genuslengths = df2.groupby('genus')['length'].mean()
grouplengths = df2.groupby('group')['length'].mean()
orderlengths = df2.groupby('order')['length'].mean()
familylengths = df2.groupby('family')['length'].mean()


def safeserielookup(serie, value, default=0):
    if(value in serie.index):
        return serie[value]
    else:
        return default
    

df['genus_length'] = df['genus'].apply(lambda x: safeserielookup(genuslengths, x))
df['group_length'] = df['group'].apply(lambda x: safeserielookup(grouplengths, x))
df['order_length'] = df['order'].apply(lambda x: safeserielookup(orderlengths, x))
df['family_length'] = df['family'].apply(lambda x: safeserielookup(familylengths, x))

#df_sorted = df.sort_values(by=['order_length','family_length','name'])
df_sorted = df.sort_values(by=['order_length', 'family_length', 'group_length', 'name'])


pageinit = '\\begin{center}\n \\begin{tikzpicture}[>=latex]\n'
pageend = '  \\otherborders\n \\end{tikzpicture}\n\\end{center}\n\\newpage\n\n'

# TODO:
# Open woodland -> add a newline
# Get the right aspect ratio for art pictures

with open('allaboutbirds/allaboutbirds_booklet_aux.tex', 'w') as writer:
    writer.write(pageinit)
    pos = 0
    for index, row in df_sorted.iterrows():
        if(pos == 7):
            writer.write(pageend)
            writer.write(pageinit)
            pos = 0
        # column position
        writer.write('  \\begin{{scope}}[shift={{(3.99*{},0)}}]\n   \\leftborder\n'.format(pos))
        # images
        for i in range(3):
            imgfile = birdimgfile(row['sciname'], row['selected_imgs'][i])
            text = row['selected_imgs_text'][i]
            writer.write('   \\drawpicture{{0}}{{-1.15*{}*\\imgsize}}{{{}}}{{{}}}\n'.format(i, imgfile, text))
        # art img
        (height, width, _) = mpimg.imread('allaboutbirds/pictures/'+row['sciname'].replace(' ', '-')+'_art.jpg').shape
        maxheight = 2.7
        maxwidth = 3.8
        sizestr = ''
        if(maxheight >= maxwidth*height/width):
            sizestr = 'width='+str(maxwidth)
        else:
            sizestr = 'height='+str(maxheight)
        imgfile = 'pictures/'+row['sciname'].replace(' ', '-')+'_art.jpg'
        writer.write('   \\node[inner sep=0pt] () at (0,-9.7) {{\\includegraphics[{}cm]{{{}}}}};\n'.format(sizestr,imgfile))
        #writer.write('   \\drawart{{0}}{{-1.18*2.80*\\imgsize}}{{{}}}\n'.format(imgfile))
        # name and url
        names = row['name'].split(',')
        name = ',\\\\'.join(names)
        writer.write('   \\birdname{{{}}}{{{}}}{{{}}}\n'.format(name, row['sciname'], row['url']))
        # extra info
        writer.write('   \\begin{scope}[shift={(-1.3,-1-4.4*\\imgsize)}]\n')
        yoffs = [0, -1.15, -2.3, -3.45, -4.6]
        for i, (header, text) in enumerate(zip(row['mini_info_headers'],
                                               row['mini_info_text'])):
            imgfile = 'pictures/'+row['sciname'].replace(' ', '-')+'_{}_icon.png'.format(header)
            writer.write('     \\icontext{{0}}{{{}*\iconsize}}{{{}:}}{{{}}}\n'.format(yoffs[i], header, text))
            if(header == 'Conservation'):
                writer.write('     \\drawconsicon{{0}}{{{}*\iconsize}}{{\\iconsize}}{{{}}}{{{}}}\n'.format(yoffs[i], header.lower(), imgfile))
            else:
                writer.write('     \\drawicon{{0}}{{{}*\iconsize}}{{\\iconsize}}{{{}}}{{{}}}\n'.format(yoffs[i], header.lower(), imgfile))
        # ending
        writer.write('   \\end{scope}\n')
        writer.write('  \\end{scope}\n')
        pos = pos + 1 
    writer.write(pageend)
