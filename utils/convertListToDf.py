
import re
import numpy as np
import pandas as pd

def convert_list_to_df(table_data, item_to_remove, pattern_of_value):
    ## calculate number of row item
    # remove element in list which is not row label, save into list and text separately 
    # list used to remove number value to find row item, text used for regex
    row_item = [x for x in table_data if x not in item_to_remove]
    row_item_text = " ".join(x for x in table_data if x not in item_to_remove)
    # find number value of table
    value_to_remove = re.findall(pattern_of_value, row_item_text)
    # remove number value
    clean_row_item = [x for x in row_item if x not in value_to_remove]
    # count number of row item
    no_row_item = len(clean_row_item)

    # change the list into array, then into dataframe
    list_length = len(table_data)
    
    # number of row of a pivot table = columns labels + number of item in column field + grand total +  number item in row field
    # value of column label depend on wb.Sheets("pivot_table").PivotTables("example").DisplayFieldCaptions = True or False, if true column labels = 1, else = 0
    # you can use row to determine number of column for pivot table or vice versa, depend on which on you find easier
    # in this case we calculate number of row first, then calculate number of column
    row_df =  no_row_item
    column_df = int(list_length/row_df)
    
    # reshape list into array
    arr2D = np.reshape(table_data, (15, 2))
    df = pd.DataFrame(arr2D, columns=['Month', 'Volume'])
    df = df.drop(index = 0, axis=1)
    df = df.drop(index = 1, axis=1)
    df = df.iloc[:-1]
    return df