import pandas as pd

class PlayerDatabase:
    def __init__(self):
        self.df = None
        self.players = []
        self.columns = []
        self.count = 0

    def load_data(self, file_path):
        df = pd.read_csv(file_path)

        if "Unnamed: 0" in df.columns:
            df = df.drop(columns=["Unnamed: 0"])

        df["salary"] = df["salary"].fillna(0)
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
        df["displayHeight"] = pd.to_numeric(df["displayHeight"], errors="coerce")
        df["displayWeight"] = pd.to_numeric(df["displayWeight"], errors="coerce")

        self.df = df
        self.players = df.to_dict(orient="records")
        self.columns = list(df.columns)
        self.count = len(self.players)

        print("Dataset loaded successfully!")
        return df

    def show_head(self, n=5):
        return self.df.head(n)

    def show_tail(self, n=5):
        return self.df.tail(n)

    def show_info(self):
        return self.df.info()

    def show_row(self, idx):
        return self.df.iloc[idx]

    def search_by_name(self, name):
        name = name.lower()
        return [
            p for p in self.players
            if name in p["fullName"].lower()
        ]

    def filter_by_age(self, min_age, max_age):
        return [
            p for p in self.players
            if min_age <= p["age"] <= max_age
        ]

    def top_salaries(self, n=5):
        return self.df.sort_values("salary", ascending=False).head(n)

    def summary_statistics(self):
        return self.df.describe()
