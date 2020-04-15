import pandas as pd 


class TrainingDataProcessor:
    """Preprocessing raw data for neural network training
    - comment1
    - comment2
    - comment3
    """
    def __init__(self):
        self.data = []
    
    @staticmethod
    def preprocessed_data(df_numerical_data):
        """Preprocess data"""
        
        print("Preparing input data for training the neural net.")
        
        print(df_numerical_data.head())
        print("Rows:", df_numerical_data.shape[0], "Column:", df_numerical_data.shape[1])

        #total = data_df.isnull().sum().sort_values(ascending = False)
        print(df_numerical_data.isnull().sum())