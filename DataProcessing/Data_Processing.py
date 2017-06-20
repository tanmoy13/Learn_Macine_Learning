
# coding: utf-8

# In[ ]:

#Imporing Library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[5]:

#Importing Dataset
data_frame=pd.read_csv('/home/tanmoy/Desktop/MachineLearning/pima-data.csv')


# In[7]:

#Display the data set size row and col
data_frame.shape


# In[9]:

#display first 3 row of the dataset
data_frame.head(3)


# In[11]:

#display last 4 row of the dataset
data_frame.tail(4)


# In[13]:

#If there is any empty cell in dataset then isnull value is true otherwise false in this case we have no empty cell so every cell is False
data_frame.isnull()


# In[15]:

#This function returns an array of the result
data_frame.isnull().values


# In[19]:

#This function check if there is any empty cell in the data set or not
data_frame.isnull().values.any()


# In[31]:

#function for display the heatmap here yellow cell means the data in this cell are same diagonals are always same
def corr_heatmap(data_frame, size=11):
    correlation=data_frame.corr()
    fig, heatmap = plt.subplot(figsize=(size,size))
    heatmap.matshow(correlation)
    plt.xticks(range(len(correlation.columns)),correlation.columns)
    plt.yticks(range(len(correlation.columns)),correlation.columns)
    plt.show()


# In[34]:

#call the above funciton
corr_heatmap(data_frame)


# In[37]:

#here we delete the duplicate date col skin and preserve the thickness column 
del data_frame['skin']
data_frame.head()


# In[39]:

#This is the dataset heatmap after deleting the duplicate col skin
corr_heatmap(data_frame)


# In[41]:

data_frame.head()


# In[43]:

#Data Molding = Converting from True False to binary 0 or 1
map_diabetis={True:1,False:0}
data_frame['diabetes']=data_frame['diabetes'].map(map_diabetis)


# In[45]:

data_frame.head()


# In[46]:

#Checking True false Ratio
cnt_true=0.0
cnt_false=0.0
for item in data_frame['diabetes']:
    if(item==1):
        cnt_true+=1
    else:
        cnt_false+=1
percent_true=(cnt_true/(cnt_true+cnt_false))*100
percent_false=(cnt_false/(cnt_true+cnt_false))*100

print "Number of True cases: {0} ({1:2.2f}%)".format(cnt_true,percent_true)
print "Number of False cases: {0} ({1:2.2f}%)".format(cnt_false,percent_false)
        

