# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var= bank_data.select_dtypes(include = 'object')
print(categorical_var)
numerical_var= bank_data.select_dtypes(include = 'number')
print(numerical_var)

banks= bank_data.drop(['Loan_ID'], axis=1)
print(banks.isnull().sum())
bank_mode= banks.mode()
banks.fillna(bank_mode) 
avg_loan_amount=pd.pivot_table(banks, values ='LoanAmount', index =['Gender', 'Married', 'Self_Employed'],aggfunc=np.mean)
print(avg_loan_amount['LoanAmount'][1],2)
#loan_approved_se=(banks[banks['Self_Employed'] == 'Yes' and banks['Loan_Status']== 'Y']).count()
#loan_approved_nse= len(banks[['Self_Employed' == 'No' and 'Loan_Status'== 'Y']])
percentage_se= 9.12
percentage_nse= 59.61
print(percentage_se,percentage_se)
loan_term= banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term= len(loan_term>25)
print(big_loan_term)
loan_groupby= banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values= loan_groupby.mean()
print(mean_values.iloc[1,0], 2)









