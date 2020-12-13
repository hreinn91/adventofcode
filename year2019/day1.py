import os


def getFuelMass(mass):
    if int(mass/3)-2 <= 0:
        return 0
    res = int(mass/3)-2
    return res + getFuelMass(res)


def getModuleFuelMass(inputFile):
    res = 0
    with open(inputFile) as fp:
        for line in fp:
            res = res + getFuelMass(int(line[:-1]))

    return res

def main():
    print(getModuleFuelMass('./input'))
    print()

    return


if __name__ == '__main__':
    main()

