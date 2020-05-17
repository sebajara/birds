import pandas as pd
import ezodf

# read_ods taken from:
# https://stackoverflow.com/questions/17834995/how-to-convert-opendocument-spreadsheets-to-a-pandas-dataframe
def read_ods(filename, sheet_no=0, header=0):
    tab = ezodf.opendoc(filename=filename).sheets[sheet_no]
    return pd.DataFrame({col[header].value:[x.value for x in col[header+1:]]
                         for col in tab.columns()})

df = read_ods(filename='list.ods')

monthskeys = {'?':  0,
              'c':  1,
              'cs': 2,
              'u':  3,
              'us': 4,
              'r':  5,
              'rs': 6,
              None: 7}

monthcolums = ['January', 'February', 'March',
               'April', 'May', 'June',
               'July', 'August', 'September',
               'October', 'November', 'December']


with open('Birds_RockCreekPark_LatexCommands.tex', 'w') as writer:
    for i, values in df.iterrows():
        name = values['Name']
        names = name.split(' ')
        name2 = names[-1] + ", " + " ".join(names[:-1])
        months_list = [str(monthskeys[val]) for val in values[monthcolums].values]
        print_str = "\\drawbirdbox{{0}}{{-{} * \\rowheight}}{{{}}}{{{{{}}}}}".format(str(i),name2,
                                                                                     ",".join(months_list))
        writer.write(print_str+';\n')
    
