import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def test():
    df=pd.read_csv("../data/HR.csv")
    print(df.head())
    #sns.set()
    # spearman
    # kendall
    # data=df.corr("spearman")
    #plt.violinplot
    # ax=sns.heatmap(df,annot=True, vmax=1, square=True, cmap="Blues")
    # plt.show()
    plt.boxplot(df["spearman"])
    plt.show()

def drawheadmaptest():
    sns.set()
    np.random.seed(0)
    data= np.random.rand(10,12)
    print(data)
    ax=sns.heatmap(data,center=0)
    plt.show()



if __name__ == '__main__':
    test()
    #drawheadmaptest()