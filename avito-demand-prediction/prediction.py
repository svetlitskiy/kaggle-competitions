import os
import zipfile
import csv
import pandas as pd


pathToData = '.kaggle/competitions/avito-demand-prediction'

files = dict(train=dict(data=os.path.join(os.path.expanduser('~'), pathToData, 'train.csv.zip'),
                        active=os.path.join(os.path.expanduser('~'), pathToData, 'train_active.csv.zip'),
                        jpg=os.path.join(os.path.expanduser('~'), pathToData, 'train_jpg.zip')))



#print(files)


#Read train.cvs
dataArchive = zipfile.ZipFile(files['train']['data'], 'r')
dataFile = dataArchive.open('train.csv')
reader = pd.read_csv(dataFile, chunksize=12)
for chunk in reader:
    chunk.columns = ['item_id', 'user_id', 'region', 'city', 'parent_category_name', 'category_name', 'param_1',
                     'param_2', 'param_3', 'title', 'description', 'price', 'item_seq_number', 'activation_date',
                     'user_type', 'image', 'image_top_1', 'deal_probability']
    print (chunk['deal_probability'])
