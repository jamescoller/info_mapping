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

# Setup Overview network
whole = gv.Digraph(comment='Roomba Overall Functions',format ='png',engine = 'dot')

whole.node('roomba','Roomba', shape = 'hexagon')
whole.node('drive','Drive', shape = 'box')
whole.node('nav','Navigate',shape = 'box')
whole.node('charge','Recharge',shape = 'box')
whole.node('vacuum','Clean Floors',shape = 'box')
whole.node('empty','Empty Dirt',shape = 'box')

whole.edge('roomba','drive')
whole.edge('roomba','nav')
whole.edge('roomba','charge')
whole.edge('roomba','vacuum')
whole.edge('roomba','empty')

# Render the Drive Map
whole.render('output/whole.gv', view=True)

# Setup Drive Function Network
drive = gv.Digraph(comment='Roomba Drive Function',format ='png',engine = 'dot')

# Nodes
drive.node ('drive','Drive', shape = 'box')
drive.node('fwd', 'Move Forward')
drive.node('back','Move Backard')
drive.node('turn','Turn Left or Right')
drive.node('nostuck','Do Not Get Stuck')
drive.node('nocliff','Do Not Fall Off Cliff')
drive.node('onGround','Drive on Ground Only')

drive.node('spinL','Spin Left Wheel')
drive.node('spinR','Spin Right Wheel')
drive.node('act_motor','Activate Motor')
drive.node('motor_control','Motor Controller Signal')
drive.node('nav_cmd','Navigation Command')

drive.node('wheels_move','Ensure Wheels are Moving')
drive.node('not_wall','Ensure Not on Wall')
drive.node('Bump','Bump Sensor')
drive.node('trigger','Bump Trigger')
drive.node('spring','Bump Spring')
drive.node('enconder','Wheel Encoders')
drive.node('logic','Logic Processor')

drive.node('wheel_drop','Wheel Drop Sensor')
drive.node('wh_trigger','Trigger')
drive.node('wh_spring','Spring')
drive.node('IR','IR Sensor')
drive.node('ir_trans','Transmitter')
drive.node('ir_rec','Receiver')
drive.node('cliff_logic','Logic Processor')

drive.node('ground_logic','Logic Processor')


# edges
drive.edge('drive','fwd')
drive.edge('drive','back')
drive.edge('drive','turn')
drive.edge('drive','nostuck')
drive.edge('drive','nocliff')
drive.edge('drive','onGround')

drive.edge('fwd','spinL')
drive.edge('fwd','spinR')

drive.edge('back','spinL')
drive.edge('back','spinR')

drive.edge('turn','spinR')
drive.edge('turn','spinL')

drive.edge('spinL','act_motor')
drive.edge('spinR','act_motor')
drive.edge('act_motor','motor_control')
drive.edge('motor_control','nav_cmd')

drive.edge('nostuck','wheels_move')
drive.edge('nostuck','not_wall')
drive.edge('wheels_move','enconder')
drive.edge('nostuck','logic')
drive.edge('not_wall','Bump')
drive.edge('Bump','trigger')
drive.edge('Bump','spring')

drive.edge('nocliff','wheel_drop')
drive.edge('wheel_drop','wh_spring')
drive.edge('wheel_drop','wh_trigger')
drive.edge('nocliff','IR')
drive.edge('IR','ir_rec')
drive.edge('IR','ir_trans')
drive.edge('nocliff','cliff_logic')

drive.edge('onGround','wheel_drop')
drive.edge('onGround','ground_logic')

# Render the Drive Map
drive.render('output/drive.gv', view=True)

# Setup Drive Function Network
nav = gv.Digraph(comment='Roomba Navigate Function',format ='png',engine = 'dot')

# Nodes
nav.node('nav','Navigate', shape = 'box')
nav.node('on_dirt','Stay on Dirty Area')
nav.node('is_dirt','Check for Dirt')
nav.node('cover_room','Cover Full Room')
nav.node('avoid','Avoid Obstacles')
nav.node('rcon','Robot Confinement')
nav.node('map','Mapping')
nav.node('home','Find "Home"')

nav.node('pizo','Pizoelectric Sensor')
nav.node('dirt-circuit','Sensor Circuit')
nav.node('power','Power Source')
nav.node('dirt-logic','Logic Processor')
nav.node('motor_control','Motor Control')

nav.node('cover_logic','Logic Processor')
nav.node('pose','Pose Estimation')
nav.node('wheel_enc','Wheel Encoders')
nav.node('frnt_track','Front Wheel Tracking')

nav.node('bumper','Bumpers')
nav.node('bump-trigger','Trigger')
nav.node('bump-spring','Spring')
nav.node('no-fall','Do Not Fall Down')
nav.node('ir','IR Sensors')
nav.node('wheel_drop','Wheel Drop Sensor')
nav.node('fall-logic','Logic Processor')
nav.node('ir-send','IR Transmitter')
nav.node('ir-rec','IR Receiver')
nav.node('drop-trigger','Trigger')
nav.node('drop-spring','Spring')
nav.node('see-wall','ID Walls')
nav.node('avoid-logic','Logic Processor')

nav.node('lighthouse','Lighthouse Transmit Signal')
nav.node('lh_pwr','Variable Power Knob')
nav.node('lh_ir_trans','IR Transmitter')
nav.node('lh_pwr_src','Power Source')
nav.node('bat','Battery')
nav.node('rbt','Robot Receive Signal')
nav.node('rbt-rec','IR Receiver')
nav.node('rbt-logic','Logic Processor')

nav.node('dead','Dead Reckoning')
nav.node('prior','Prior Positions')
nav.node('current','Current Position')
nav.node('odom','Odometry')
nav.node('vis','Visual Sensing')
nav.node('vis_front_end','Locate Image in Database')
nav.node('img','Image Data')
nav.node('database','Landmark Database')
nav.node('slam','SLAM')
nav.node('slam-data','Data')
nav.node('slam-base','SLAM Database')
nav.node('map-logic','Logic Processing')

nav.node('home-logic','Logic Processing')
nav.node('home-sig','Recieve Home Signal')
nav.node('home-ir','Top IR Receiver')

# edges
nav.edge('nav','on_dirt')
nav.edge('nav','cover_room')
nav.edge('nav','avoid')
nav.edge('nav','rcon')
nav.edge('nav','map')
nav.edge('nav','home')

nav.edge('on_dirt','is_dirt')
nav.edge('is_dirt','pizo')
nav.edge('pizo','dirt-circuit')
nav.edge('pizo','power')
nav.edge('on_dirt','dirt-logic')
nav.edge('on_dirt','motor_control')

nav.edge('cover_room','cover_logic')
nav.edge('cover_room','map')
nav.edge('cover_room','pose')
nav.edge('pose','wheel_enc')
nav.edge('pose','frnt_track')
nav.edge('cover_room','motor_control')

nav.edge('avoid','map')
nav.edge('avoid','bumper')
nav.edge('bumper','bump-trigger')
nav.edge('bumper','bump-spring')
nav.edge('avoid','no-fall')
nav.edge('no-fall','ir')
nav.edge('no-fall','wheel_drop')
nav.edge('wheel_drop','drop-trigger')
nav.edge('wheel_drop','drop-spring')
nav.edge('no-fall','fall-logic')
nav.edge('ir','ir-send')
nav.edge('ir','ir-rec')
nav.edge('avoid','see-wall')
nav.edge('see-wall','ir')
nav.edge('avoid','avoid-logic')

nav.edge('rcon','lighthouse')
nav.edge('lighthouse','lh_pwr')
nav.edge('lighthouse','lh_ir_trans')
nav.edge('lighthouse','lh_pwr_src')
nav.edge('lh_pwr_src','bat')
nav.edge('rcon','rbt')
nav.edge('rbt','rbt-rec')
nav.edge('rbt','rbt-logic')
nav.edge('rbt','motor_control')

nav.edge('map','dead')
nav.edge('dead','prior')
nav.edge('dead','current')
nav.edge('current','pose')
nav.edge('current','odom')
nav.edge('odom','wheel_enc')
nav.edge('map','vis')
nav.edge('vis','ir')
nav.edge('map','vis_front_end')
nav.edge('vis_front_end','img')
nav.edge('vis_front_end','database')
nav.edge('map','slam')
nav.edge('slam','slam-data')
nav.edge('slam','slam-base')
nav.edge('map','map-logic')

nav.edge('home','home-logic')
nav.edge('home','motor_control')
nav.edge('home','home-sig')
nav.edge('home-sig','home-ir')
nav.edge('home','map')

# Render the Nav Map
nav.render('output/navigate.gv', view=True)

# Setup Power Function Network
pwr = gv.Digraph(comment='Roomba Power Function',format ='png',engine = 'dot')

# Nodes
pwr.node('pwr','Power Supply', shape = 'box')
pwr.node('src','Store Energy')
pwr.node('bat','Battery')
pwr.node('li','Lithium Battery')
pwr.node('charge','Recharge Energy')
pwr.node('charger','Battery Charger')
pwr.node('leads','Battery Leads')
pwr.node('dock','Home Dock Charging')
pwr.node('dist','Distribute Electricity')
pwr.node('circuit','Circuit Board')
pwr.node('wires','Wiring')

# edges
pwr.edge('pwr','src')
pwr.edge('src','bat')
pwr.edge('bat','li')
pwr.edge('pwr','charge')
pwr.edge('charge','charger')
pwr.edge('charger','leads')
pwr.edge('charger','dock')
pwr.edge('pwr','dist')
pwr.edge('dist','circuit')
pwr.edge('dist','wires')

# Render the power Map
pwr.render('output/power.gv', view=True)

# Setup Empty Function Network
empty = gv.Digraph(comment='Roomba Empty Function',format ='png',engine = 'dot')

# Nodes
empty.node('empty','Empty Dirt', shape = 'box')
empty.node('full','Sense if Full')
empty.node('fill','Fill Sensor')
empty.node('logic','Logic Processor')
empty.node('alert','Alert User')
empty.node('light','Activate Light')
empty.node('board','Light on Circuit Board')
empty.node('emptied','Get Emptied')
empty.node('remove','Allow Tray Removal')

# edges
empty.edge('empty','full')
empty.edge('full','fill')
empty.edge('empty','logic')
empty.edge('empty','alert')
empty.edge('alert','light')
empty.edge('light','board')
empty.edge('empty','emptied')
empty.edge('emptied','remove')


# Render the empty Map
empty.render('output/empty.gv', view=True)

# Setup Clean Function Network
clean = gv.Digraph(comment='Roomba Cleaning Function',format ='png',engine = 'dot')

# Nodes
clean.node('clean','Clean Floors', shape = 'box')
clean.node('vacuum','Vacuum')
clean.node('control','Control Vac Motor')
clean.node('motor','Vac Motor')
clean.node('intake','Vac Intake')
clean.node('exh','Vac Exhaust')
clean.node('scrape','Scrape up Dirt & Debris')
clean.node('rollers','Rollers')
clean.node('notangle','Do Not Tangle')
clean.node('torque','Torque Sensor')
clean.node('contain','Contain Dirt')
clean.node('filter','Air Filter')
clean.node('unit','Containment Bin')
clean.node('corners','Clean Along Walls & Corners')
clean.node('brush','Sweeping Brush')

# edges
clean.edge('clean','vacuum')
clean.edge('vacuum','control')
clean.edge('vacuum','motor')
clean.edge('vacuum','intake')
clean.edge('vacuum','exh')
clean.edge('clean','scrape')
clean.edge('scrape','rollers')
clean.edge('scrape','notangle')
clean.edge('notangle','torque')
clean.edge('clean','contain')
clean.edge('contain','filter')
clean.edge('contain','unit')
clean.edge('clean','corners')
clean.edge('corners','brush')


# Render the power Map
clean.render('output/clean.gv', view=True)
