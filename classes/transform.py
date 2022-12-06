from classes.pivot import Pivot 
import pandas as pd
import re
from datetime import datetime
import locale

class Transform:
    def __init__(self, pivot: Pivot):
        self.pivot = pivot
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 


    def createDF(self, uf: str, product: str, year: str):
        filtersItens = self.pivot.getFilterItens
        years = self.pivot.getItensColumn(year)

        df = pd.DataFrame([])
        self.pivot.clearFilter(year)
        self.pivot.clearFilter(uf)
        self.pivot.clearFilter(product) 
        for i in filtersItens[uf]:
            for j in filtersItens[product]:
                for y in years:
                    self.pivot.setFilter(uf, i)
                    self.pivot.setFilter(product,  j)
                    self.pivot.setVisibleColumns(year, y)
                    aux = self.pivot.excelToDf()
                    aux[year] = y
                    aux[uf] = i
                    aux[product]  = j
                    df = pd.concat([df, aux], axis=1)
                    self.pivot.clearFilter(year)

        df.Month = df.Month.apply(lambda x : datetime.strptime(x, '%B').month) 
        #df['Date'] = list(zip(df.ANO, df.Month))
        df['Date'] = df.ANO + '-' +  df.Month.astype(str)

        regex = '\(.*?\)'
        df['Unit'] = df.PRODUTO.apply(lambda x : re.findall(regex,x)[0].replace('(', '').replace(')', '') )
        df[product]  = df.PRODUTO.apply(lambda x : re.sub(regex, '',x)) 

        df = df[['Volume', uf, product,  'Date', 'Unit']]

        df.rename(columns={'Volume': 'volume', uf: 'uf', product:  'product', 'Date': 'year_month', 'Unit': 'unit'}, inplace=True)

        return df
