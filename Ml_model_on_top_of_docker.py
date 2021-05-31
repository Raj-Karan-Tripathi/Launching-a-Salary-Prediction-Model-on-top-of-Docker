import pandas as pd   
sal = pd.read_csv('SalaryData.csv')       
x = sal['YearsExperience'].values.reshape(30,1)        
y = sal['Salary']
from sklearn.linear_model import LinearRegression
salmodel = LinearRegression()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
salmodel.fit(X_train , y_train)
def sal_predict():
	exp_years = float(input("Enter your experience in years:"))
	sal_predict = salmodel.predict([[exp_years]])
	print("The salary for the submitted years of experience is : ",sal_predict)
while True:
    choice = input("\n Please type  'Start' to continue to prediction or type 'leave' to end  the prediction: ")
    if choice == "Start":
	    sal_predict()
    elif choice == "leave":
	    print("Bye")
	    break
    else:
	    print("\n Please re enter the input")