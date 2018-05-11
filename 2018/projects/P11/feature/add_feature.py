# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime
import sys
import time

def user_click(beforesomeday):
	user_act_count = pd.croosstab([beforesomeday.user_id, beforesomeday.behavior_type], beforesomeday.hours, dropna = False)
	user_act_count = user_act_count.unstack(fill_value = 0)
	return user_act_count

def user_activeday(train_user_window1):
	user_act_day = train_user_window1.groupby(by = ['user_id', 'behavior_type']).agg({"daytime": lambda x:x.nunique()})
	user_act_day = user_live.unstack(fill_value = 0)
	return user_act_day

def user_item_click(beforesomeday):
	user_item_act_count = pd.croosstab([beforesomeday.user_id, beforesomeday.item_id, beforesomeday.behavior_type], beforesomeday.hours)
	user_item_act_count = user_item_act_count.unstack(fill_value = 0)
	return user_item_act_count

def user_cate_click(beforesomeday):
	user_cate_act_count = pd.croosstab([beforesomeday.user_id, beforesomeday.item_category, beforesomeday.behavior_type], beforesomeday.hours)
	user_cate_act_count = user_cate_act_count.unstack(fill_value = 0)
	return user_cate_act_count

def user_item_long_touch(train_user_window1):
	_active = train_user_window1.groupby(by = ['user_id', 'item_id']).agg({"daytime": lambda x:(x.max() - x.min()).days})
	return _active

def user_cate_lone_touch(train_user_window1):
	_active = train_user_window1.groupby(by = ['user_id', 'item_category']).agg({"datetime": lambda x:(x.max() - x.min()).days})
	return _active