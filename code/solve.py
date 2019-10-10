#!/usr/bin/python3
import cv2
import numpy as np
import os
import measure
import scale
import export


####

###
names = ['pawn', 'bishop', 'queen']
#mmperpix = 70/694
#mmperpix = 45/537
mmperpix={'pawn':45/537, 'bishop': 60/604,'queen':70/694} 
sizes = {}
sides = {}

for name in names:
    sizes[name] = measure.measure('../cut_images/'+name+'.png')
sizes['base'] = measure.measure('../cut_images/base.png')

for name in names:
    sizes[name] = scale.scale(sizes[name], mmperpix[name])
    sizes['base_'+name] = scale.scale(sizes['base'], mmperpix[name])

for name in names:
    export.export('../scad_files/'+name+'.scad', sizes['base_'+name], mmperpix[name], sizes[name], mmperpix[name])