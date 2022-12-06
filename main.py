import pandas as pd
from classes.excel import Excel
from classes.pivot import Pivot
from classes.transform import Transform

from pathlib import Path
from database.anp import DataBase
import re
from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

f_path = f"{Path.cwd()}\data"
f_name = 'vendas-combustiveis-m3.xls'
filename = f'{f_path}\{f_name}'


excel = Excel(filename)
pivot = Pivot(excel.wb, "B53")
transform = Transform(pivot)
db = DataBase()

df = transform.createDF('UN. DA FEDERAÇÃO', 'PRODUTO', 'ANO')

df.to_excel("output.xlsx")  
db.insert(df)


pivotDiesel = Pivot(excel.wb, "B133")
transformDiesel = Transform(pivotDiesel)
dfDiesel = transformDiesel.createDF('UN. DA FEDERAÇÃO', 'PRODUTO', 'ANO')
dfDiesel.to_excel("outputdfDiesel.xlsx")  