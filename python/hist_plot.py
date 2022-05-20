import pandas as pd
import matplotlib.pyplot as plt


def hist_plot(df, target_column:str):
    df_np = df[target_column].to_numpy()
    df_counts = np.unique(df_np, return_counts=True)
    fig, ax = plt.subplots(1, 1)
    plt.bar(df_counts[0], df_counts[1])
    # ax.hist(df[target_column])
    ax.set_title(target_column)
    ax.set_xticks(df_counts[0])

    rects = ax.patches
    labels = ["%d" % i for i in range(len(rects))]

    for rect, label in zip(rects, df_counts[1]):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
                ha='center', va='bottom')
    # plt.legend()
    plt.show()
