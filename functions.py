import pandas as pd

def load_data(data):
    df = pd.read_csv(data)
    head = df.head()
    shape = df.shape
    describe = df.describe()

    output = {
        "head": head,
        "shape": shape,
        "describe": describe
    }

    return output

class DataPreparation:
    def __init__(self, data):
        self.df = pd.read_csv(data)

    def check_duplicates(self):
        return self.df.duplicated().sum()
    
    def remove_outliers_zscore(self):
        """
        Takes in a dataframe and removes outliers from the dataframe using Z-score method.
        """
        z_scores = np.abs(stats.zscore(self.df.select_dtypes(include=[np.number])))
        
        # Identify rows with any Z-score greater than the threshold
        outliers = (z_scores > 3).any(axis=1)
        
        # Remove outliers from the dataframe
        df_cleaned = self.df[~outliers]
        
        return df_cleaned

    def outlier_plot(self):
        """
        Plots boxplots to visualize outliers in the dataset.
        """
        # List of columns for the first boxplot
        cols1 = ["account length", "total day minutes", "total day calls",
                "number vmail messages",
                "total eve minutes", "total eve calls", "total night minutes",
                "total night calls"]
        cols2 = ["total intl minutes", "total intl calls", "customer service calls"]

        # Create a figure with one row and two columns
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

        # Create a boxplot for the first subset of columns in the first column
        sns.boxplot(data=self.df[cols1], ax=axes[0])
        axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=90)

        # Create a boxplot for the second subset of columns in the second column
        sns.boxplot(data=self.df[cols2], ax=axes[1])
        axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=90)

        # Setting the figure title
        fig.suptitle("Boxplots for different subsets of columns")

        # Show the plot
        plt.show()



