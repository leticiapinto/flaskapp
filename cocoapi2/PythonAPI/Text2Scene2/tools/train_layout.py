#!/usr/bin/env python

import _init_paths
import os, sys, cv2, math
import random, json, logz
import numpy as np
import os.path as osp
from copy import deepcopy
import matplotlib.pyplot as plt
from glob import glob

from modules.layout_evaluator import *
from modules.layout_trainer import SupervisedTrainer
from datasets.layout_coco import layout_coco
from layout_utils import *
from layout_config import get_config


def train_model(config):    
    transformer = volume_normalize('background')
    train_db = layout_coco(config, split='train', transform=transformer)   
    val_db   = layout_coco(config, split='val',   transform=transformer) 
    test_db  = layout_coco(config, split='test',  transform=transformer)

    trainer = SupervisedTrainer(train_db)
    trainer.train(train_db, test_db, val_db)   


if __name__ == '__main__':
    cv2.setNumThreads(0)
    config, unparsed = get_config()
    config = layout_arguments(config)
    np.random.seed(config.seed)
    random.seed(config.seed)
    torch.manual_seed(config.seed)
    if(config.cuda):
        torch.cuda.manual_seed_all(config.seed)
    prepare_directories(config)

    train_model(config)
