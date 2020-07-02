#!/usr/bin/env python

#/mnt/c/Users/dhanu/Documents/EcoData
#source env/bin/activate


import pandas as pd
import numpy as np
import os



#Read in the original file - change directory name to yours with the csv file in it
contaminant_data = pd.read_csv("/mnt/c/Users/dhanu/Documents/EcoData/input/UMCR4_All_MichiganOnlyData.csv" , encoding = "ISO-8859-1")
#only for ucmr 4 formatting
contaminant_data = contaminant_data.rename(columns={"AnalyticalResultValue(µg/L)":"AnalyticalResultValue"})



#Uncomment below code to only select for the rows for Michigan
#contaminant_data = contaminant_data[contaminant_data.State.str.contains("MI")]


#Remove the extraneous columns we don't need
#UCMR2
#contaminant_data = contaminant_data.drop(['Size', 'FacilityName','SamplePointName', 'SamplePointType', 'MethodID', 'MonitoringRequirement', 'SampleEventCode', 'DisinfectantType'], axis=1)
#UCMR3
#contaminant_data = contaminant_data.drop(['Size', 'FacilityName','SamplePointName', 'SamplePointType', 'MethodID', 'MonitoringRequirement', 'SampleEventCode'], axis=1)
#UCMR4
contaminant_data = contaminant_data.drop(['Size', 'FacilityName','SamplePointName', 'SamplePointType', 'MethodID', 'MonitoringRequirement', 'SampleEventCode'], axis=1)





#create a new dataframe that only has values of contaminants over significance level
new_data = contaminant_data[~contaminant_data.AnalyticalResultsSign.str.contains("<" , na=False)]





#read in the zipcodes to a dataframe - change directory name to yours with the csv file in it
#ucmr 2+3
#zipcodes = pd.read_csv('/mnt/c/Users/dhanu/Documents/EcoData/input/UCMR3_ZipCodes_Excel.csv')
#ucmr 4
zipcodes = pd.read_csv('/mnt/c/Users/dhanu/Documents/EcoData/input/UCMR4_ZipCodes_csv.csv')




#connect the zipcodes to our previous dataframe
full_data=pd.merge(new_data,zipcodes, on='PWSID', how="inner")




#Uncomment the below code to grab singular contaminants
#PFAS_triggers = ["PFOS", "PFOA", "PFNA", "PFHxS", "PFHpA", "PFBS"]
#full_data = full_data[full_data["Contaminant"].isin(PFAS_triggers)]



#generate the counts of each contaminant
counts = full_data.groupby(['Contaminant']).count()




#Uncomment the code to generate the counts of each state
#state_counts = full_data.groupby(['State']).count()


#change directory to ouput folder for  csv
os.chdir('/mnt/c/Users/dhanu/Documents/EcoData/output/')


#Save your full data as well as the counts into their own csv files
full_data.to_csv('Michigan_UCMR4.csv')
counts.to_csv('Michigan_UCMR4_counts.csv')
#state_counts = ('Full_UCMR3_state_counts.csv')