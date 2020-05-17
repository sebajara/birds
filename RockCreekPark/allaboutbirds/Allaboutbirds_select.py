import ezodf
import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os.path

def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})


def birdimgfile(birddic, index):
    prefix = birddic["scientific-name"].replace(' ', '-')
    imgfolder = 'allaboutbirds/pictures/'
    return '{}{}_{}.jpg'.format(imgfolder, prefix, index)


def myplotimg(ax, img, title):
    ax.imshow(img, cmap=plt.cm.gray)
    ax.set_title(title, fontsize=16)
    ax.axis('off')


# To go in order
df = read_ods(filename='Birds_RockCreekPark.ods')
birdnamelist = df.iloc[:, 0].values

with open('allaboutbirds/Allaboutbirds_RockCreekPark_json.txt') as json_file:
    birddata = json.load(json_file)


def plotbirdimgs(birdname):
    fig, axes = plt.subplots(ncols=4, nrows=4,
                         figsize=(18, 10))
    axlist = axes.flatten()
    for i in range(0, 16):
        filepath = birdimgfile(birddata[birdname], i)
        if(os.path.isfile(filepath)):
            img = mpimg.imread(filepath)
            print('{}. {}'.format(i, birddata[birdname]['imgs_text'][i]))
            myplotimg(axlist[i], img, '{}.'.format(i))
            plt.imshow(img)
        else:
            myplotimg(axlist[i], np.array([[0,0],[0,0]]), '')
            plt.tight_layout()
    plt.show()

    
# Used this to select images one by one
# plotbirdimgs(birdnamelist[0])
# ...
# plotbirdimgs(birdnamelist[137])

birddata[birdnamelist[0]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[0]]["Selected_text"] = ['Breeding Male', 'Female', 'Nonbreeding Male']
birddata[birdnamelist[1]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[1]]["Selected_text"] = ['Breeding Male', 'Female', 'Nonbreeding Male']
birddata[birdnamelist[2]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[2]]["Selected_text"] = ['Male', 'Female', 'Juvenile']
birddata[birdnamelist[3]]["Selected"] = [0, 1, 6]
birddata[birdnamelist[3]]["Selected_text"] = ['Male', 'Female/Nonbreeding', 'Female/Nonbreeding']
birddata[birdnamelist[4]]["Selected"] = [0, 3, 6]
birddata[birdnamelist[4]]["Selected_text"] = ['Male', 'Male (Masked)', 'Female']
birddata[birdnamelist[5]]["Selected"] = [0, 1, 4]
birddata[birdnamelist[5]]["Selected_text"] = ['Male', 'Female', 'Immature Male']
birddata[birdnamelist[6]]["Selected"] = [0, 1, 7] # could be also 3
birddata[birdnamelist[6]]["Selected_text"] = ['Breeding Male', 'Female/Immature', 'Nonbreeding Male']
birddata[birdnamelist[7]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[7]]["Selected_text"] = ['Male', 'Female', 'Juvenile']
birddata[birdnamelist[8]]["Selected"] = [0, 3, 7]
birddata[birdnamelist[8]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[9]]["Selected"] = [0, 3, 7]
birddata[birdnamelist[9]]["Selected_text"] = ['Adult', 'Adult', 'Habitat']
birddata[birdnamelist[10]]["Selected"] = [0, 1, 2]
birddata[birdnamelist[10]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[11]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[11]]["Selected_text"] = ['Male', 'Female', 'Juvenile']
birddata[birdnamelist[12]]["Selected"] = [0, 1, 4]
birddata[birdnamelist[12]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[13]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[13]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[14]]["Selected"] = [0, 1, 2]
birddata[birdnamelist[14]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[15]]["Selected"] = [0, 1, 4]
birddata[birdnamelist[15]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[16]]["Selected"] = [0, 1, 4]
birddata[birdnamelist[16]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[17]]["Selected"] = [0, 1, 7]
birddata[birdnamelist[17]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[18]]["Selected"] = [0, 1, 4]
birddata[birdnamelist[18]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[19]]["Selected"] = [0, 1, 3]
birddata[birdnamelist[19]]["Selected_text"] = ['Male', 'Female', 'Eclipse Male']
birddata[birdnamelist[20]]["Selected"] = [6, 0, 1] # also 4 is nice
birddata[birdnamelist[20]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[21]]["Selected"] = [0, 3, 1] # 
birddata[birdnamelist[21]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[22]]["Selected"] = [0, 1, 9] # 
birddata[birdnamelist[22]]["Selected_text"] = ['Adult male', 'Female/Immature', 'Female/Immature']
birddata[birdnamelist[23]]["Selected"] = [0, 4, 1] # 
birddata[birdnamelist[23]]["Selected_text"] = ['Adult male', 'Adult male', 'Female/immature']
birddata[birdnamelist[24]]["Selected"] = [0, 6, 11] # 
birddata[birdnamelist[24]]["Selected_text"] = ['Male (Yellow-shafted)', 'Female (Yellow-shafted)', 'Male (Red-shafted)']
birddata[birdnamelist[25]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[25]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[26]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[26]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[27]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[27]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[28]]["Selected"] = [0, 1, 6] #
birddata[birdnamelist[28]]["Selected_text"] = ['Breeding Male', 'Female/Nonbreeding', 'Female/Nonbreeding']
birddata[birdnamelist[29]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[29]]["Selected_text"] = ['Breeding Male', 'Nonbreeding Male', 'Female/Immature Male']
birddata[birdnamelist[30]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[30]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[31]]["Selected"] = [0, 1, 5] #
birddata[birdnamelist[31]]["Selected_text"] = ['Adult Male', 'Female', 'Immature']
birddata[birdnamelist[32]]["Selected"] = [0, 3, 1] #
birddata[birdnamelist[32]]["Selected_text"] = ['Breeding Male', 'Nonbreeding Male', 'Female/Immature Male']
birddata[birdnamelist[33]]["Selected"] = [0, 4, 7] #
birddata[birdnamelist[33]]["Selected_text"] = ['Adult Male', 'Female/Immature Male', 'Flock']
birddata[birdnamelist[34]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[34]]["Selected_text"] = ['Adult Male', 'Female', 'Immature Male']
birddata[birdnamelist[35]]["Selected"] = [0, 1, 9] #
birddata[birdnamelist[35]]["Selected_text"] = ['Breeding Adult', 'Nonbreeding Adult', 'Juvenile']
birddata[birdnamelist[36]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[36]]["Selected_text"] = ['Breeding Adult', 'Nonbreeding Adult', 'Juvenile']
birddata[birdnamelist[37]]["Selected"] = [0, 1, 5] #
birddata[birdnamelist[37]]["Selected_text"] = ['Breeding Adult', 'Nonbreeding Adult', 'Juvenile']
birddata[birdnamelist[38]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[38]]["Selected_text"] = ['Adult light morph', 'Adult light morph', 'Adult light morph']
birddata[birdnamelist[39]]["Selected"] = [12, 0, 10] #
birddata[birdnamelist[39]]["Selected_text"] = ['Adult', 'Adult', 'Immature']
birddata[birdnamelist[40]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[40]]["Selected_text"] = ['Adult', 'Adult', 'Immature']
birddata[birdnamelist[41]]["Selected"] = [0, 1, 15] #
birddata[birdnamelist[41]]["Selected_text"] = ['Adult (borealis)', 'Adult (light morph)', 'Adult (borealis)']
birddata[birdnamelist[42]]["Selected"] = [0, 4, 1] #
birddata[birdnamelist[42]]["Selected_text"] = ['Adult', 'Adult', 'Immature']
birddata[birdnamelist[43]]["Selected"] = [0, 4, 3] #
birddata[birdnamelist[43]]["Selected_text"] = ['Adult', 'Adult', 'Immature']
birddata[birdnamelist[44]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[44]]["Selected_text"] = ['Adult (blue)', 'Adult (blue)', 'Adult (white)']
birddata[birdnamelist[45]]["Selected"] = [0, 7, 1] #
birddata[birdnamelist[45]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[46]]["Selected"] = [0, 4, 3] #
birddata[birdnamelist[46]]["Selected_text"] = ['Adult Male', 'Adult Male', 'Female']
birddata[birdnamelist[47]]["Selected"] = [0, 1, 6] #
birddata[birdnamelist[47]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[48]]["Selected"] = [0, 10, 1] #
birddata[birdnamelist[48]]["Selected_text"] = ['Adult Male (Slate-colored)', 'Female/Immature (Slate-colored)', 'Adult male (Oregon)']
birddata[birdnamelist[49]]["Selected"] = [3, 0, 1] #
birddata[birdnamelist[49]]["Selected_text"] = ['Adult Male', 'Adult Male', 'Female']
birddata[birdnamelist[50]]["Selected"] = [0, 5, 1] #
birddata[birdnamelist[50]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[51]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[51]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[52]]["Selected"] = [0, 1, 5] #
birddata[birdnamelist[52]]["Selected_text"] = ['Female', 'Male', 'Female']
birddata[birdnamelist[53]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[53]]["Selected_text"] = ['Adult', 'Adult Male', 'Juvenile']
birddata[birdnamelist[54]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[54]]["Selected_text"] = ['Adult', 'Adult Male', 'Adult']
birddata[birdnamelist[55]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[55]]["Selected_text"] = ['Breeding', 'Nonbreeding/Immature', 'Nonbreeding/Immature']
birddata[birdnamelist[56]]["Selected"] = [2, 3, 4] #
birddata[birdnamelist[56]]["Selected_text"] = ['Breeding Male', 'Female', 'Nonbreeding Male and Female']
birddata[birdnamelist[57]]["Selected"] = [0, 3, 6] #
birddata[birdnamelist[57]]["Selected_text"] = ['Adult Male', 'Adult Male', 'Female/Immature Male']
birddata[birdnamelist[58]]["Selected"] = [0, 6, 1] #
birddata[birdnamelist[58]]["Selected_text"] = ['Breeding', 'Breeding', 'Nonbreeding']
birddata[birdnamelist[59]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[59]]["Selected_text"] = ['Male', 'Female/Immature Male', 'Male and Female']
birddata[birdnamelist[60]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[60]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[61]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[61]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[62]]["Selected"] = [0, 3, 1] #
birddata[birdnamelist[62]]["Selected_text"] = ['Adult', 'Adult', 'Female']
birddata[birdnamelist[63]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[63]]["Selected_text"] = ['Adult', 'Adult Female', 'Adult Male']
birddata[birdnamelist[64]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[64]]["Selected_text"] = ['Adult Male', 'Adult Female', 'Immature Male']
birddata[birdnamelist[65]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[65]]["Selected_text"] = ['Adult Male', 'Female', 'Immature Male']
birddata[birdnamelist[66]]["Selected"] = [0, 6, 3] #
birddata[birdnamelist[66]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[67]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[67]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[68]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[68]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[69]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[69]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[70]]["Selected"] = [0, 1, 6] #
birddata[birdnamelist[70]]["Selected_text"] = ['Adult (gray morph)', 'Adult (red morph)', 'Juvenile']
birddata[birdnamelist[71]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[71]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[72]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[72]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[73]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[73]]["Selected_text"] = ['Adult Male', 'Female', 'Immature Male']
birddata[birdnamelist[74]]["Selected"] = [0, 4, 9] #
birddata[birdnamelist[74]]["Selected_text"] = ['Adult Male', 'Female/Immature Male', 'Juvenile']
birddata[birdnamelist[75]]["Selected"] = [0, 3, 1] #
birddata[birdnamelist[75]]["Selected_text"] = ['Breeding', 'Breeding', 'Nonbreeding']
birddata[birdnamelist[76]]["Selected"] = [0, 3, 5] #
birddata[birdnamelist[76]]["Selected_text"] = ['Breeding', 'Breeding', 'Nonbreeding']
birddata[birdnamelist[77]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[77]]["Selected_text"] = ['Male', 'Female', 'Juvenile']
birddata[birdnamelist[78]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[78]]["Selected_text"] = ['Adult', 'Adult Male', 'Juvenile']
birddata[birdnamelist[79]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[79]]["Selected_text"] = ['Breeding', 'Nonbreeding', 'Juvenile']
birddata[birdnamelist[80]]["Selected"] = [0, 3, 1] #
birddata[birdnamelist[80]]["Selected_text"] = ['Breeding Male', 'Nonbreeding Male', 'Female']
birddata[birdnamelist[81]]["Selected"] = [4, 1, 3] #
birddata[birdnamelist[81]]["Selected_text"] = ['Adult', 'Adult', 'Juvenile']
birddata[birdnamelist[82]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[82]]["Selected_text"] = ['Adult (Red)', 'Adult (Sooty)', 'Adult (Thick-billed)']
birddata[birdnamelist[83]]["Selected"] = [0, 2, 12] #
birddata[birdnamelist[83]]["Selected_text"] = ['Adult (Eastern)', 'Adult (Eastern)', 'Habitat']
birddata[birdnamelist[84]]["Selected"] = [0, 5, 3] #
birddata[birdnamelist[84]]["Selected_text"] = ['Adult', 'Nonbreeding/Immature', 'Adult']
birddata[birdnamelist[85]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[85]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[86]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[86]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[87]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[87]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[88]]["Selected"] = [0, 6, 4] #
birddata[birdnamelist[88]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[89]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[89]]["Selected_text"] = ['Adult (Olive-backed)', 'Adult (Russet-backed)', 'Adult (Olive-backed)']
birddata[birdnamelist[90]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[90]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[91]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[91]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[92]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[92]]["Selected_text"] = ['Adult Male', 'Female/Immature', 'Adult Male (white-eyed)']
birddata[birdnamelist[93]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[93]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[94]]["Selected"] = [0, 4, 2] #
birddata[birdnamelist[94]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[95]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[95]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[96]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[96]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[97]]["Selected"] = [0, 1, 5] #
birddata[birdnamelist[97]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[98]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[98]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[99]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[99]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[100]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[100]]["Selected_text"] = ['Adult', 'Adult', 'Immature']
birddata[birdnamelist[101]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[101]]["Selected_text"] = ['Breeding Male', 'Breeding Female', 'Nonbreeding Female/Immature Male']
birddata[birdnamelist[102]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[102]]["Selected_text"] = ['Adult Male', 'Female/Immature Male', 'Female/Immature Male']
birddata[birdnamelist[103]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[103]]["Selected_text"] = ['Breeding Male', 'Breeding Female', 'Nonbreeding Female/Immature']
birddata[birdnamelist[104]]["Selected"] = [0, 1, 2] #
birddata[birdnamelist[104]]["Selected_text"] = ['Male', 'Female', 'Male']
birddata[birdnamelist[105]]["Selected"] = [0, 1, 6] #
birddata[birdnamelist[105]]["Selected_text"] = ['Adult Male', 'Adult Female', 'Female/Immature']
birddata[birdnamelist[106]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[106]]["Selected_text"] = ['Adult Male', 'Adult Female', 'Immature female']
birddata[birdnamelist[107]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[107]]["Selected_text"] = ['Adult Male', 'Adult Female', 'Adult Male']
birddata[birdnamelist[108]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[108]]["Selected_text"] = ['Adult Male', 'Adult Female/Immature Male', 'Immature Female']
birddata[birdnamelist[109]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[109]]["Selected_text"] = ['Adult Male', 'Adult Female/Immature Male', 'Immature Female']
birddata[birdnamelist[110]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[110]]["Selected_text"] = ['Breeding Male', 'Breeding Female', 'Nonbreeding Female/Immature Male']
birddata[birdnamelist[111]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[111]]["Selected_text"] = ['Male', 'Female', 'Male']
birddata[birdnamelist[112]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[112]]["Selected_text"] = ['Adult Male', 'Female/Immature Male', 'Adult Female']
birddata[birdnamelist[113]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[113]]["Selected_text"] = ['Adult Male', 'Adult Female/Immature Male', 'Immature male']
birddata[birdnamelist[114]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[114]]["Selected_text"] = ['Adult Male', 'Female/Immature', 'Female/Immature']
birddata[birdnamelist[115]]["Selected"] = [0, 3, 1] #
birddata[birdnamelist[115]]["Selected_text"] = ['Breeding Adult (Yellow)', 'Nonbreeding/Immature (Yellow)', 'Breeding Adult (Western)']
birddata[birdnamelist[116]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[116]]["Selected_text"] = ['Adult Male', 'Immature Male', 'Immature Female']
birddata[birdnamelist[117]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[117]]["Selected_text"] = ['Adult Male', 'Adult Female', 'Immature Female']
birddata[birdnamelist[118]]["Selected"] = [0, 3, 4] #
birddata[birdnamelist[118]]["Selected_text"] = ['Adult Male', 'Female/Immature', 'Adult Male']
birddata[birdnamelist[119]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[119]]["Selected_text"] = ['Adult Male', 'Adult Female', 'Adult Male']
birddata[birdnamelist[120]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[120]]["Selected_text"] = ['Breeding Male', 'Breeding Female', 'Immature']
birddata[birdnamelist[121]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[121]]["Selected_text"] = ['Adult Male', 'Female/Immature', 'Female/Immature']
birddata[birdnamelist[122]]["Selected"] = [0, 6, 10] #
birddata[birdnamelist[122]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[123]]["Selected"] = [0, 1, 5] #
birddata[birdnamelist[123]]["Selected_text"] = ['Adult Male (Northern)', 'Adult Female (Northern)', 'Immature (Northern)']
birddata[birdnamelist[124]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[124]]["Selected_text"] = ['Adult male (Myrtle)', 'Adult male (Audubon\'s)', 'Female (Myrtle)']
birddata[birdnamelist[125]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[125]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[126]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[126]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[127]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[127]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[128]]["Selected"] = [0, 1, 8] #
birddata[birdnamelist[128]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[129]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[129]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[130]]["Selected"] = [0, 9, 6] #
birddata[birdnamelist[130]]["Selected_text"] = ['Male (Eastern)', 'Female (Eastern)', 'Juvenile']
birddata[birdnamelist[131]]["Selected"] = [1, 0, 6] #
birddata[birdnamelist[131]]["Selected_text"] = ['Male', 'Female', 'Juvenile']
birddata[birdnamelist[132]]["Selected"] = [0, 1, 4] #
birddata[birdnamelist[132]]["Selected_text"] = ['Male', 'Female', 'Male']
birddata[birdnamelist[133]]["Selected"] = [0, 1, 5] #
birddata[birdnamelist[133]]["Selected_text"] = ['Adult', 'Immature', 'Juvenile']
birddata[birdnamelist[134]]["Selected"] = [0, 1, 11] #
birddata[birdnamelist[134]]["Selected_text"] = ['Adult', 'Adult', 'Adult']
birddata[birdnamelist[135]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[135]]["Selected_text"] = ['Adult/immature (Northern)', 'Adult/immature (Brown-throated)', 'Adult/immature (Southern)']
birddata[birdnamelist[136]]["Selected"] = [0, 1, 3] #
birddata[birdnamelist[136]]["Selected_text"] = ['', '', '']
birddata[birdnamelist[137]]["Selected"] = [0, 9, 3] #
birddata[birdnamelist[137]]["Selected_text"] = ['Adult Male', 'Female', 'Immature Male']

with open('allaboutbirds/Allaboutbirds_RockCreekPark_Selected_json.txt', 'w') as outfile:
    json.dump(birddata, outfile)
