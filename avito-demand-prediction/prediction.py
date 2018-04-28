import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io
from PIL import Image



pathToData = '.kaggle/competitions/avito-demand-prediction'

files = dict(train=dict(data=os.path.join(os.path.expanduser('~'), pathToData, 'train.csv.zip'),
                        active=os.path.join(os.path.expanduser('~'), pathToData, 'train_active.csv.zip'),
                        jpg=dict(path=os.path.join(os.path.expanduser('~'), pathToData, 'train_jpg.zip'),
                                 index=None)),
             test=dict(data=os.path.join(os.path.expanduser('~'), pathToData, 'test.csv.zip'),
                       active=os.path.join(os.path.expanduser('~'), pathToData, 'test_active.csv.zip'),
                       jpg=dict(path=os.path.join(os.path.expanduser('~'), pathToData, 'test_jpg.zip'),
                                index=None)))
# init indexes
files['test']['jpg']['index'] = zipfile.ZipFile(files['test']['jpg']['path'], 'r')


#base functions
def read_csv_data(zipFile, pathInZipFile, has_probability=True, func=print, max_items=0):
    counter = 0
    columns = ['item_id', 'user_id', 'region', 'city', 'parent_category_name', 'category_name', 'param_1',
               'param_2', 'param_3', 'title', 'description', 'price', 'item_seq_number', 'activation_date',
               'user_type', 'image', 'image_top_1']
    if has_probability:
        columns.append('deal_probability')

    data_archive = zipfile.ZipFile(zipFile, 'r')
    data_file = data_archive.open(pathInZipFile)
    reader = pd.read_csv(data_file, chunksize=1000)
    for chunk in reader:
        if counter > 0 and counter >= max_items:
            break
        chunk.columns = columns
        for index, row in chunk.iterrows():
            if counter > 0 and counter >= max_items:
                break
            counter = counter+1
            #if row['deal_probability'] == 1.0:
            func(index, row)

#print(data_archive.namelist())


def read_img_data(zip_file, file_in_zipfile):
    archive_file = 'data/competition_files/test_jpg/'+file_in_zipfile+'.jpg'
    print(archive_file)
    archive = zip_file['index']
    #print(archive.namelist())
    data = archive.read(archive_file)
    data_enc = io.BytesIO(data)
    png_img = plt.imread(data_enc, format='jpg')
    plt.imshow(png_img)
    return 1



#jpgImg1 = read_img_data(files['test']['jpg'], '77c8a6d30596c3ad51874f7e04b9ba7b09cbf0d27d2e4fc8d4b7bcb418a9321b')
#plt.show()








#data/competition_files/test_jpg/77c8a6d30596c3ad51874f7e04b9ba7b09cbf0d27d2e4fc8d4b7bcb418a9321b.jpg
#data/competition_files/test_jpg/f78123832b29b81a61d3b13ad1ce50c3cdbf0b4c6036c9fa0f40045753dbcec5.jpg
#data/competition_files/test_jpg/130ff59ea64c2ce954cf26aa57568dc484d9e9d444626d057efd989c29cebe7e.jpg


#pl.figure(figsize=(10, 10))
#pl.show()

#pl.figure(figsize=(1.8 * n_col, 2.4 * n_row))


#user functions
def print_image(index, row):
    print(index, row['image'], row['parent_category_name'], row['category_name'])
    #print(row)
    if row['image']!='nan':
        read_img_data(files['test']['jpg'], row['image'])
        plt.show()


read_csv_data(files['test']['data'], 'test.csv', has_probability=False, func=print_image, max_items=4)















print('---------------------------')



#67a19a5bbe577828e958721fadd1a56d529838cc2bef6509f104fdcb8b7173a4 1291.0