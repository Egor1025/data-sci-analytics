import pandas as pd


class DataFrameExporter:
    def __init__(self, df, path):
        self.df = df
        self.path = path

    def to_json(self):
        self.df.to_json(self.path, orient='records', force_ascii=False, indent=4)

    def to_csv(self):
        self.df.to_csv(self.path, index=False, sep='|')

    def to_excel(self):
        self.df.to_excel(self.path, index=False)