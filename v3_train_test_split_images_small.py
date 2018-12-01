import numpy as np
import pandas as pd

images = pd.read_csv('../Data_Entry_2017.csv',encoding='utf-8')

cols = ['Image Index', 'Finding Labels']

images = images[cols]

cardiomegaly = images.loc[images['Finding Labels'] == 'Cardiomegaly']
no_finding = images.loc[images['Finding Labels'] == 'No Finding']
hernia = images.loc[images['Finding Labels'] == 'Hernia']
infiltration = images.loc[images['Finding Labels'] == 'Infiltration']
nodule = images.loc[images['Finding Labels'] == 'Nodule']
emphysema = images.loc[images['Finding Labels'] == 'Emphysema']
effusion = images.loc[images['Finding Labels'] == 'Effusion']
atelectasis = images.loc[images['Finding Labels'] == 'Atelectasis']
pleural_thickening = images.loc[images['Finding Labels'] == 'Pleural_Thickening']
pneumothorax = images.loc[images['Finding Labels'] == 'Pneumothorax']
mass = images.loc[images['Finding Labels'] == 'Mass']
fibrosis = images.loc[images['Finding Labels'] == 'Fibrosis']
consolidation = images.loc[images['Finding Labels'] == 'Consolidation']
edema = images.loc[images['Finding Labels'] == 'Edema']
pneumonia = images.loc[images['Finding Labels'] == 'Pneumonia']

cardiomegaly_img = cardiomegaly['Image Index'].values
no_finding_img = no_finding['Image Index'].values
hernia_img = hernia['Image Index'].values
infiltration_img = infiltration['Image Index'].values
nodule_img = nodule['Image Index'].values
emphysema_img = emphysema['Image Index'].values
effusion_img = effusion['Image Index'].values
atelectasis_img = atelectasis['Image Index'].values
pleural_thickening_img = pleural_thickening['Image Index'].values
pneumothorax_img = pneumothorax['Image Index'].values
mass_img = mass['Image Index'].values
fibrosis_img = fibrosis['Image Index'].values
consolidation_img = consolidation['Image Index'].values
edema_img = edema['Image Index'].values
pneumonia_img = pneumonia['Image Index'].values

print(cardiomegaly_img)


labels = [
            [cardiomegaly, cardiomegaly_img, 'cardiomegaly'],
            [no_finding, no_finding_img, 'no_finding'],
            [hernia, hernia_img, 'hernia'],
            [infiltration, infiltration_img, 'infiltration'],
            [nodule, nodule_img, 'nodule'],
            [emphysema, emphysema_img, 'emphysema'],
            [effusion, effusion_img, 'effusion'],
            [atelectasis, atelectasis_img, 'atelectasis'],
            [pleural_thickening, pleural_thickening_img, 'pleural_thickening'],
            [pneumothorax, pneumothorax_img, 'pneumothorax'],
            [mass, mass_img, 'mass'],
            [fibrosis, fibrosis_img, 'fibrosis'],
            [consolidation, consolidation_img, 'consolidation'],
            [edema, edema_img, 'edema'],
            [pneumonia, pneumonia_img, 'pneumonia']
        ]


from random import shuffle
from math import floor


from shutil import copyfile


preferred = ['no_finding', 'infiltration', 'atelectasis', 'effusion']

for label in labels:
    if(label[2] in preferred):
        if(label[2]=='no_finding'):
            label[0]=label[0][:20000]
            label[1]=label[1][:20000]

        print(label[1])
        shuffle(label[1])
        print(label[1])

        n_train = floor(len(label[0])*.64)
        n_val = floor(len(label[0])*.16)
        n_test = len(label[0]) - (n_train + n_val)

        print(n_train, n_val, n_test)

        train = label[1][:n_train]
        val = label[1][n_train:n_train + n_val]
        test = label[1][n_train + n_val:]
        print(len(train), len(val), len(test)) 

        counter = 0

        for img in train:
            base = '/home/jf/Documents/estudio/xrays/split_in_folders/224/' + label[2] + '/'
            target = '/home/jf/Documents/estudio/xrays/split_in_folders/224ML/train/' + label[2] + '/'
            base = base + img
            target = target + img
            print(base[49:], target[49:])
            copyfile(base, target)
            counter +=1
            print("==> {}".format(counter))

        counter = 0
        for img in val:
            base = '/home/jf/Documents/estudio/xrays/split_in_folders/224/' + label[2] + '/'
            target = '/home/jf/Documents/estudio/xrays/split_in_folders/224ML/val/' + label[2] + '/'
            base = base + img
            target = target + img
            print(base[49:], target[49:])
            copyfile(base, target)
            counter +=1
            print("==> {}".format(counter))

        counter = 0
        for img in test:
            base = '/home/jf/Documents/estudio/xrays/split_in_folders/224/' + label[2] + '/'
            target = '/home/jf/Documents/estudio/xrays/split_in_folders/224ML/test/' + label[2] + '/'
            base = base + img
            target = target + img
            print(base[49:], target[49:])
            copyfile(base, target)
            counter +=1
            print("==> {}".format(counter))
