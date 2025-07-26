import math
import random
import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,600)
detector = HandDetector(detectionCon=0.7,maxHands=2)
class all():
    def __init__(self,pathfood):
        self.points = []
        self.lenght = []
        self.allenght = 0
        self.maxlenght = 150
        self.beforhead = 0,0
        self.imgfood = cv2.imread(pathfood, cv2.IMREAD_UNCHANGED)
        self.imgfood = cv2.resize(self.imgfood, (50, 50), interpolation=cv2.INTER_AREA)
        self.hfood, self.wfood, _ = self.imgfood.shape
        self.foodpoints = 0,0 
        self.randoma()
    def randoma (self):
            self.foodpoints = random.randint(100,650) , random.randint(100,400)
 

    def update(self,imgmain,afterhead):
        px , py = self.beforhead
        cx , cy = afterhead
        self.points.append([cx,cy])
        distance = math.hypot(cx - px,cy - py)
        self.lenght.append(distance)
        self.allenght += distance
        self.beforhead = cx,cy
        if self.allenght > self.maxlenght:
            for i , lenght in enumerate(self.lenght):
                self.allenght -= lenght
                self.lenght.pop(i)
                self.points.pop(i)
                if self.allenght < self.maxlenght:
                    break
        rx , ry = self.foodpoints
        if rx - self.wfood//2 < cx < rx + self.wfood // 2 and ry - self.hfood//2 <cy<ry + self.hfood:
            self.randoma()
            self.maxlenght += 25
        if self.points:
            for i , points in enumerate(self.points):
                if i != 0 :
                    cv2.line(imgmain,self.points[i-1],self.points[i],(0,0,250),20)
                    cv2.circle(imgmain,self.points[-1],20,(200,0,200),cv2.FILLED)
            rx,ry = self.foodpoints
            imgmain = cvzone.overlayPNG(imgmain,self.imgfood,(rx-self.wfood//2, ry - self.hfood//2))

        return imgmain   

game = all('hacker.png')

while True:
    secsses , img  = cap.read()
    img = cv2.flip(img,1)
    hands , img = detector.findHands(img,flipType=False)
    if hands:
        lmList = hands[0]['lmList']
        pointendix = lmList[8][0:2]
        # cv2.circle(img,pointendix,30,(200,0,200),cv2.FILLED)
        img = game.update(img,pointendix)
    cv2.imshow('Snak',img)
    key = cv2.waitKey(1)
    if key == 27:  # Esc key
       break