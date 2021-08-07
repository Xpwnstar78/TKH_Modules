def main():

    alist = ['Tom', 54, 'Julia', 78]
    print(alist)

    alist.append(help)
    print(alist)

    blists = [['Tom', 54], ['Julia', 78]]
    print(blists)

    blists[-1]
    print(blists[-1])

    print(blists[-2][0])

    blists.append(['Mak', 90])
    print(blists)

    a = [0]*5
    print(a)

    cols = 5
    rows = 4
    dlist = [[1]*cols]*rows
    print(dlist)

    tup1 = ('Tom', 78)
    tup2 = list(tup1)
    tup2[1] = 90
    tup1 = tuple(tup2)
    print(tup1)

    tup2 = ('Julia', 89)
    print(tup1 + tup2)

    print(tup1)

    tup3 = tup1 + tup2
    print(tup3)

    print(len(tup3))

    country_code = {'India': 1, 'USA': 2, 'China': 3}
    print(country_code)

    print(country_code['China'])

    country_code['UAE'] = 4
    print(country_code)

    print('Inda' in country_code)

    x = True
    print(type(x))

    print(1 == 2)

    print(1 != 2)

    a = 1
    b = 2
    print(a == b)
    print(a > b)
    print(a < b)
    print(a != b)

    color = 'red'
    if color == 'red':
        print("Color is red!")
        print("Color problem is solved!!")

    color = 'kjh'
    if color == 'red':
        print("Color is red!")
    else:
        print("color is not red!")
        print("Color problem is solved!!")

    color = 'green'
    if color == 'red':
        print("Color is red!")
    elif color == 'green':
        print("Color is green!")
    else:
        print("color is not red!")
        print("Color problem is solved!!")

    age = 15
    if age >= 18:
        print("Adult")
    else:
        print("Juvenile")

    a = 0
    print(not(a))

    a = 3
    print(not(a))

    a = True
    print(not(a))

    score = 76
    percentile = 83
    if score < 75 and percentile < 90:
        print("Admission successful!")
    else:
        print("Try again next year")

    print(range(5))

    for i in range(5):
        print(i)

    for i in range(1, 10, 2):
        product = 8 * i
        print(product)

    names = ('harshit', 'shubham', 'sahil')
    for name in names:
        print(name.upper())

    age = [12, 43, 45, 10]
    i = 0
    while i < len(age):
        if age[i] >= 18:
            print("Adult")
        else:

            print("Juvenile")
        i += 1

    cubes = [n ** 3 for n in range(1, 10)]
    print(cubes)

    cubes = []
    for i in range(1, 10):
        cubes.append(i ** 3)
        print(cubes)

    help(abs)

    print(abs(2-5))

    def add_two_numbers(a, b):
        sum = a + b
        return sum

    print(add_two_numbers(5, 11))

    def fahr_to_celsius(temp):
        tempInCel = (temp - 32) * 5/9
        return tempInCel

    print(fahr_to_celsius(50))


if __name__ == '__main__':
    main()
