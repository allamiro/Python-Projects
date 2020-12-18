import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
bf_data = [['MC1', 1.16, 1, 1, 1, 1], ['MC2', 1.19, 1, 1, 1, 1], ['CVC1', 1, 0.86, 0.75, 0.71, 0.66],\
       ['CVC2', 1, 0.93, 0.71, 0.82, 0.65], ['CVC3', 1.01, 0.69, 0.53,0.41,0.38], ['A1', 1.46, 1, 1, 1, 1],\
     ['A2', 1.25, 1, 1, 1, 0.97], ['A3', 1.91, 1, 1, 1, 1], ['A4', 1.12, 1, 0.96, 1, 1] ]
bf_last = pd.DataFrame(bf_data, columns=["Sensor", "Ratio_BF", "ACC-BF-80-20", "ACC-BF-70-30", "ACC-BF-60-40", "ACC-BF-50-50"])
bf_last
sns.set_style("whitegrid")
boxplot = bf_last.boxplot(column=['Ratio_BF', 'ACC-BF-80-20', 'ACC-BF-70-30', 'ACC-BF-60-40','ACC-BF-50-50'], figsize=(8,6))
histplot = bf_last.hist(column=['Ratio_BF', 'ACC-BF-80-20', 'ACC-BF-70-30', 'ACC-BF-60-40'], figsize=(8,6))
boxplot = bf_last.boxplot(column=['Ratio_BF', 'ACC-BF-80-20'], by='Sensor', layout=(2, 1), figsize=(9,8))

bf_mcs = [['MC1', 1.16, 1, 1, 1], ['MC2', 1.19, 1, 1, 1]]
bf_allmcs = pd.DataFrame(bf_mcs, columns=["Sensor", "Ratio_BF", "ACC-BF-80-20", "ACC-BF-70-30", "ACC-BF-60-40"])
bf_allmcs
boxplot = bf_allmcs.boxplot(column=['Ratio_BF', 'ACC-BF-80-20'], figsize=(7,5))
bf_cvcs = [['CVC1', 1, 0.86, 0.75, 0.71],\
  ['CVC2', 1, 0.93, 0.71, 0.82], ['CVC3', 1.01, 0.69, 0.53,0.41]]
bf_allcvcs = pd.DataFrame(bf_mcs, columns=["Sensor", "Ratio_BF", "ACC-BF-80-20", "ACC-BF-70-30", "ACC-BF-60-40"])
bf_allcvcs
boxplot = bf_allcvcs.boxplot(column=['Ratio_BF', 'ACC-BF-80-20'], figsize=(7,5))

sns.boxplot(y = 'Ratio_BF', x = 'ACC-BF-50-50', data = bf_last)
sns.distplot(bf_allmcs['Ratio_BF'], hist=True, kde=True, 
          bins=int(18/5), color = 'red', 
   hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})

sns.distplot(bf_last['Ratio_BF'], hist=True, kde=True, 
           bins=int(18/5), color = 'blue', 
        hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
sns.distplot(bf_last['ACC-BF-50-50'], hist=True, kde=True, 
             bins=int(18/5), color = 'green', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
sns.distplot(bf_last['Ratio_BF'], hist=True, kde=True, 
             bins=int(18/5), color = 'blue', 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 4})
