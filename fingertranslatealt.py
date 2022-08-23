import cv2

import HandTrackingModule as htm

pTime = 0
tipIds = [4, 8, 12, 16, 20]
spl_point = [21]
probabilityCount = [0 for i in range(20)]
fingers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

detector = htm.handDetector(detectionCon=1)


def runner(InputFromPyQt5):
    global pTime, tipIds, probabilityCount, fingers, spl_point

    img = InputFromPyQt5
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
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
            # print("right")
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                leftFingers.append(1)
            else:
                leftFingers.append(0)

            # 4 fingers
            for id in range(1, 5):
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
                    'How are you?', 'peace',
                    'I love You', 'Im fine ', 'Thank you', 'Surprise', "Whatever", "Stop", "Up", "Bye", "Me"]

        print(probabilityCount)
        # print (leftFingers)
        if lmList[tipIds[0]][1] < lmList[tipIds[4]][1]:

            # 1100
            if (f[0] and f[1] and not f[2] and not f[3] and not f[4]):
                probabilityCount[0] += 1
            # elif (f[5] and f[6] and f[7] and f[8] and f[9]):
            #     probabilityCount[8]+=1
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
            # 01100
            elif (not f[0] and f[1] and f[2] and not f[3] and not f[4]):
                probabilityCount[10] += 1


        # -----------right hand------------------
        else:
            print(f[5:])
            # 11001  --ilu
            if (f[5] and f[6] and not f[7] and not f[8] and f[9]):
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

            # 01110 - whatever
            elif (not f[5] and f[6] and f[7] and f[8] and not f[9]):
                probabilityCount[15] += 1
            # 00000 - stop
            elif (not f[5] and not f[6] and not f[7] and not f[8] and not f[9]):
                probabilityCount[16] += 1

            # 01000 -- up
            elif (not f[5] and f[6] and not f[7] and not f[8] and not f[9]):
                probabilityCount[17] += 1
            # 11111 -- bye
            elif (f[5] and f[6] and f[7] and f[8] and f[9]):
                probabilityCount[18] += 1

            # 10000 -me
            elif (f[5] and not f[6] and not f[7] and not f[8] and not f[9]):
                probabilityCount[19] += 1

        for i, prob in enumerate(probabilityCount):
            # print(f"in for,{prob}, {i}")
            if prob >= 16:
                outputText = (messages[i])
                # textToSpeech(outputText)

                # print(probabilityCount)
                probabilityCount = [0 for i in range(21)]
        # h, w, c = overlayList[0].shape
        # img[0:h,0:w]=overlayList[0]

    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    # cv2.putText(img, f'FPS : {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)

    cv2.waitKey(1)
    # if cv2.waitKey(10) & 0xFF == ord("d"):
    #     break

    try:
        return img, outputText
    except NameError:
        return img

# cap.release()
# cv2.destroyAllWindows()
