def MedianOfTwoSortedArray(num1, num2):
    while 1:
        median1 = num1[len(num1) / 2 - 1] + num1[len(num1) / 2] if len(num1) % 2 == 0 else num1[len(num1) / 2]
        median2 = num1[len(num2) / 2 - 1] + num2[len(num2) / 2] if len(num2) % 2 == 0 else num2[len(num2) / 2]
        if median1 == median2:
            return median1
        low = 0
        high = len(num2) - 1
        middle = 0
        while low <= high:
            middle = (low + high) / 2
            if num2[middle] > median1:
                high = middle - 1
            elif num2[middle] < median1:
                low = middle + 1
            else:
                index = middle
                break
        else:
            index = middle

        if median2 > median1:
            num2 = num2[:index]
        else:
            num2 = num2[index:]

