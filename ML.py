from sklearn.linear_model import LinearRegression
import random

from sklearn.svm import l1_min_c

feature_set = []
target_set=[]
number_of_rows =50
random_number_limit=300


for i in range(number_of_rows):
    x=random.randint(0,random_number_limit)
    y=random.randint(0,random_number_limit)
    z=random.randint(0,random_number_limit)

    function = 2*x*x + 10*y + 7*z
    feature_set.append([x,y,z])
    target_set.append(function)


for i in range(len(feature_set)):
    print(i, feature_set[i],"  -->",target_set[i])

model=LinearRegression()
model.fit(feature_set,target_set)

test_set=[[8,10,0]]

prediction= model.predict(test_set)

print(prediction,model.coef_)