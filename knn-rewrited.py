import random

coords = [[30, 12], [26, 27], [22, 30], [7, 19], [4, 19], [0, 8], [23, 17], [4, 20], [26, 5], [14, 15]]

def knn(coords, iterations_count, clusters_count=256):
    rand = lambda: random.randint(0, 30)

    points_count = len(coords)
    colors = [0] * points_count
    centers = [[rand(), rand()] for _ in range(clusters_count)]

    for i in range(0, iterations_count):
        # Update colors
        for j in range(0, points_count):
            min_dist = float('inf')
            best_cent = [-1, -1]

            p = coords[j]
            for l, cent in enumerate(centers):

                dist = (cent[0] - p[0]) ** 2 + (cent[1] - p[1]) ** 2

                if dist < min_dist:
                    min_dist = dist
                    best_cent = l

            colors[j] = best_cent

        # new centers
        for j in range(0, clusters_count):
            x_sum = 0
            y_sum = 0
            cnt = 0
            for l in range(0, len(coords)):
                if colors[l] == j:
                    x_sum += coords[l][0]
                    y_sum += coords[l][1]
                    cnt += 1
            if cnt != 0:
                centers[j] = [x_sum/cnt, y_sum/cnt]
            else:
                centers[j] = [rand(), rand()]
    return centers
