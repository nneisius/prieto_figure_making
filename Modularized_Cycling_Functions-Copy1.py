#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib
import matplotlib.pyplot as plt
import math
from pylab import rcParams
from pylab import figure
from pandas import read_excel 
import ipywidgets as widgets
from itertools import cycle
import glob
import matplotlib.gridspec as gridspec

class files:
    def __init__(self,path):
        self.path = path
        
    def retrieve(self):
        """
        req.: path.
        retrieves all files in a path - makes a list for files.
        """
        global files
        flist = []
        for item in glob.glob(self.path):
            flist.extend([item])
        flist.sort()
        
        return flist

class data:
    def __init__(self,file,arbin,mass,label):
        self.file = file
        self.arbin = arbin
        self.mass = mass
        self.label = label
    def data_cycle(self):
        """
        gets cycle data from import. Need file,arbin and mass.
        arbin = 'new' or 'old'
        mass in g
    
        """
        if self.arbin == 'new':
            cycle_cols = 'B,D,E,F,H,I'
        else:
            cycle_cols = 'B,E,F,H,I,J'
        
        df = pd.read_excel(self.file, sheet_name=1, usecols=cycle_cols,names=['time','step','cycle','voltage','charge','discharge'])
        return df
    def data_cap(self):
        if self.arbin == 'new':
            cap_cols = 'E,H,I'
        else:
            cap_cols = 'A,F,G'
        df = pd.read_excel(self.file,  
            sheet_name=2,                        
            usecols=cap_cols,    #these columns change depending on which Arbin the data originated
            names=['cycle','charge','discharge'])     
        return df
    def data_by_cycle(self):
        dt = self.data_cycle().groupby(['cycle','step'])
        return dt
    def cycle_nums(self):
        a = self.data_cap()
        number = a['cycle'].iat[-1]-2
        return number



