import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def countPlot(columns : pd.Series, data : pd.DataFrame, title : str):
    """_summary_

    Args:
        columns (pd.Series): Certain column for counting
        data (pd.DataFrame): Dataframe
        title (str): Plot title

    >>> 
    """
    ax = sns.countplot(col, data=data)
    ax.set_title(title)