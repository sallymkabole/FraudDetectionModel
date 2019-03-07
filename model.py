import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json
import numpy as np
from flask import Flask, request, jsonify
import pickle

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report


balance=11111.32
print("    ATM    ")
print("""
1)        Balance
2)        Withdraw
3)        Deposit
4)        Quit


""")
Option=int(input("Enter Option: "))

if Option==1:
    print("Balance  ksh ",balance)


if Option==2:
    print("Balance  ksh  ",balance)
    Withdraw=float(input("Enter Withdraw amount ksh "))
    if Withdraw>0:
    	if Withdraw<balance:
    		data = pd.read_csv('pandas.csv')
    		print("Total rows and columns\n\n",data.shape,"\n")
    		#Dependent and independent variable
    		X = data.iloc[:, 1:2].columns
    		y = data['Class']
    		X = data[X]
    		#total count in each class
    		count = data['Class'].value_counts()
    		print("Total count in each class\n\n",count)
    		print("\n")
    		#splitting the data
    		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    		#Build the model
    		clf = LogisticRegression()
    		# Train the classifier
    		clf.fit(X_train, y_train)
    		#test the model
    		y_pred = clf.predict(X_test)
    		#classification report
    		cr = (classification_report(y_test, y_pred))
    		#confusion matrix
    		cm = (metrics.confusion_matrix(y_test, y_pred))
    		print("Confusion Matrix:\n\n",cm,"\n")
    		#classification report
    		print(classification_report(y_test, y_pred))
    		#Accuracy score
    		a= (metrics.accuracy_score(y_test, y_pred))
    		print("Accuracy score:",round(a,1))
    		#print the actual and predicted labels
    		df1 = pd.DataFrame({'Actual':y_test, 'Predicted': y_pred})
    		print(df1.head(13))
    		# Saving model to disk
    		pickle.dump(clf, open('model.pkl','wb'))
    		# Loading model to compare the results
    		model = pickle.load( open('model.pkl','rb'))
    		t= model.predict([[int(Withdraw)]])
    		print (t)
    		if t== 0:
    			print("Transaction Declined")
    		else:
    			print("Transaction Successful")
    	else:
    		print("Insufficient funds")
    else:
    	print("Cannot Withdraw negative")


if Option==3:
    print("Balance  ksh ",balance)
    Deposit=float(input("Enter deposit amount ksh "))
    if Deposit>0:
        forewardbalance=(balance+Deposit)
        print("Forewardbalance  ksh ",forewardbalance)
    else:
        print("None deposit made")


if Option==4:
    exit()
