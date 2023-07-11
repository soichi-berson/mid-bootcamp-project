import pandas as pd

def remove_region(df:pd.DataFrame) -> pd.DataFrame:
	'''
	This function removes enexpected values(region) of the column: 'country' but only' total world' and 
	something of 'other--- ' are remained.

	Input:pd.DataFrame

	Output:pd.DataFrame  


	''' 
	df2 = df.copy()

	remove_regions = {'North America', 'North America', '- of which EU', '- of which EU15', '- of which EU Oth', 'Europe'}

	#for i in len(df):
	#	if df2['country'] in remove_regions:
	#		df2. 
	df2 = df2[~df2['country'].isin(remove_regions )]





	return df2




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













