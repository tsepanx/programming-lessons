from knn import *

CLUSTERS_COUNT = 64
LOOPS_COUNT = 2

im = Image.open('lenna.png')

without_alpha = lambda x: x[:-1]
arr = list(map(without_alpha, im.getdata()))

centers, colors = knn(arr, LOOPS_COUNT, CLUSTERS_COUNT)
res_coords = fill_with_centers(arr, centers, colors)

res_coords = np.array([res_coords], dtype=np.uint8)
res_coords.resize((256, 256, 3))

print(res_coords.shape)
print(np.array(colors).shape)

res_img = Image.fromarray(res_coords)
res_img.show()
res_img.save('result_png.png')
