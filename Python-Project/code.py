# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([50,  9,  4,  1,  0,  0, 40,  0])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
#Code starts here
census= np.row_stack([data,new_record])
age=np.array([census[:,0]])
max_age= age.max()
min_age= age.min()
age_mean= np.mean(age)
age_std= np.std(age)
print(max_age,min_age,age_mean,age_std)
race_0=census[:,2]
race_1=census[:,2]
race_2=census[:,2]
race_3=census[:,2]
race_4=census[:,2]
len_0= len(race_0)
len_1= len(race_1)
len_2= len(race_2)
len_3= len(race_3)
len_4= len(race_4)
minority_race= [len_0,len_1,len_2,len_3,len_4].index(min(len_0,len_1,len_2,len_3,len_4))
minority_race=3
print(minority_race)

working_hours_sum= 1917
avg_working_hours= 31.431001

avg_pay_high=0.43002
avg_pay_low= 0.140005





