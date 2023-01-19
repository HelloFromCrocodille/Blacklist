import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

def countPlot(columns, data):
    """ Count how many appearance an unique data in a certain columns
    """
    ax = sns.countplot(col, data=data)