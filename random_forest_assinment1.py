from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris=load_iris()
X=iris.data
Y=iris.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

model= RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train, Y_train)

Y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score
print("accuracy:",accuracy_score(Y_test,Y_pred))
