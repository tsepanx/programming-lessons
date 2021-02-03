import random
import numpy as np
from PIL import Image

def knn(coords, iterations_count, clusters_count=256, shape=3):
    rand = lambda: random.randint(0, 30)
    rand_pos = lambda: [rand() for _ in range(shape)]

    points_count = len(coords)
    colors = [0] * points_count
    centers = [rand_pos() for _ in range(clusters_count)]

    for i in range(iterations_count):
        # Update colors
        for j in range(points_count):
            min_dist = float('inf')
            best_cent = [-1, -1]

            p = coords[j]
            for l, cent in enumerate(centers):
                # dist = (cent[0] - p[0]) ** 2 + (cent[1] - p[1]) ** 2
                try:
                    dist = (cent[0] - p[0]) ** 2 + (cent[1] - p[1]) ** 2 + (cent[2] - p[2]) ** 2
                except Exception as e:
                    print(cent, p)
                    print(*centers, sep='\n')
                    exit()

                if dist < min_dist:
                    min_dist = dist
                    best_cent = l

            colors[j] = best_cent

        print(i, 1)

        # Update centers
        for j in range(clusters_count):
            coords_sum = [0] * shape
            cnt = 0
            for l in range(0, points_count):
                if colors[l] == j:
                    for s in range(shape):
                        coords_sum[s] += coords[l][s]
                    cnt += 1

            divide_list = lambda x: x / cnt
            centers[j] = list(map(divide_list, coords_sum)) if cnt else rand_pos()

        print(i, 2)

    return centers, colors

def main():
    im = Image.open('lenna.png')

    without_alpha = lambda x: x[:-1]
    arr = list(map(without_alpha, im.getdata()))


    centers, colors = knn(arr, 6)

    def fill_with_centers(coords, centers, colors):
        res_coords = coords[:]
        for i in range(len(colors)):
            cluster = centers[colors[i]]
            res_coords[i] = cluster

        return res_coords

    def array_from_list(l):
        # c = [[0] * k * im.width for i in range(k * im.height)]
        # return np.asarray(c)
        res = np.array([])
        

    res_coords = fill_with_centers(arr, centers, colors)
    # res_coords = arr

    res_coords = np.array([res_coords], dtype=np.uint8)
    res_coords.resize((256, 256, 3))

    print(res_coords.shape)

    res_img = Image.fromarray(res_coords)
    res_img.show()
    res_img.save('result_png.png')

main()
