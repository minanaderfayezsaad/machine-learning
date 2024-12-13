from sklearn import svm
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
digits=load_digits()
X=digits.data
Y=digits.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

clf=svm.SVC(kernel="linear")

clf.fit(X_train,Y_train)

Y_pred=clf.predict(X_test)
print("accuracy:",clf.score(X_test,Y_test))