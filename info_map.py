#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Info map for 800 series Roomba

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

# Setup Network
whole = gv.Digraph(comment='Roomba Info Map',format ='png',engine = 'dot')

# Top Level - Hardware (sensors)
whole.node('ir','IR Sensors', shape = 'box', style='filled', color='deepskyblue')
whole.node('drop', 'Wheel Drop Sensor', shape = 'box', style='filled', color='deepskyblue')
whole.node('l_bumper', 'Left Bumper', shape = 'box', style='filled', color='deepskyblue')
whole.node('r_bumper', 'Right Bumper', shape = 'box', style='filled', color='deepskyblue')
whole.node('dust_sensor', 'Dust Sensor', shape = 'box', style='filled', color='deepskyblue')
whole.node('fill_sensor', 'Fill Sensor', shape = 'box', style='filled', color='deepskyblue')
whole.node('top_ir','Top IR Receiver', shape = 'box', style='filled', color='deepskyblue')

# Intermediate Level - Code
whole.node('ir_driver', 'IR I/O Driver')
whole.node('img_database', 'Image Database')
whole.node('img_recog', 'Image Recognition')
whole.node('vslam', 'vSLAM')
whole.node('path_plan', 'Path Planning')
whole.node('motor_control', 'Motor Controller')
whole.node('drop_logic','Drop Sensor Logic Code')
whole.node('drop_driver', 'Drop I/O Driver')
whole.node('bump_driver', 'Bumper Driver')
whole.node('bump_logic','Bump Direction Logic')
whole.node('dust_driver', 'Dust Sensor Driver')
whole.node('fill_driver', 'Fill Sensor Driver')
whole.node('dust_logic', 'Dust Collection Logic')
whole.node('fill_logic', 'Full Bin Logic')
whole.node('user_io', 'User Interface Code')
whole.node('bounds','Boundary and Docking Logic')
whole.node('vac_io','Vac Motor Driver')
whole.node('pwr_node','Power Unit Driver')

# Bottom Level - Hardware (motors)
whole.node('l_motor', 'Left Motor', shape = 'diamond', style='filled', color='coral1')
whole.node('r_motor', 'Right Motor', shape = 'diamond', style='filled', color='coral1')
whole.node('vac_motor', 'Vacuum Motor', shape = 'diamond', style='filled', color='coral1')
whole.node('ui', 'User Interface Hardware', shape = 'diamond', style='filled', color='coral1')
whole.node('power','Power',shape = 'diamond', style='filled', color='coral1')

# Circuit Hardware
#whole.node('slam_processor','SLAM Processor', shape = 'hexagon', style = 'filled', color = 'green')
#whole.node('veh_processor','Vehicle Control Processor', shape = 'hexagon', style = 'filled', color = 'gold')
#whole.node('chip_coms','Chip I/O', shape = 'hexagon', style = 'filled', color = 'gold')
#whole.node('ir_chip','IR Processor', shape = 'hexagon', style = 'filled', color = 'green')
#whole.node('drop_chip','Drop Sensor Processor', shape = 'hexagon', style = 'filled', color = 'gold')
#whole.node('bump_chip','Bump Processor', shape = 'hexagon', style = 'filled', color = 'gold')
#whole.node('dust_chip','Dust Processor', shape = 'hexagon', style = 'filled', color = 'gold')
#whole.node('fill_chip','Fill Processor', shape = 'hexagon', style = 'filled', color = 'gold')

# Connect edges
# Mapping
whole.edge('ir','ir_driver')
whole.edge('ir_driver','img_database')
whole.edge('ir_driver','img_recog')
whole.edge('ir_driver','vslam')
whole.edge('img_database','path_plan')
whole.edge('img_recog','path_plan')
whole.edge('vslam','path_plan')
whole.edge('path_plan','motor_control')
whole.edge('motor_control','l_motor')
whole.edge('motor_control', 'r_motor')

# Drop Sensor
whole.edge('drop','drop_driver')
whole.edge('drop_driver','drop_logic')
whole.edge('drop_logic','motor_control')

# Bumpers
whole.edge('l_bumper', 'bump_driver')
whole.edge('r_bumper', 'bump_driver')
whole.edge('bump_driver', 'bump_logic')
whole.edge('bump_logic', 'path_plan')

# Dust Bin
whole.edge('dust_sensor','dust_driver')
whole.edge('dust_driver','dust_logic')
whole.edge('dust_logic','path_plan')
whole.edge('fill_sensor','fill_driver')
whole.edge('fill_driver','fill_logic')
whole.edge('fill_logic', 'user_io')
whole.edge('user_io','ui')
whole.edge('fill_logic','vac_io')
whole.edge('vac_io','vac_motor')
whole.edge('fill_logic','path_plan')

# RCON
whole.edge('top_ir','ir_driver')
whole.edge('ir_driver','bounds')
whole.edge('bounds','pwr_node')
whole.edge('pwr_node','power')
whole.edge('bounds','vac_io')
whole.edge('bounds','path_plan')
whole.edge('bounds','user_io')




whole.render('output/map.gv', view=True)
