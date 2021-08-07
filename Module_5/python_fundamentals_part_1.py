def main():
    print("Hello World")

    input()

    a = 5
    if a == 5:
        print("a equals 5")

    myString = 'hello world'
    print(type(myString))

    n = 10
    print(type(n))

    n_float = 7.5
    print(type(n_float))

    single_string = 'Its a single quote string'
    print(single_string)

    double_string = "It's a double quote string"
    print(double_string)

    n1 = 5
    n2 = 7.5
    print(n1+n2)

    nstr1 = "abc"
    print(nstr1 + str(n1))

    nstr2 = "def"
    print(nstr1 + nstr2)

    n3, n4 = 10, 11
    print(n3)
    print(n4)

    result = 3 + 4.0 / 2 * 5
    print(result)

    remainder = 17 % 10
    print(remainder)

    x = 5
    y = 4
    print(x ** y)

    nstr = "abc"
    ans = nstr * 10
    print(len(ans))

    name = "Harshit"
    print("%s is a data scientist!" % name)

    print(name.upper())
    print(name.lower())

    nstr1 = "it is a nice day today."
    print(nstr1.capitalize())

    print(name.index('s'))

    print(name[2:5])

    print(name[2:6:2])

    alist = [3, 4, 5]
    print(alist)

    alist1 = ['harshit', 2, 5.5]
    print(alist1)

    alist1.append(10)
    alist1.append(15)
    print(alist1)

    alist1.pop()
    print(alist1)

    print(alist1[3])

    print(alist1[1:])

    alist1.append([1, 2, 3])
    print(alist1)

    print(alist1*2)

    print(alist1 + alist1)


if __name__ == '__main__':
    main()
