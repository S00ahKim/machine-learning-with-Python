import numpy as np
from scipy import stats
import collections
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import scipy as sp
import pandas as pd
import pylab 
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqline
from numpy import dot
from numpy.linalg import norm
from sklearn.preprocessing import minmax_scale

# 1.
data = np.array([13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70])

# (a)
print(len(data))
print("%0.2f" % np.mean(data))
print("%0.2f" % np.median(data))

# (b)
m = stats.mode(data)
print(m)

counter=collections.Counter(data)
print(counter)

def get_mode(list):
    o = collections.Counter(list).most_common()
    max,m = o[0][1],[]
    for num in o:
        if num[1] == max:m.append(num[0])
    if len(m)==len(list):return '없음'
    return m
print(get_mode(data))

# modality - i
labels, values = zip(*Counter(data).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

# modality - ii
age = np.array([10, 20, 30, 40, 50, 60, 70])
d_frq = np.array([5, 9, 8, 3, 1, 0, 1])

plt.bar(age, d_frq, color="blue")
plt.show()

# (c)
lower_data = data[0:13]
upper_data = data[14:27]

Q1 = np.median(lower_data)
Q3 = np.median(upper_data)
print(Q1, Q3)

print("Q1 quantile of arr : ", np.quantile(data, .25)) 
print("Q3 quantile of arr : ", np.quantile(data, .75)) 

# (d)
sp.stats.describe(data) #간단한 기술통계
pdata = pd.Series(data)
print(pdata.describe()) #five number summary

print(np.percentile(data, 25, interpolation='nearest')) #1분위수 (보간법 적용)
print(np.percentile(data, 75, interpolation='nearest')) #3분위수 (보간법 적용)

# (e)
plt.boxplot(data)
plt.show()

#########################################################

# 2.

sum = 200+450+300+1500+700+44
print(sum)
print(sum/2)

print(200+450+300)

print(20+((sum/2-950)/1500)*30)

#########################################################

# 3. 

# (a)

age = np.array([23, 23, 27, 27, 39, 41 , 47 , 49 , 50, 52 , 54 , 54 , 56 , 57 , 58 , 58 , 60 , 61])
fat = np.array([9.5 ,26.5 ,7.8 ,17.8 ,31.4 ,25.9 ,27.4 ,27.2 ,31.2, 34.6 ,42.5 ,28.8 ,33.4 ,30.2 ,34.1 ,32.9 , 41.2 ,35.7])

page = pd.Series(age)
pfat = pd.Series(fat)

print(page.describe())
print(pfat.describe())

print(np.std(age))
print(np.std(fat))

# (b)

plt.boxplot(age)
plt.show()

plt.boxplot(fat)
plt.show()

# (c)

plt.scatter(age, fat, c="green", alpha=0.5)
plt.show()

stats.probplot(age, dist="norm", plot=pylab)
stats.probplot(fat, dist="norm", plot=pylab)
pylab.show()

ax = plt.subplot(111)
plt.scatter(age, fat)
qqline(ax, 'r', age, fat)
plt.show()

#########################################################

# 4. 

# (a)
def cos_sim(A, B):
       return dot(A, B)/(norm(A)*norm(B))

print (cos_sim((1.5, 1.7),(1.4, 1.6)))
print (cos_sim((2.0,1.9),(1.4, 1.6)))
print (cos_sim((1.6, 1.8),(1.4, 1.6)))
print (cos_sim((1.2, 1.5),(1.4, 1.6)))
print (cos_sim((1.5, 1.0),(1.4, 1.6)))

# (b)
print((1.5, 1.7)/norm((1.5, 1.7)))
print((2.0,1.9)/norm((2.0,1.9)))
print((1.6, 1.8)/norm((1.6, 1.8)))
print((1.2, 1.5)/norm((1.2, 1.5)))
print((1.5, 1.0)/norm((1.5, 1.0)))
print((1.4, 1.6)/norm((1.4, 1.6)))

def ecld_distance(a):
    return np.sqrt((np.abs(a[0]-0.65850461)**2)+(np.abs(a[1]-0.75257669)**2))

print(ecld_distance([0.66162164, 0.74983786]))
print(ecld_distance([0.72499943, 0.68874946]))
print(ecld_distance([0.66436384, 0.74740932]))
print(ecld_distance([0.62469505, 0.78086881]))
print(ecld_distance([0.83205029, 0.5547002]))

#########################################################

# 5. 

# (a)
dataset = np.array([200, 300, 400, 600, 1000])

# 함수 사용
print(minmax_scale(dataset))

# 공식으로 구하기
nrm_arr = []
def min_max_normalization(arr):
    for i in range(len(arr)):
        nrm_arr.append((arr[i]-200)/(1000-200))
        
min_max_normalization(dataset)
print(nrm_arr)

# (b)
z_arr = []
ds_mean = np.mean(dataset)
ds_std = np.std(dataset)

def z_score(arr):
    for i in range(len(arr)):
        x=(arr[i]-ds_mean)/ds_std
        z_arr.append("%0.2f" % x)
        
z_score(dataset)
print(z_arr)

#########################################################

# 6.

# (a)
z_age=[]
ag_mean = np.mean(age)
ag_std = np.std(age)

def z_score_age(arr):
    for i in range(len(arr)):
        x= (arr[i]-ag_mean)/ag_std
        z_age.append("%0.2f" % x)
        
z_score_age(age)
print(z_age)

z_fat=[]
f_mean = np.mean(fat)
f_std = np.std(fat)

def z_score_fat(arr):
    for i in range(len(arr)):
        x= (arr[i]-f_mean)/f_std
        z_fat.append("%0.2f" % x)
        
z_score_fat(fat)
print(z_fat)

# (b)

comp = pd.DataFrame({
    "age" : [23, 23, 27, 27, 39, 41 , 47 , 49 , 50, 52 , 54 , 54 , 56 , 57 , 58 , 58 , 60 , 61],
    "fat" : [9.5 ,26.5 ,7.8 ,17.8 ,31.4 ,25.9 ,27.4 ,27.2 ,31.2, 34.6 ,42.5 ,28.8 ,33.4 ,30.2 ,34.1 ,32.9 , 41.2 ,35.7]
})

print(comp.corr(method="pearson"))
print(comp.cov())