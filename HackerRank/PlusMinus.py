class PlusMinus:
    @staticmethod
    def plus_minus(arr):
        n = len(arr)
        positive_count = 0
        negative_count = 0
        zero_count = 0

        for num in arr:
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1
            else:
                zero_count += 1

        print("{:.6f}".format(positive_count / n))
        print("{:.6f}".format(negative_count / n))
        print("{:.6f}".format(zero_count / n))


if __name__ == '__main__':
    print("Welcome to PlusMinus program!")
    n = int(input("Please enter the number of elements in the array: "))
    arr = list(map(int, input("Please enter the elements of the array, separated by spaces: ").split()))

    pm = PlusMinus()
    pm.plus_minus(arr)


