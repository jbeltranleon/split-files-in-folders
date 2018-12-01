
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


images = pd.read_csv('../Data_Entry_2017.csv',encoding='utf-8')


# In[3]:


cols = ['Image Index', 'Finding Labels']


# In[4]:


images = images[cols]


# In[5]:


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


# In[6]:


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


# In[7]:


print(cardiomegaly_img)


# In[8]:


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


# In[10]:
from random import shuffle
from math import floor

shuffle(cardiomegaly_img)
print(cardiomegaly_img)

base_train = floor(len(cardiomegaly)*.80)
n_test = len(cardiomegaly_img)-base_train
n_train = floor(base_train*.80)
n_val = base_train - n_train

train = cardiomegaly_img[:n_train]
val = cardiomegaly_img[n_train:n_train + n_val]
test = cardiomegaly_img[n_train + n_val:]


# In[11]:


print(len(train), len(val), len(test))


# In[12]:


print(train[0], train[698])
print(val[0], val[174])
print(test[0], test[217])


# In[20]:

from shutil import copyfile

for label in labels:
    if(label[2]=='no_finding'):
        label[0]=label[0][:10000]
        label[1]=label[1][:10000]

    print(label[1])
    shuffle(label[1])
    print(label[1])
    base_train = floor(len(label[0])*.80)
    n_test = len(label[1])-base_train
    n_train = floor(base_train*.80)
    n_val = base_train - n_train

    train = label[1][:n_train]
    val = label[1][n_train:n_train + n_val]
    test = label[1][n_train + n_val:]
    print(len(train), len(val), len(test))

    for img in train:
        base = '/home/jf/Documents/estudio/xrays/split_in_folders/299/' + label[2] + '/'
        target = '/home/jf/Documents/estudio/xrays/split_in_folders/299_less_no/train/' + label[2] + '/'
        base = base + img
        target = target + img
        print(base, target)
        copyfile(base, target)

    for img in val:
        base = '/home/jf/Documents/estudio/xrays/split_in_folders/299/' + label[2] + '/'
        target = '/home/jf/Documents/estudio/xrays/split_in_folders/299_less_no/val/' + label[2] + '/'
        base = base + img
        target = target + img
        print(base, target)
        copyfile(base, target)

    for img in test:
        base = '/home/jf/Documents/estudio/xrays/split_in_folders/299/' + label[2] + '/'
        target = '/home/jf/Documents/estudio/xrays/split_in_folders/299_less_no/test/' + label[2] + '/'
        base = base + img
        target = target + img
        print(base, target)
        copyfile(base, target)
