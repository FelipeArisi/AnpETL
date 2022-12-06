from utils.convertListToDf import convert_list_to_df


class Pivot:
    def __init__(self, wb, range: str):
        self.table = wb.Sheets("Plan1").Range(range).PivotTable
        self._filters = []
        self._filter_itens = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def filters(self):
        page_range_item = []
        for i in self.table.PageRange:
            page_range_item.append(str(i))

        self._filters = page_range_item[0::2]
        return self._filters

    @property
    def getFilterItens(self):
        for filter in self.filters:    
            self._filter_itens[filter] = self.getItensColumn(filter)
        return self._filter_itens

    def getItensColumn(self, column):
        itens = []
        for item in self.table.PivotFields(column).PivotItems():
            product = str(item)
            itens.append(product) 
        return itens
    
    @property
    def tableData(self):
        table_data = []
        for i in self.table.TableRange1:
            #print(i)
            table_data.append(str(i))
        
        return table_data


    def setFilter(self, pivotField, currentPage):
        self.table.PivotFields(pivotField).CurrentPage = currentPage

    def clearFilter(self, pivotField):
        self.table.PivotFields(pivotField).ClearAllFilters()


    def excelToDf(self):
        pattern_of_value = r"\d+.?\d+"
        return convert_list_to_df(self.tableData, ['None'], pattern_of_value)
 
    def setVisibleColumns(self, column, visible):
        for item in self.table.PivotFields(column).PivotItems():
            year = str(item)
            if(year == visible):
                self.table.PivotFields(column).PivotItems(year).Visible = True  
            else:
                self.table.PivotFields(column).PivotItems(year).Visible = False 