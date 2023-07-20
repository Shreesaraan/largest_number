def largestNumber(array):
    singleDigitArray = []

    for i in range(len(array)):
        if array[i] > 9:
            while array[i] > 0:
                singleDigitArray.append(str(array[i] % 10))
                array[i] //= 10
        else:
            singleDigitArray.append(str(array[i]))

    singleDigitArray.sort(reverse=True)

    return "".join(singleDigitArray)


A = list(map(int, input().split()))
print(largestNumber(A))