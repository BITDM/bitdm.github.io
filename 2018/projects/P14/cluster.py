# -*- coding: utf-8 -*
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from PIL import Image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
from matplotlib._png import read_png

IMG_SIZE = 120

data_path = '../CBIR_dataset/mirflickr'

def io(path):
    img = Image.open(path)
    width, height = img.size
    size = np.minimum(width, height)
    stx = int((width - size) / 2)
    sty = int((height - size) / 2)
    img = img.crop((stx, sty, stx + size, sty + size))
    img = img.resize((IMG_SIZE, IMG_SIZE))
    data = np.array(img).astype(np.float32) / 255.
    data = data.reshape([IMG_SIZE, IMG_SIZE, 3])
    return data



def cluster():
    data_path = '../CBIR_dataset/mirflickr'
    num_class = 10
    fd = 2048
    pca = PCA(fd)
    pca2 = PCA(2)


    mapping = {}

    name_list = []
    feature_list = []
    
    with open('mapping.pkl', 'rb') as fp:
        mapping = pickle.load(fp, encoding='iso-8859-1')
    


    for name in mapping:
        feature_list.append(mapping[name])
        name_list.append(name)

    if os.path.exists('plot.pkl'):
        with open('plot.pkl','rb') as fp:
            cluster = pickle.load(fp, encoding='iso-8859-1')
        cluster_x = cluster[0]
        cluster_y = cluster[1]
        labels = cluster[2]
    else:
        data = np.array(feature_list)
        estimator = KMeans(n_clusters=num_class)
        estimator.fit(data)
        label = estimator.labels_
        labels = []
        
        cluster_x = []
        cluster_y = []
        for i in range(num_class):
            cluster_x.append([])
            cluster_y.append([])
            labels.append([])
        
        feature_list_pca = pca2.fit_transform(feature_list)
        print(len(feature_list_pca))
        for i,l in enumerate(label):
            cluster_x[l].append(feature_list_pca[i][0])
            cluster_y[l].append(feature_list_pca[i][1])
            labels[l].append(i)

        cluster = [cluster_x, cluster_y, labels]
        with open('plot.pkl','wb') as fp:
            pickle.dump(cluster,fp)

    fig, ax = plt.subplots()
    # fig2,ax2 = plt.subplots()
    total = 0
    # ax2.plot(0,0,'.')
    for i in range(num_class):
        num_e = len(cluster_x[i])
        print(num_e)
        ax.scatter(np.array(cluster_x[i]), np.array(cluster_y[i]),alpha=0.5)
        for j in range(int(num_e/10),int(num_e/10)*2):
            # break
            # if i!=0:
                # break
            id = labels[i][j]
            path = os.path.join(data_path,name_list[id])
            print(path)
            img = io(path)
            imgbox = OffsetImage(img,zoom=0.2)
            # imgbox.image.axes = ax2
            ab = AnnotationBbox(imgbox,(cluster_x[i][j],cluster_y[i][j]),xybox=(cluster_x[i][j],cluster_y[i][j]),xycoords='data',boxcoords=("data"))
            ax.add_artist(ab)
            # break

        
    # plt.draw()
            
    plt.show()
    #plt.savefig('test.png')
    
    

if __name__ == '__main__':
    cluster()
