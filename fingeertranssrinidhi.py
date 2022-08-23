import mediapipe as mp
import cv2 as cv
import numpy as np



def yclose(keypoints,Hand):
    Hand = []
    if Hand == 'R':
        if keypoints[4][0]<keypoints[2][0]:
            Hand.append(0)
            
        else:
            Hand.append(1)
    if Hand== 'L':
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

def xclose(keypoints,Hand):
    Hand = []
    
    if keypoints[4][1]<keypoints[2][1]:
        Hand.append(0)
        #print('R T close')
    else:
        Hand.append(1)
    if Hand == 'R':
        for finger in [8,12,16,20]:
            if keypoints[finger][0]>keypoints[finger-2][0]:
                Hand.append(0)
            else:
                Hand.append(1)
    if Hand== 'L':
        for finger in [8,12,16,20]:
            if keypoints[finger][0]<keypoints[finger-2][0]:
                Hand.append(0)
            else:
                Hand.append(1)

    return Hand   
Ry = [-1,-1,-1,-1,-1]
Rx = [-1,-1,-1,-1,-1]
Ly = [-1,-1,-1,-1,-1]
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

capture = cv.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.25,min_tracking_confidence=0.25) as holistic:
    while True:
        ret,frame = capture.read()
        
        img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        results = holistic.process(img)
        
            
        mp_drawing.draw_landmarks(frame,results.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(frame,results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)

        
        rKeypoints = np.array([[res.x,res.y] for res in results.right_hand_landmarks.landmark]) if results.right_hand_landmarks else np.zeros([21,2])
        lKeypoints = np.array([[res.x,res.y] for res in results.left_hand_landmarks.landmark]) if results.left_hand_landmarks else np.zeros([21,2])
        
        if rKeypoints[1][0]>rKeypoints[17][0]:
            Ry = yclose(rKeypoints,'R')
            #print('R Up')
        else:
            Rx = xclose(rKeypoints,'R')
        if lKeypoints[2][0]<lKeypoints[17][0]:
            Ly = yclose(lKeypoints,'L')
            #print('L Up')
        if Rx == [0,0,0,0,0]:
            #print('RClose')
            pass
        if Ly == [0,0,0,0,0]:
            #print('LClose')
            pass
        
            
        
        

        cv.imshow('Holistic',frame)


        if cv.waitKey(20) & 0xff==ord('x'):
            break

capture.release()
cv.destroyAllWindows()