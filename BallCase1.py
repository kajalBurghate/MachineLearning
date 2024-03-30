
from sklearn import tree

def main():
    print("Ball Classification case study")


#Load the data
    ballfeatures = [[35, "Rough"], [47, "Rough"], [90, "Smooth"], [48, "Rough"], [90, "Smooth"], [35, "Rough"], [92, "Smooth"], [35, "Rough"],[35, "Rough"],[35, "Rough"], [96, "Smooth"], [43, "Rough"], [110, "Smooth"], [35, "Rough"], [95, "Smooth"]]
    labels = ["Teenis", "Teenis", "Cricket", "Tennis", "Cricket", "Teenis","Cricket", "Teenis","Teenis","Teenis","Cricket", "Teenis","Cricket","Teenis","Cricket"]

    obj = tree.DecisionTreeClassifier()  #decide the algorithm

    obj = obj.fit(ballfeatures, labels)   #Train the data

    print(obj.predict([[36, "Rough"], [91, "Smooth"]]))   #Test model

    





if __name__ == "__main__":
    main()