# -*- coding: utf-8 -*-
"""
mar 6 2023

@author: mauspad
"""
print("This script loops over every csv in the data directory. IF YOU GET AN ERROR, CHECK TO SEE IF THE CSV IS BUGGED. Score is total correct for relational change trials")

#import packages
import pandas as pd
import glob

#set directory
path = "data/*.csv"
for fname in glob.glob(path):

	# turn csv into dataframe
	df = pd.read_csv(fname)
	key_resp = []

	# list all key responses
	block2 = df.dropna(subset=["block2_response.corr"])
	block4 = df.dropna(subset=["block4_response.corr"])
	block6 = df.dropna(subset=["block6_response.corr"])
	block8 = df.dropna(subset=["block8_response.corr"])
	key_resp2 = block2["block2_response.corr"].tolist()
	key_resp4 = block4["block4_response.corr"].tolist()
	key_resp6 = block6["block6_response.corr"].tolist()
	key_resp8 = block8["block8_response.corr"].tolist()
	key_resp = key_resp2 + key_resp4 + key_resp6 + key_resp8

	#sum the correct answers
	Score = sum(key_resp)
	print(fname)
	print(Score)
	