
import win32com.client as win32

class Excel:
    def __init__(self, filename: str):
        # create excel object
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        # excel can be visible or not
        excel.Visible = False  # False
        excel.ScreenUpdating = False
        excel.DisplayAlerts = False
        excel.EnableEvents = False
        self._wb = excel.Workbooks.Open(filename)  

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._wb.Close()
        self.close()


    @property
    def wb(self):
        return self._wb

