import pandas as pd
import matplotlib.pyplot as plt
class Analyzes:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = None   # we will load the dataframe here later
    def load_data(self):
        """Loads the CSV dataset."""
        try:
            self.df = pd.read_csv(self.file_name)
            print("Dataset loaded successfully.")
        except Exception as e:
            print("Error loading dataset:", e)
    def analyze_data(self):
        if self.df is None: #to make sure that the data is loaded
            print("Data not loaded yet!")
            return
        print("FIRST ROWS:")
        print(self.df.head())
        print("INFO:")
        print(self.df.info())
        print("DESCRIBE:")
        print(self.df.describe(include='all'))
        print("MISSING VALUES:")
        print(self.df.isna().sum())
    def plot_data(self):
        """Create basic visualizations using Matplotlib."""
        if self.df is None:
            print("Data not loaded yet!")
            return

        # 1. BAR CHART: Total Sales by Category
        if 'Category' in self.df.columns:
            sales_by_category = self.df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
            plt.figure(figsize=(10, 6))
            plt.bar(sales_by_category.index, sales_by_category.values, color='cornflowerblue')
            plt.title('Total Sales by Product Category', fontsize=14, fontweight='bold')
            plt.xlabel('Product Category', fontsize=12)
            plt.ylabel('Total Sales ($)', fontsize=12)
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.4)
            plt.show()

        # 2. SCATTER PLOT: Profit vs Discount
        if 'Discount' in self.df.columns and 'Profit' in self.df.columns:
            plt.figure(figsize=(8, 6))
            plt.scatter(
                self.df['Discount'],
                self.df['Profit'],
                color='purple',
                alpha=0.6,
                edgecolors='black',
                s=60)
            plt.title('Profit vs Discount', fontsize=14, fontweight='bold')
            plt.xlabel('Discount (%)', fontsize=12)
            plt.ylabel('Profit ($)', fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.4)
            plt.show()

# USING THE CLASS
analysis = Analyzes("DATA_SET.csv")
analysis.load_data()
analysis.analyze_data()
analysis.plot_data()