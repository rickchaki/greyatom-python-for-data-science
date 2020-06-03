# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status= data['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind= 'bar')


# Step 2
property_and_loan= data.groupby(['Property_Area','Loan_Status']).size().unstack()
#Plotting an unstacked bar plot
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis
plt.xticks(rotation=45)

# Step 3
#Plotting a stacked bar plot
education_and_loan= data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=False)


#Changing the x-axis label
plt.xlabel('Education Status')
plt.ylabel('Loan Status')

#Changing the y-axis label
plt.xticks(rotation=45)

#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate= data[(data['Education'] == 'Graduate')]

#Subsetting the dataframe based on 'Education' column
not_graduate= data[(data['Education'] == 'Not Graduate')]
print(not_graduate)
#Plotting density plot for 'Graduate'
graduate.plot(kind='density',label='Graduate')

#Plotting density plot for 'Graduate'
not_graduate.plot(kind='density',label='Not Graduate')

#For automatic legend display
plt.legend(labels=['Graduate', 'Not Graduate'])

# Step 5
#Setting up the subplots
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))

#Plotting scatter plot
ax_1= plt.scatter(data['ApplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title
plt.title('Applicant Income')

#Plotting scatter plot
ax_2= plt.scatter(data['CoapplicantIncome'],data['LoanAmount'])

#Setting the subplot axis title
plt.title('CoapplicantIncome')

#Creating a new column 'TotalIncome'
data['TotalIncome']= data['ApplicantIncome']+data['CoapplicantIncome']

#Plotting scatter plot
ax_3= plt.scatter(data['TotalIncome'],data['LoanAmount'])


#Setting the subplot axis title
plt.title('Total Income')


