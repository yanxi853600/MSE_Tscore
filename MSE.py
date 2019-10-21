#(10/9-homework_7107029258_林彥希)
#1. 樣本集當母體 2.找出3個欄位 3. 對欄位進行抽樣 4. 做區間估計&T-檢定

#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from scipy import stats
import math

#download dataset
avocado=pd.read_csv("avocado.csv")

df=pd.DataFrame([avocado["Total Volume"],
               avocado["Total Bags"],
               avocado["AveragePrice"],
                avocado["Small Bags"],
                avocado["Large Bags"],
                avocado["XLarge Bags"]]).T

#大樣本區間估計
population = []
for x in range(18249):
    Sample=df.sample(n=3,axis=1)
    
    population.append(Sample.mean())
#print("母體平均:", sum(population)/18249.0)
  
Sample_size = 100
#Sample = np.random.choice(a=population, size=Sample_size)    


Sample_mean = Sample.mean()
print("樣本平均:", Sample_mean)
Sample_stdev = Sample.std()
print("樣本標準差:", Sample_stdev)
sigma = Sample_stdev/math.sqrt(Sample_size-1)
print("樣本計算出的母體標準差:", sigma)
z_critical = stats.norm.ppf(q=0.975)
print("Z分數:", z_critical)
margin_of_error = z_critical * sigma
confidence_interval = (Sample_mean - margin_of_error,
                       Sample_mean + margin_of_error)
#print(confidence_interval)
conf_int = stats.norm.interval(alpha=0.95,                 
                               loc=Sample_mean, 
                               scale=sigma)
print("區間估計: ",conf_int[0], conf_int[1])


#T檢定
population_mean = 18249 #母體平均

Sample_size = len(Sample)
Sample_mean = Sample.mean()
#print("樣本平均:", Sample_mean)
Sample_stdev = Sample.std()
#print("樣本標準差:", Sample_stdev)
sigma = Sample_stdev/math.sqrt(Sample_size-1)
#print("樣本計算出的母體標準差:", sigma)
t_obtained = (Sample_mean-population_mean)/sigma
print("檢定統計量:", t_obtained)
#print(stats.ttest_1samp(a=Sample, popmean=population_mean))

t_critical = stats.t.ppf(q=0.975, df=Sample_size-1)
print("t分數:", t_critical)

