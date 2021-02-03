import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

from knn import fill_with_centers

im = Image.open('lenna.png')

without_alpha = lambda x: x[:-1]
arr = list(map(without_alpha, im.getdata()))

kmeans = KMeans(n_clusters=8, random_state=0).fit(arr)
print(kmeans)

colors = kmeans.predict(arr) # kmeans.labels_
print(colors)

# res_coords = fill_with_centers(arr, 

# res_img = Image.fromarray(res_coords)

# res_img.show()
# res_img.save('result_png.png')
