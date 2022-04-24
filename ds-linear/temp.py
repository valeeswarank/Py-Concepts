import numpy

def reshape(a1, a2):
    np = numpy.array(a2, int)
    a1 = numpy.array(a1, int)
    np = numpy.transpose(np)
    np = np.reshape((int(a1[0]), int(a1[1])))
    print(np)

    #np = numpy.transpose(np)
    np = np.flatten()
    np.sort()
    print(np)


if __name__ == "__main__":
    h = []
    c1 = []
    c2 = []

    l = 0
    c = []
    while True:
        try:
            line = input()
            if l == 0:
                h = line.strip().split(" ")
            else:
                c.append(line.strip().split(" "))
            l +=1
        except EOFError:
            break

    c = numpy.array(c, int)
    c.transpose()

    reshape(h, c)



