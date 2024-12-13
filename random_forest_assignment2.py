from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

digits=load_digits()
X=digits.data
Y=digits.target

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

model= RandomForestClassifier(n_estimators=200, max_depth=5,random_state=42)
model.fit(X_train, Y_train)

Y_pred=model.predict(X_test)

print(classification_report(Y_test,Y_pred))
print(confusion_matrix(Y_test,Y_pred))