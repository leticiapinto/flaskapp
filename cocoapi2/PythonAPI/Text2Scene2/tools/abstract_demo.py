#!/usr/bin/env python

import _init_paths
import math, cv2, random
import numpy as np
import os.path as osp
from copy import deepcopy
import matplotlib.pyplot as plt
from datasets.abstract_scene import abstract_scene
from modules.abstract_trainer import SupervisedTrainer

from abstract_utils import *
from abstract_config import get_config
import sys


def abstract_demo(config, input_app):
    transformer = image_normalize('background')
    train_db = abstract_scene(config, split='train', transform=transformer)   
    trainer = SupervisedTrainer(train_db)
    input_sentences = json_load('examples/abstract_samples.json')
    #print(type(input_sentences))
    #print(input_sentences[0])
    #input_sentences_2 = prepare_data('Mike talks to the dog.,Jenny kicks the soccer ball.,The duck wants to play.')
    #print(input_sentences_2)
    input_app = prepare_data(input_app)
    #print(type(input_sentences_2))
    #print(input_app)
    #print(type(input_app))
    trainer.sample_demo(input_app)

def prepare_data(input_text):
    mylist = input_text.split(',')
    return [list(mylist)]

if __name__ == '__main__':

    #print("This is the 2nd arg: ", sys.argv[2])
    #print("This is the 3rd arg: ", sys.argv[3])
    input_app = sys.argv[2]
    #print(json_load(sys.argv[3]))
    cv2.setNumThreads(0)
    config, unparsed = get_config()
    config = abstract_arguments(config)
    np.random.seed(config.seed)
    random.seed(config.seed)
    torch.manual_seed(config.seed)
    if(config.cuda):
        torch.cuda.manual_seed_all(config.seed)
    #print(config)
    #postfix = datetime.now().strftime("%m%d_%H%M%S")
    postfix = sys.argv[3]
    print(postfix)
    prepare_directories(config, postfix)

    abstract_demo(config, input_app)
