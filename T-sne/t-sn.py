import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.manifold import TSNE
import pandas as pd
import seaborn as sns


def plot_tsne(features, labels):
    tsne = TSNE(n_components=2, init='pca', random_state=0)

    class_num = len(np.unique(labels))  # 类别数量
    tsne_features = tsne.fit_transform(features)  # 降维至2维
    print('tsne_features的shape:', tsne_features.shape)

    # 用 Pandas 创建 DataFrame
    df = pd.DataFrame()
    df["y"] = labels
    df["comp-1"] = tsne_features[:, 0]
    df["comp-2"] = tsne_features[:, 1]

    # 使用 Seaborn 进行可视化
    sns.scatterplot(x="comp-1", y="comp-2", hue="y",  # 这里直接传入 "y" 列
                    palette=sns.color_palette("hls", class_num),
                    data=df).set(title="T-SNE projection of digits data")
    plt.show()


if __name__ == '__main__':
    digits = datasets.load_digits(n_class=9)  # 加载数据集，限制为前5类
    features, labels = digits.data, digits.target
    print(features.shape)
    print(labels.shape)
    plot_tsne(features, labels)
