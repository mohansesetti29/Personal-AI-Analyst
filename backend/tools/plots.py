import matplotlib.pyplot as plt
import seababorn as sns

def plot_distribution(df, column):
    plt.figure()
    sns.histplot(df[column].dropna(), kde=True)
    return plt
