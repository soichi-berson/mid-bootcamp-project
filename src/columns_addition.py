import numpy as np
import pandas as pd

def add_columns(data:pd.DataFrame, year:str) -> None:
	'''
	This function add columns according to the year

	Input: 
	pd.DataFrame
	year


	'''

	#eu
	eu = pd.read_excel('../data/eu_countries.xlsx', engine="openpyxl")
	eu = eu[ eu['Name'].isna()==False ]
	data1 = data.copy()
	data1['is_EU'] = data1["country"].apply(lambda x: 'Yes' if x in eu.values else "No")

	
	#Englsih spoken
	# import the data
	english = pd.read_excel('../data/english_spoken.xlsx', engine="openpyxl")
	english_countries = english.iloc[0:44,0]
	data2 = data1.copy()
	data2['english_spoken'] = data2["country"].apply(lambda x: 'Yes' if x in english_countries.values else "No")

	#visa
	# import the data
	visa = pd.read_excel('../data/visa_requirement.xlsx', engine="openpyxl")
	data5 = data2.copy()
	data5['visa_requirement'] = data5["country"].apply(lambda x: 'Yes' if x in visa.values else "No")


	#commonwealth
	# import the data
	commonwealth = pd.read_excel('../data/commonwealth.xlsx', engine="openpyxl")
	data6 = data5.copy()

	# Convert the elements to strings
	commonwealth_array = np.array(commonwealth['Country'], dtype=str)

	# Remove spaces from the elements of the array
	commonwealth_array = np.char.strip(commonwealth_array)


	data6['commonwealth'] = data6["country"].apply(lambda x: 'Yes' if x in commonwealth_array else "No")




	#population
	# download the file
	population = pd.read_excel('../data/population1.xlsx', engine="openpyxl")
	# choose the data
	population1 = population.loc[:,['Country Name', year]]
	population1 = population1.rename(columns={'Country Name':'country', year:'population'})
	population1 = population1[ population1['population'].isna()==False ]
	population1['population'] = population1['population'].astype('int64')
	population1 = population1.reset_index(drop=True)
	#change the unit of population
	population3 = population1.copy()
	population3['population'] = round(population3['population']/1000000,2)

	data8 = data6.copy()

	merged_data =  pd.merge(data8,population3 , on='country', how='left')
	merged_data = merged_data.rename(columns={'population':'population_(m)'})


	#region and income
	# download the file
	region_income = pd.read_excel('../data/region_and_income.xlsx', engine="openpyxl")
	merged_data2 = merged_data.copy()

	#change the column names 
	region_income = region_income.rename(columns={'Country Name':'country', 'Region': 'region', 'IncomeGroup': 'income_group'})
	# add the data
	merged_data3 =  pd.merge(merged_data2,region_income , on='country', how='left')
	

	#GDP
	# download the file
	gdp = pd.read_excel('../data/GDP.xlsx', engine="openpyxl")
	# choose the data
	gdp1 = gdp.loc[:,['country', year]]
	gdp1 = gdp1.rename(columns={year:'gdp'})
	gdp1 = gdp1[ gdp1['gdp'].isna()==False ]
	gdp1['gdp'] = round(gdp1['gdp'],2)
	gdp1 = gdp1.reset_index(drop=True)


	merged_data4 = merged_data3.copy()


	# add the data
	merged_data5 =  pd.merge(merged_data4,gdp1 , on='country', how='left')


	#save the data
	name = '../data/data_' + year + '.csv' 
	merged_data5.to_csv(name, index=False)






