
# coding: utf-8

# In[1]:


from __future__ import division
import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Constants define
ROOT_PATH = '/home2/sj/pycharm/2018-Tencent-Lookalike-master/2018-Tencent-Lookalike-master/data/'


# In[ ]:


########################################### Helper function ###########################################


# In[3]:


def log(info):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' ' + str(info))


# In[4]:


def transform_data():
    user_feature_data = []
    with open(ROOT_PATH + 'userFeature.data', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip().split('|')
            user_feature_dict = {}
            for group in line:
                group_list = group.split(' ')
                user_feature_dict[group_list[0]] = ' '.join(group_list[1:])
            user_feature_data.append(user_feature_dict)
            if i % 100000 == 0:
                log('Progress: ' + str(i))
        user_feature = pd.DataFrame(user_feature_data)
        user_feature.to_csv(ROOT_PATH + 'userFeature.csv', index=False)


# In[ ]:


########################################### Transform data ###########################################


# In[5]:


transform_data()

