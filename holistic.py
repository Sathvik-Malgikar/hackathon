import mediapipe as mp
import cv2 as cv
import numpy as np
import HandTrackingModule as htm

pTime = 0
tipIds = [4, 8, 12, 16, 20]
spl_point = [21]
probabilityCount = [0 for i in range(20)]
fingers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

detector = htm.handDetector(detectionCon=1)
#Ha
def yclose(keypoints,hand):
    Hand = []
    if hand == 'R':
        if keypoints[4][0]<keypoints[2][0]:
            Hand.append(0)
            
        else:
            Hand.append(1)
    if hand== 'L':
        if keypoints[4][0]>keypoints[2][0]:
            Hand.append(0)

        else:
            Hand.append(1)

    for finger in [8,12,16,20]:
        if keypoints[finger][1]>keypoints[finger-2][1]:
            Hand.append(0)
        else:
            Hand.append(1)

    return Hand

def xclose(keypoints,hand):
    Hand = []
    
    if keypoints[4][1]>keypoints[2][1]:
        Hand.append(0)
        #print('R T close')
    else:
        Hand.append(1)
    if hand == 'R':
        for finger in [8,12,16,20]:
            if keypoints[finger][0]<keypoints[finger-2][0]:
                Hand.append(0)
            else:
                Hand.append(1)
    if hand== 'L':
        for finger in [8,12,16,20]:
            if keypoints[finger][0]>keypoints[finger-2][0]:
                Hand.append(0)
            else:
                Hand.append(1)

    return Hand   
Ry = [-1,-1,-1,-1,-1]
Rx = [-1,-1,-1,-1,-1]
Ly = [-1,-1,-1,-1,-1]
Lx = [-1,-1,-1,-1,-1]
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

probabilityCount = [0 for i in range(22)]
capture = cv.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.25,min_tracking_confidence=0.25) as holistic:
    while True:
        ret,frame = capture.read()
        
        img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results = holistic.process(img)
        
            
        mp_drawing.draw_landmarks(frame,results.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(frame,results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)

        Ry = [-1,-1,-1,-1,-1]
        Rx = [-1,-1,-1,-1,-1]
        Ly = [-1,-1,-1,-1,-1]
        Lx = [-1,-1,-1,-1,-1]

        
        rKeypoints = np.array([[res.x,res.y] for res in results.right_hand_landmarks.landmark]) if results.right_hand_landmarks else np.zeros([21,2])
        lKeypoints = np.array([[res.x,res.y] for res in results.left_hand_landmarks.landmark]) if results.left_hand_landmarks else np.zeros([21,2])
        

        

        messages = ["Later", "Thumbs down", "Thumbs Up", "Hi", 'Super', 'Rock', 'Restroom', 'Stay Strong', 'Good Luck!',
                    'How are you?', 'peace?',
                    'I love You', 'Im fine ', 'Thank you', 'Surprise','whatever',"stop","up","bye","me",'play','Please']
        
        
        
        if rKeypoints[2][1]>rKeypoints[17][1]:
            Rx = yclose(rKeypoints,'R')
            #print('R Up')
        elif rKeypoints[2][1]<rKeypoints[17][1]:
            
            Ry = xclose(rKeypoints,'R')
        if lKeypoints[2][0]<lKeypoints[17][0]:
            Lx = yclose(lKeypoints,'L')
            #print('L Up')
        elif lKeypoints[2][0]>lKeypoints[17][0] :
            Ly =xclose(lKeypoints,'L')
        

        
        
        #hii
        
        if(Lx==[1,1,1,1,1]):    
            probabilityCount[3]+=1
        # later 
        elif(Lx==[1,1,0,0,0]):
            probabilityCount[0]+=1
        # thumbs up
        elif (Ly==[1,0,0,0,0]):
            probabilityCount[2]+=1
        # thumbs down
        # elif ()
        elif(Ly==[0,0,0,0,0] and lKeypoints[4][1]>lKeypoints[0][1]):
            probabilityCount[1]+=1
        #rock 
        elif (Lx==[0,1,0,0,1]):
            probabilityCount[5]+=1
        # super
        elif(Lx==[0,0,1,1,1]):
            probabilityCount[4]+=1
        # restroom
        elif(Lx==[0,0,0,0,1]):
            probabilityCount[6]+=1
        
        elif(Lx==[0,0,0,0,0]):
            probabilityCount[7]+=1
        
        elif (Lx==[1,1,1,0,1]):
            probabilityCount[9]+=1
        
        elif (Lx ==[1,1,0,0,0]):
            probabilityCount[10]+=1
        
        # ---- right hand ---------

        # ilu
        elif (Rx==[1,1,0,0,1]):
            probabilityCount[11]+=1
    # im fine 
        elif (Rx==[1,1,1,0,1]):
            probabilityCount[12]+=1
        # thank you 
        elif(Rx==[1,1,1,0,0]):
            probabilityCount[13]+=1
        # surprise
        elif (Rx==[1,0,0,0,1]):
            probabilityCount[14]+=1
        # whatever
        elif (Rx==[0,1,1,1,0]):
            probabilityCount[15]+=1
        # stop
        elif (Rx==[0,0,0,0,0]):
            probabilityCount[16]+=1
        
        elif (Rx==[1,0,0,0,0]):
            probabilityCount[19]+=1
        elif (Rx ==[1,1,1,1,1]):
            probabilityCount[18]+=1
        elif (Rx==[0,1,0,0,0]):
            probabilityCount[17]+=1
        elif(Ry==[1,1,1,1,1] and not Ly==[1,1,1,1,1]):
            probabilityCount[21]+=1
        elif(Ry==[1,1,1,1,1] and Ly==[1,1,1,1,1]):
            probabilityCount[13]+=1
        elif(Ry==[1,0,0,0,1] and Ly==[1,0,0,0,1]):
            probabilityCount[20]+=1
        
        

        for i, prob in enumerate(probabilityCount):
            # print(f"in for,{prob}, {i}")
            if prob >= 20:
                outputText = (messages[i])
                # textToSpeech(outputText)
                print (outputText)
                # print(probabilityCount)
                probabilityCount = [0 for i in range(22)]
        
        cv.imshow('Holistic',frame)


        if cv.waitKey(20) & 0xff==ord('x'):
            break

capture.release()
cv.destroyAllWindows()