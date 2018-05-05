# coding:utf-8
import numpy as np
from matplotlib import pyplot

attribute = [([] * 10) for i in range(10)]
filename = 'magic04.txt'


def read_file():
    count = 0
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            count += 1
            if not lines:
                break
                pass
            temp = lines.split(",")
            for i in range(len(attribute)):
                attribute[i].append(float(temp[i]))
                pass
            pass
        for Attr in attribute:
            print sum(Attr)/count
        pass


def normal_fun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf
    pass


def fun_a():
    print np.cov(attribute)
    a = np.array(attribute[0])
    b = np.array(attribute[1])
    pyplot.plot(a, b, 'go')
    pyplot.show()

    data = a
    mean = data.mean()
    std = data.std()
    x = np.arange(-200, 200, 0.1)
    y = normal_fun(x, mean, std)
    pyplot.plot(x, y)
    pyplot.hist(data, bins=10, rwidth=0.9, normed=True)
    pyplot.title('Data distribution')
    pyplot.xlabel('Data')
    pyplot.ylabel('Probability')
    pyplot.show()
    pass


def fun_variance(a):
    array = np.array(a)
    return array.var()
    pass


def fun_covariance(a):
    array = np.array(a)
    covariance = np.cov(array)
    return covariance


def fun_print_variance():
    for j in range(len(attribute)):
        print fun_variance(attribute[j])
    print "---------------------------------"
    pass


def fun_print_covariance():
    for j in range(len(attribute)):
        print fun_covariance(attribute[j])
    pass


if __name__ == '__main__':
    read_file()
    fun_a()
    fun_print_variance()
    fun_print_covariance()
