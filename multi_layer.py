#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Multi-Layer Network for 800 series Roomba

@author: jcoller
"""
# Do float division
from __future__ import division

# Imports
# matplotlib.use('TkAgg')

import networkx as nx
import graphviz as gv
import networkx.drawing
# from networkx.drawing.nx_pydot import grahviz_layout
# from graphviz import Digraph
import matplotlib.pyplot as plt
import random
# import pylab as plt
# import random
# import scipy
import numpy as np

# Setup Overview network
primary = gv.Digraph(comment='Roomba Overall Functions',format ='png',engine = 'circo')

primary.node('drive','Drive')
primary.node('nav','Navigate')
primary.node('charge','Recharge')
primary.node('vacuum','Clean Floors')
primary.node('empty','Empty Dirt')

primary.edge('nav','drive')
primary.edge('drive','nav')

# Render the Map
primary.render('output/multi_1.gv', view=True)
