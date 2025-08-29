# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
    
    def show_basic_info(self):
        print("Dataset Info:")
        print(self.data.info())
        print("\nFirst 5 rows:")
        print(self.data.head())
    
    def analyze_numerical_data(self):
        numerical_cols = self.data.select_dtypes(include=['int64', 'float64']).columns
        print("\nNumerical Data Analysis:")
        print(self.data[numerical_cols].describe())
    
    def create_visualizations(self):
        # Example: Correlation heatmap
        plt.figure(figsize=(10, 8))
        numerical_data = self.data.select_dtypes(include=['int64', 'float64'])
        sns.heatmap(numerical_data.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.savefig('correlation_heatmap.png')
        plt.close()

# Usage example:
# analyzer = DataAnalyzer('your_dataset.csv')
# analyzer.show_basic_info()