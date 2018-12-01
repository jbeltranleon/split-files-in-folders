
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


images = pd.read_csv('../../Data_Entry_2017.csv',encoding='utf-8')


# In[ ]:


images.head()


# In[ ]:


images.dtypes


# In[ ]:


cols = ['Image Index', 'Finding Labels']


# In[ ]:


images = images[cols]


# In[ ]:


images.head()


# In[ ]:


labels_counts = images['Finding Labels'].value_counts()


# In[ ]:


labels = images['Finding Labels'].unique()


# In[ ]:


useless = 0
for label in labels:
    if("|" in label):
        useless += 1
    else:
        print(label.lower())


# In[ ]:


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


# In[ ]:


print(pneumonia.count())


# In[ ]:


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


# In[ ]:


import os


# In[ ]:


from shutil import copyfile
from sys import exit


# In[ ]:


os.makedirs('cardiomegaly', exist_ok=True)
os.makedirs('no_finding', exist_ok=True)
os.makedirs('hernia', exist_ok=True)
os.makedirs('infiltration', exist_ok=True)
os.makedirs('nodule', exist_ok=True)
os.makedirs('emphysema', exist_ok=True)
os.makedirs('effusion', exist_ok=True)
os.makedirs('atelectasis', exist_ok=True)
os.makedirs('pleural_thickening', exist_ok=True)
os.makedirs('pneumothorax', exist_ok=True)
os.makedirs('mass', exist_ok=True)
os.makedirs('fibrosis', exist_ok=True)
os.makedirs('consolidation', exist_ok=True)
os.makedirs('edema', exist_ok=True)
os.makedirs('pneumonia', exist_ok=True)


# In[ ]:


for img in pneumonia_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/pneumonia/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in cardiomegaly_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/cardiomegaly/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in no_finding_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/no_finding/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[2]:


for img in hernia_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/hernia/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in infiltration_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/infiltration/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in nodule_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/nodule/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in emphysema_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/emphysema/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in effusion_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/effusion/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in atelectasis_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/atelectasis/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in pleural_thickening_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/pleural_thickening/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in pneumothorax_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/pneumothorax/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in mass_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/mass/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in fibrosis_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/fibrosis/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in consolidation_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/consolidation/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)


# In[ ]:


for img in edema_img:
    base = '/home/jf/Documents/estudio/xrays/299/images/'
    target = os.getcwd() + '/edema/'
    base = base + img
    target = target + img
    print(base, target)
    copyfile(base, target)
