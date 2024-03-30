from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a, b):
    return distance.euclidean(a, b)

class MarvellousKNN():
    def fit(self, TrainingData, TrainingTarget):  #User defined
        self.TrainingData = TrainingData
        self.TrainingTarget = TrainingTarget

    def predict(self, TestData):  #user defined
        predictions = []
        for row in TestData:
            lebel = self.closest(row)
            predictions.append(lebel)
        return predictions
    
    def closest(self, row):  #Helper method
        bestdistance = euc(row, self.TrainingData[0])
        bestindex = 0
        for i in range(1, len(self.TrainingData)):
            dist = euc(row, self.TrainingData[0])
            if dist < bestdistance:
                bestdistance = distbestindex = i
        return self.TrainingTarget[bestindex]

def MarvellousKNeighbor():
    border = "*"*50

    iris = load_iris()
    data = iris.data
    target = iris.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID: %d, Lebel %s, Feature : %s" %(i, iris.data[i], iris.target[i]))
    print("Size of Training data set %d" %(i+1))

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)

    print(border)
    print("Training Data set")
    print(border)
    for i in range(len(data_test)):
        print("ID :%d, Lebel : %s, Feature : %s"%(i, data_test[i], target_test[i]))
    print("Size of Training Test  set %d" %(i+1))

    classifier = MarvellousKNN()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return  Accuracy

def main():

    Accuracy = MarvellousKNeighbor()
    print("Accuracy of Classiification algorithm with K Neighbor Classifier is ", Accuracy*100,"%")

if __name__ == "__main__":
    main()