#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 20:48:01 2018

@author: thiago
"""

"""
Music generator using RBM
"""

import numpy as np
import pandas as pd
#import msgpack
import glob
import tensorflow as tf
from tensorflow.python.ops import control_flow_ops
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable


# class to hold all the data for our problem
class DATA(Training, Test = None):


