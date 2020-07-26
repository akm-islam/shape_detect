#!/usr/bin/env python
# coding: utf-8
import numpy as np
import cv2
def getWidth(cnt):
    a=[]
    for i in cnt:
        a.append(i[0][0])
    #print("min",min(a),"max",max(a))
    return max(a)-min(a)
def getHeight(cnt):
    a=[]
    for i in cnt:
        a.append(i[0][1])
    return max(a)-min(a)
def getXY(cnt):
    a=[]
    b=[]
    for i in cnt:
        a.append(i[0][0])
        b.append(i[0][1])
    #print("min",min(a),min(b))
    return (min(a),min(b))
def getShape(img_url):
    img = cv2.imread(img_url)
    print(img.shape)
    print()
    #----------------
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    contours,h = cv2.findContours(thresh,1,2)
    #----------------
    dict_to_return={}
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if len(approx)==4:
            if getXY(cnt)[0]!=0:
                dict_to_return["div"+str(np.random.randint(10))]={"width":getWidth(cnt),"Height":getHeight(cnt),"x":getXY(cnt)[0],"y":getXY(cnt)[1]}
        elif len(approx)==7:
            dict_to_return["div"+str(np.random.randint(10))]={"width":getWidth(cnt),"Height":getHeight(cnt),"x":getXY(cnt)[0],"y":getXY(cnt)[1]}
        elif len(approx)==6:
            dict_to_return["div"+str(np.random.randint(10))]={"width":getWidth(cnt),"Height":getHeight(cnt),"x":getXY(cnt)[0],"y":getXY(cnt)[1]}
        elif len(approx)==8:
            dict_to_return["div"+str(np.random.randint(10))]={"width":getWidth(cnt),"Height":getHeight(cnt),"x":getXY(cnt)[0],"1":getXY(cnt)[1]}
    return dict_to_return
print(getShape('01.png'))
