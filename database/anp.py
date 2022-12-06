from sqlalchemy import create_engine

class DataBase:
    def __init__(self):
        self.engine = create_engine('sqlite:///anp.db')

    def insert(self, df):
        with self.engine.connect().execution_options(autocommit=True) as conn:
            print(df.to_sql('anp', con=conn, if_exists='append', index= False))