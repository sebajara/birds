# Overview

The [Rock Creek Park](https://www.nps.gov/rocr/) gives a very useful
[bird
checklist](https://www.nps.gov/rocr/learn/nature/upload/birdchecklist.pdf)
for us beginners, but the content is not very well organized. I remade
their table using color and shape coding, and all fit into one
page.

To help bird identification, I made scripts for scrapping the
 [Audubon](https://www.audubon.org) and
 [Allaboutbirds](https://www.allaboutbirds.org/) sites, and organize
 their bird photographs into a booklet. I hope not to be violating any
 copywrite issues by publishing here the final pdf. In case I do, please
 let me know and I will remove the final product.

## Rock Creek Park bird checklist

The table is made in Latex using [Tikz](Http://Www.Texample.Net/Tikz/Examples/) and a few macros. A python script
converts the raw table into Latex. The original table made by the
National Park Service can be found here: [original-table](https://www.nps.gov/rocr/learn/nature/upload/birdchecklist.pdf).

![](RockCreekPark/Birds_RockCreekPark_example.png)

### Instructions:
* The list of birds as well their regular sighing seasons are saved in an Open Office table: [Birds_RockCreekPark.ods](RockCreekPark/Birds_RockCreekPark.ods)
* The table is converted into LaTex using a python script [Birds_RockCreekPark_toLatex.py](RockCreekPark/Birds_RockCreekPark_toLatex.py)
* Then the content was arranged manually into columns tables inside another LaTex document [Birds_RockCreekPark.tex](RockCreekPark/Birds_RockCreekPark.tex)
* Compile (e.g. using pdflatex). See [Birds_RockCreekPark.pdf](RockCreekPark/Birds_RockCreekPark.pdf)

## Rock Creek Park Identification Guide

I took all the birds in the Rock Creek Park bird checklist, and scrapped
their related content in the [Audubon](https://www.audubon.org) and
[Allaboutbirds](https://www.allaboutbirds.org/) sites,
and downloaded the pictures they contain to generate a identification
guide. Here is one example page:

![](RockCreekPark/allaboutbirds/allaboutbirds_booklet-2.png)

### Instructions:
* Scrap and download the content from the Audubon site using
  [Audubon_scrap.py](RockCreekPark/audubon/Audubon_scrap.py). For now I
  am using only the drawings they generate, but the script downloads way
  more data than that.
* Scrap and download the content from the Allaboutbirds site using
  [Allaboutbirds_scrap.py](RockCreekPark/allaboutbirds/Allaboutbirds_scrap.py). Allaboutbirds
  search engine doesn't work well unless the bird name query is very
  close to what they have, so I had to manually modify some name names
  in the table (see [Birds_RockCreekPark.ods](RockCreekPark/allaboutbirds/Birds_RockCreekPark.ods).
* Manually select which picture we want to use for the identification
  guide. The maximum number is 3. Examples of how to select and final
  selection is in: [Allaboutbirds_select.py](RockCreekPark/allaboutbirds/Allaboutbirds_select.py).
* Convert content to Latex [Tikz](Http://Www.Texample.Net/Tikz/Examples/) commands using
  [Allaboutbirds_toLatex.py](RockCreekPark/allaboutbirds/Allaboutbirds_toLatex.py). Here
  I order birds based on their classification, and classifications
  sorted by average body weight.
* Compile file
  [allaboutbirds_booklet.tex](RockCreekPark/allaboutbirds/allaboutbirds_booklet.tex)
  into a pdf. **NOTE:** by mistake I am adding the ouside frame with
  default widht, so the last page has two empty extra white
  columns. Need to fix this.
* The full pdf is in: [allaboutbirds_booklet.pdf](RockCreekPark/allaboutbirds/allaboutbirds_booklet.pdf)
