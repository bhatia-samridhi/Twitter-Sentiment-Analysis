# -*- coding: utf-8 -*-


import pandas as pd

#import my csv files
happy = pd.read_csv('C:\\Users\\DELL\\Download/Happie_words.csv')
sad = pd.read_csv('C:\\Users\\DELL\\Download/Sad_words.csv')
unsmile = pd.read_csv('C:\\Users\\DELL\\Download/Unsmile_words.csv')
fun = pd.read_csv('C:\\Users\\DELL\\Download/Funny_words.csv')


wordbag = pd.concat([happy,sad,unsmile,fun]).drop_duplicates(subset = 'word').reset_index(drop=True)

print(wordbag)

wordbag.to_csv('C:\\Users\\DELL\\Download/Wordbag.csv')