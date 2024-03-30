
from sklearn import tree

#Rough 1
#Smooth 0

def main():
    print("Ball Classification case study")


#Load the data
    ballfeatures = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1],[35, 1],[35, 1], [96, 0], [43, 1], [110, 0], [35, 1], [95, 0]]
    labels = ["Teenis", "Teenis", "Cricket", "Tennis", "Cricket", "Teenis","Cricket", "Teenis","Teenis","Teenis","Cricket", "Teenis","Cricket","Teenis","Cricket"]

    obj = tree.DecisionTreeClassifier()  #decide the algorithm

    obj = obj.fit(ballfeatures, labels)   #Train the data

    print(obj.predict([[36, 1], [91, 0]]))   #Test modelcd ..

    





if __name__ == "__main__":
    main()