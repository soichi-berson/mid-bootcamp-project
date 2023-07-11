
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def create_histograms(dataframe):
    # Set the figure size
    plt.figure(figsize=(16, 16))
    
    # Get the column names of the dataframe
    columns = dataframe.columns
    
    # Calculate the number of rows and columns for subplots
    n_rows = len(columns) // 3 + (len(columns) % 3 > 0)
    n_cols = 3
    
    # Create subplots
    for i, column in enumerate(columns):
        plt.subplot(n_rows, n_cols, i+1)
        sns.histplot(data=dataframe[column])
        #plt.title(column)
    
    # Adjust the layout
    plt.tight_layout()
    
    # Show the plot
    plt.show()





def detect_outliers_zscore(df: pd.DataFrame, column: str, threshold: int=3) ->list:
    '''
    This function checks a column of a given Pandas DataFrame, computes the z-score
    of every value, and flags the value as "outlier" if it's values is outside the
    [-3,3] range.

    Input:
    df: Pandas DataFrame

    Output:
    Python list of indexes for values which are outliers.
    '''

    df2 = df.copy()
    outliers = []

    df2['abs-z-score'] = np.abs( ( df2[column] - df2[column].mean() ) / df2[column].std(ddof=1) )

    outliers = df2[ df2['abs-z-score'] > threshold ].index.tolist()
    
    

    return outliers





def create_countplots(df: pd.DataFrame)->None:
    '''
    This function creates a seaborn countplot of each categorical column.
    
    Input: pd.DataFrame
    output: None
    
    '''
    df2 = df.copy()
    # Get the categorical column names
    categorical = df2.select_dtypes('object')
    
    # Set the figure size
    plt.figure(figsize=(8, 8))
    
    # Iterate over categorical columns
    for column in categorical.columns:
        # Determine the count of unique values in the column
        unique_values = df2[column].nunique()

        # Set the orientation of countplot based on cardinality
        if unique_values >= 6:
            orientation = 'horizontal'
            sns.countplot(data=df2, y=column, order=df2[column].value_counts().index, orient=orientation)
        else:
            orientation = 'vertical'
            sns.countplot(data=df2, x=column, order=df2[column].value_counts().index, orient=orientation)


        # Set title
        plt.title(f'Countplot of {column}')
       

        # Show the plot
        plt.tight_layout()
        plt.show()
    
    