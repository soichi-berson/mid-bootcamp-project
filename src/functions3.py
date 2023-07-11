import numpy as np
import pandas as pd
visit = pd.read_csv('../data/cleaned_number_of_visitors.csv')
spending = pd.read_csv('../data/cleaned_spending_per_day.csv')
stay = pd.read_csv('../data/cleaned_length_of_stay.csv')
#ata = pd.concat([visit['country'], visit['2022'],spending['2022'], stay['2022']], axis=1)

def remove_total_other(df:pd.DataFrame) -> pd.DataFrame:
	'''
	This function removes total world and something of 'other --' ', but other china is remained.

	Input:pd.DataFrame

	Output:pd.DataFrame  


	''' 
	df2 = df.copy()

	remove_regions = {'Total World', 'Other Countries', 'Rest of the World', 'Other Central & Sth. America', 
	'Other Caribbean', 'Other Africa' 'Other North Africa', 'Rest of Europe' , 'Other Middle East', 'Other North Africa', 'Other Asia'}

	remove2 = {'Other Africa'}

	#for i in len(df):
	#	if df2['country'] in remove_regions:
	#		df2. 
	df2 = df2[~df2['country'].isin(remove_regions )]
	df2 = df2[~df2['country'].isin(remove2 )]





	return df2

def creating_data(year:str):
	'''
	This function creates the data of year

	'''
	data = pd.concat([visit['country'], visit[year],spending[year], stay[year]], axis=1)
	a = year

	b = 'number_of_visit_'+a
	c = 'spending_per_day_'+ a
	d = 'length_of_stay_'+ a
	data.columns = ['country','number_of_visit_'+a, 'spending_per_day_'+ a, 'length_of_stay_'+ a]



	e = 'total_' + year + '_(m)'
	data[e] = data[b]*1000*data[c]*data[d]

	data2 = data.copy()
	data2[e] = data2[e]// 1000000

	#change the unit 
	#data2[e] = data2[e].astype('int64')
	data2[e] = pd.to_numeric(data2[e], errors='coerce').astype('Int64')
	#change the column name 

	name = '../data/visit_spending_length_total' + year + '.csv' 

	data2.to_csv(name, index=False) 





	

	df = data2.copy()
	df = remove_total_other(df)
	data4 = df.reset_index(drop=True)


	# Other china and HongKong is combined. 
	df4 = data4.copy()

	# combine the numerical values
	visit_china = df4.iloc[36,1] + df4.iloc[37,1]
	spend_china = (df4.iloc[36,1]*df4.iloc[36,2] + df4.iloc[37,1]*df4.iloc[37,2])/visit_china  #average
	length_china = (df4.iloc[36,1]*df4.iloc[36,3] + df4.iloc[37,1]*df4.iloc[37,3])/visit_china  #average
	total_china = df4.iloc[36,4] + df4.iloc[37,4]
	china = {'country': ['China'] }


	new_row = pd.DataFrame({'country': 'China',
           b: visit_china ,
           c: round(spend_china,2) ,
          d: int(round(length_china,0)),
          e: total_china},index=[len(df4)])


	# Append the new row to the DataFrame
	df4 = pd.concat([df, new_row])
	df4 = df4.reset_index(drop=True)

	#remove 'Hong Kong' and 'other China'
	data5 = df4.copy()
	data5 = data5.drop(data5[data5['country'].isin(['Hong Kong (China)', 'Other China'])].index)
	data5 = data5.reset_index(drop=True)

	name = '../data/V_S_L_T_by_country' + year + '.csv' 
	data5.to_csv(name, index=False) 

	print("finished")
	



	



