class DivisibleSumPairs:
    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ar = ar
        self.count = 0

    def find_pairs(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if (self.ar[i] + self.ar[j]) % self.k == 0:
                    self.count += 1
        return self.count


if __name__ == '__main__':
    print("This program finds the number of pairs in an array of integers where the sum of the pair is divisible by a given integer.")
    input_str = input("Enter the length of the array and the divisor separated by a space: ")
    n, k = map(int, input_str.split())
    input_str = input("Enter the elements of the array separated by a space: ")
    ar = list(map(int, input_str.split()))
    pairs = DivisibleSumPairs(n, k, ar)
    print("The number of pairs where the sum is divisible by {} is {}.".format(k, pairs.find_pairs()))

