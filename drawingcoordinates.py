# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:05:42 2017

@author: Nishad
"""

from PIL import Image, ImageDraw, ImageFont
import os


#im = Image.open("hunter900x600.png")

#draw = ImageDraw.Draw(im)

#draw.point([96.347360611,201.799144745],'red')

#im.save('hunterMap.png')
numberOfCoordinateFiles = 249

robotPoseFile = open('data_pose.txt','r')
#skip over the title row
robotPoseFile.readline()

pixelMultiplier = 10

for fileNumber in range(numberOfCoordinateFiles):
   wallCoordinateFile = open(str(fileNumber)+'.txt', 'r')
   poseDataLineSplit = robotPoseFile.readline().split(",")
   listOfWallCoordinates = []
   for coordinateTupleString in wallCoordinateFile.readlines():
       coordinateTupleSplit = coordinateTupleString[1:-2].split(", ")
       listOfWallCoordinates.append(float(coordinateTupleSplit[0]) * pixelMultiplier)
       listOfWallCoordinates.append(float(coordinateTupleSplit[1]) * pixelMultiplier)
   #print(listOfWallCoordinates)
   robotCoordinate = []
   robotCoordinate.append(float(poseDataLineSplit[4]) * pixelMultiplier)
   robotCoordinate.append(float(poseDataLineSplit[5]) * pixelMultiplier)
   im = Image.open("hunter900x600.png")
   draw = ImageDraw.Draw(im)
   draw.point(robotCoordinate, 'green')
   draw.point(listOfWallCoordinates, 'red')
   #draw.text((0,0), str(fileNumber), fill = 'blue')
   fontsFolder = 'FONT_FOLDER'
   numberFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
   draw.text((0,0), str(fileNumber), fill = 'blue', font = numberFont)
   im.save(str(fileNumber) + '.png')
   wallCoordinateFile.close()

robotPoseFile.close()
   
   

   

   