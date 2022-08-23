# import imp
from email import message
from sre_constants import SUCCESS
import cv2
import time
import os
import pygame
from gtts import gTTS
import HandTrackingModule as htm
import mediapipe as mp

pygame.mixer.init()


def textToSpeech(t):
    language = 'en'
    output = gTTS(text=t, lang=language, slow=False)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    # os.remove("output.mp3")
    output.save("output.mp3")

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    cv2.putText(img, t, (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (250, 250, 0), 3)
    cv2.imshow("Image", img)
    # time.sleep(1)


wCam, hCam = 648, 488
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# folderPath= "image"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList=[]

# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     overlayList.append(image)

# print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0)

tipIds = [4, 8, 12, 16, 20]
spl_point = [21]
probabilityCount = [0 for i in range(20)]
fingers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        rightFingers = []
        leftFingers = []
        if lmList[tipIds[0]][1] > lmList[tipIds[4]][1]:
            leftFingers = [0, 0, 0, 0, 0]
            # thumb
            # if lmList[tipIds[0]][1]<lmList[tipIds[0]-1][1]:
            #     rightFingers.append(1)
            # else:
            #     rightFingers.append(0)

            # 4 fingers
            for id in range(5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    rightFingers.append(1)
                else:
                    rightFingers.append(0)
        else:
            rightFingers = [0, 0, 0, 0, 0]
            # thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                leftFingers.append(0)
            else:
                leftFingers.append(1)

            # 4 fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    leftFingers.append(1)
                else:
                    leftFingers.append(0)
        fingers = leftFingers + rightFingers
        f = fingers
        # print(fingers)
        messages = ["Later", "Thumbs down", "Thumbs Up", "Hi", 'Super', 'Rock', 'Restroom', 'Stay Strong', 'Good Luck!',
                    'How are you?', 'peace?',
                    'I love You', 'Im fine ', 'Thank you', 'Surprise']

        print(leftFingers)
        # 1100
        if (f[0] and f[1] and not f[2] and not f[3] and not f[4]):
            probabilityCount[0] += 1
        elif (f[5] and f[6] and f[7] and f[8] and f[9]):
            probabilityCount[8] += 1
        # if (not f[0] and not f[1] and not f[2] and not f[3] and not f[4]):

        #     probabilityCount[1]+=1

        # thumbs down
        elif (lmList[20][2] < lmList[4][2] and not f[1] and not f[2] and not f[3] and not f[4]):
            probabilityCount[1] += 1
        # thumbs up
        elif (f[0] and not f[1] and not f[2] and not f[3] and not f[4]):
            probabilityCount[2] += 1
        # 11111
        elif (f[0] and f[1] and f[2] and f[3] and f[4]):
            probabilityCount[3] += 1
        # 00111
        elif (not f[0] and not f[1] and f[2] and f[3] and f[4]):
            probabilityCount[4] += 1
        # 01001
        elif (not f[0] and f[1] and not f[2] and not f[3] and f[4]):
            probabilityCount[5] += 1
        # 00001
        elif (not f[0] and not f[1] and not f[2] and not f[3] and f[4]):
            probabilityCount[6] += 1

        # 00000
        elif (not f[0] and not f[1] and not f[2] and not f[3] and not f[4]):

            probabilityCount[7] += 1
        # interchange 01100  good luck
        elif (not f[0] and not f[3] and not f[4] and lmList[12][1] < lmList[8][1]):
            probabilityCount[8] += 1

        # 11101
        elif (f[0] and f[1] and f[2] and not f[3] and f[4]):
            probabilityCount[9] += 1

        elif (not f[0] and f[1] and f[2] and not f[3] and not f[4]):
            probabilityCount[10] += 1

        # -----------right hand------------------

        # 11001  --ilu
        elif (f[5] and f[6] and not f[7] and not f[8] and f[9]):
            probabilityCount[11] += 1

        # 11101  -- im fine
        elif (f[5] and f[6] and f[7] and not f[8] and f[9]):
            probabilityCount[12] += 1
        # 11100
        elif (f[5] and f[6] and f[7] and not f[8] and not f[9]):
            probabilityCount[13] += 1
        # 10001
        elif (f[5] and not f[6] and not f[7] and not f[8] and f[9]):
            probabilityCount[14] += 1


        elif (not f[5] and not f[6] and f[7] and f[8] and f[9]):
            probabilityCount[1] += 1

        elif (not f[5] and f[6] and f[7] and f[8] and f[9]):
            probabilityCount[14] += 1

        for i, prob in enumerate(probabilityCount):
            # print(f"in for,{prob}, {i}")
            if prob >= 20:
                outputText = (messages[i])
                textToSpeech(outputText)

                print(probabilityCount)
                probabilityCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # h, w, c = overlayList[0].shape
    # img[0:h,0:w]=overlayList[0]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS : {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == ord("d"):
        break;
cap.release()
cv2.destroyAllWindows()

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
ill be back in two minutes - left hand victory symbol
why- left last two fingers
which one- left little finger
do not know- left four fingers
'''
