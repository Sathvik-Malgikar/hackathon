

import cv2
import time

import os


import HandTrackingModule as htm






wCam , hCam = 1000 , 450
cap=cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# folderPath= "hgsamples"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList=[]

# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     overlayList.append(image)

# print(len(overlayList))
pTime=0

detector = htm.handDetector(detectionCon=1)

tipIds=[4,8,12,16,20]
probabilityCount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fingers=[0,0,0,0,0,0,0,0,0,0]

while True :
    s, image = cap.read()



    # success,  img = cap.read()
    # img=cv2.flip(img,1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList)!=0:
        rightFingers=[]
        leftFingers=[]
        
        if lmList[tipIds[0]][1]>lmList[tipIds[4]][1]:
            leftFingers=[0,0,0,0,0]
            #thumb
            if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                rightFingers.append(1)
            else:
                rightFingers.append(0)


            #4 fingers
            for id in range(1,5):
                if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                    rightFingers.append(1)
                else:
                    rightFingers.append(0)
        else:
            rightFingers=[0,0,0,0,0]
            #thumb
            if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                leftFingers.append(0)
            else:
                leftFingers.append(1)


            #4 fingers
            for id in range(1,5):
                if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                    leftFingers.append(1)
                else:
                    leftFingers.append(0)
        fingers=leftFingers+rightFingers
        f=fingers
        # print(fingers)
        messages=["HI","NO","YES","How are you",'Later','Please','Thanks','Bye','Great!',\
            'when?','where?','i will be back in two minutes','why?','which one?','Do not know']

        if (f[0] and f[1] and f[2] and f[3] and f[4] ) :
            probabilityCount[0]+=1
        if (f[5] and f[6] and f[7] and f[8] and f[9]):
            probabilityCount[8]+=1
        if (f[0] and not f[1] and not f[2] and not f[3] and not f[4]) :
            probabilityCount[2]+=1
        if (not f[0] and f[1] and not f[2] and not f[3] and not f[4]) :

            probabilityCount[3]+=1
        if (not f[0] and  f[1] and f[2] and  f[3] and not f[4]) :
         
            probabilityCount[4]+=1
        if (not f[0] and  f[1] and  f[2] and not f[3] and not f[4]) :
           
            probabilityCount[5]+=1
        if (not f[0] and not f[1] and not f[2] and not f[3] and f[4]) :
         
            probabilityCount[6]+=1
        if (not f[0] and not f[1] and  f[2] and  f[3] and f[4]) :
        
            probabilityCount[7]+=1
        if (f[5]and not f[6]and not f[7]and not f[8]and not f[9]):
            probabilityCount[9]+=1

        if (not f[5]and f[6]and not f[7]and not f[8]and not f[9]):
            probabilityCount[10]+=1

        if (not f[5]and f[6]and f[7]and not f[8]and not f[9]):
            probabilityCount[11]+=1

        if (not f[5]and not f[6]and not f[7]and  f[8]and f[9]):
            probabilityCount[12]+=1

        if (not f[5]and not f[6]and not f[7]and not f[8]and  f[9]):
            probabilityCount[13]+=1

        if (not f[5]and not f[6]and  f[7]and  f[8]and  f[9]):
            probabilityCount[1]+=1

        if (not f[5] and f[6] and f[7] and f[8] and f[9]):
            probabilityCount[14]+=1



        for i,prob in enumerate(probabilityCount):
            if prob>=10:
                outputText=(messages[i])

                print(outputText)
                
                # print(probabilityCount)
                probabilityCount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]




    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,  f'FPS : {int(fps)}', (400,70), cv2.FONT_HERSHEY_PLAIN, 3 , (255,0,0), 2)


    # cv2.imshow("Image", img)
    cv2.waitKey(1)
    cv2.imshow(img)



'''
HI  -    all five fingers of right hand.
NO -   last three fingers of left hand
YES - right thumb
How are you - right index
Later- mid three fingers
Please- right victory symbol 
thanks - right little finger
Bye - last three fingers of right hand
Great! - left palm
when- left thumb
where left index
i will be back in two minutes - left hand victory symbol
why- left last two fingers
which one- left little finger
do not know- left four fingers





'''