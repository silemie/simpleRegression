import sys
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def mean(xs):
    return sum(xs) / len(xs)

def std(xs):
    mean_x = mean(xs)
    sum_x = 0

    for x in xs:
        sum_x += (x - mean_x)**2

    var = sum_x / (len(xs) - 1)

    return var**0.5


def remove_outliers(xs, ys):
    mean_y = mean(ys)
    std_y = std(ys)

    final_xs = []
    final_ys = []

    upper = mean_y + 2 * std_y
    lower = mean_y - 2 * std_y

    for i in range(len(ys)):
        
        if ys[i] > upper or ys[i] < lower:
            print('remove outliers: (',xs[i],',',ys[i],')')

        if ys[i] <= upper and ys[i] >= lower:
            final_xs.append(xs[i])
            final_ys.append(ys[i])

    return final_xs, final_ys

def fit(xs, ys):

    # if(len(xs) != (ys)):
    #     raise 

    mean_x = mean(xs)
    mean_y = mean(ys)
    n = len(xs)
    square_x = mean_x ** 2

    arr_sum = 0
    xs_sum = 0

    for i in range(n):
        xs_sum = xs[i] * xs[i]
        arr_sum = xs[i] * ys[i]

    a = (arr_sum - n * mean_x * mean_y) / (xs_sum - n * square_x)
    b = mean_y - a * mean_x

    return a, b

def main():

    path = sys.argv[1]
    outliers = sys.argv[2].lower()

    xs = []
    ys = []

    f = open(path, "r")
    for line in f:
        point = line.split(',')
        xs.append(int(point[0]))
        ys.append(int(point[1]))
    f.close()

    if outliers == "yes":
        xs, ys = remove_outliers(xs, ys)

    a, b = fit(xs, ys)

    regression = []
    for x in xs:
        regression.append(a * x + b)

    print('The water line of the last point is', regression[len(xs) - 1])

    #The following part is to plot the line
    #Not necessary in algorithm

    plt.scatter(xs,ys,color='#003F72')
    plt.plot(xs, regression)
    plt.show()

if __name__ == "__main__":
    main()
