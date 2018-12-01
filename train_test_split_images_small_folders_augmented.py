import numpy as np
import os
from random import shuffle
from math import floor
from shutil import copyfile


folder = '/home/jf/Documents/estudio/xrays/split_in_folders/some_augmented_299/'
basefolders = os.listdir(folder)
basefolders.sort()

types = ['no_finding', 'infiltration', 'atelectasis', 'effusion', 'nodule', 'pneumothorax', 'mass', 'consolidation', 'cardiomegaly']

type_folders = []

for type in types:
    type_folders.append(folder+type)

for type_folder in type_folders:
    images = os.listdir(type_folder)
    shuffle(images)
    if 'no_finding' in type_folder:
        images = images[:10000]
    print(type_folder)
    print(images[0])
    print(len(images))



    base_train = floor(len(images)*.80)
    n_test = len(images)-base_train
    n_train = floor(base_train*.80)
    n_val = base_train - n_train

    train = images[:n_train]
    val = images[n_train:n_train + n_val]
    test = images[n_train + n_val:]
    print(len(train), len(val), len(test))


    label = type_folder[69:]
    counter = 0
    for img in train:
        base = '/home/jf/Documents/estudio/xrays/split_in_folders/some_augmented_299/' + label + '/'
        target = '/home/jf/Documents/estudio/xrays/split_in_folders/299_small_aug/train/' + label + '/'
        base = base + img
        target = target + img
        print(base, target)
        copyfile(base, target)
        counter +=1
        print(counter)

    counter = 0
    for img in val:
        base = '/home/jf/Documents/estudio/xrays/split_in_folders/some_augmented_299/' + label + '/'
        target = '/home/jf/Documents/estudio/xrays/split_in_folders/299_small_aug/val/' + label + '/'
        base = base + img
        target = target + img
        print(base, target)
        copyfile(base, target)
        counter +=1
        print(counter)

    counter = 0
    for img in test:
        base = '/home/jf/Documents/estudio/xrays/split_in_folders/some_augmented_299/' + label + '/'
        target = '/home/jf/Documents/estudio/xrays/split_in_folders/299_small_aug/test/' + label + '/'
        base = base + img
        target = target + img
        print(base, target)
        copyfile(base, target)
        counter +=1
        print(counter)
