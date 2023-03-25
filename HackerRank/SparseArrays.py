class SparseArrays:
    def __init__(self, strings):
        self.freq = {}
        for string in strings:
            if string not in self.freq:
                self.freq[string] = 0
            self.freq[string] += 1

    def count(self, queries):
        results = []
        for query in queries:
            if query in self.freq:
                results.append(self.freq[query])
            else:
                results.append(0)
        return results

if __name__ == '__main__':
    n = int(input("Please enter the number of input strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter input string #%d: " % (i + 1)))
    m = int(input("Please enter the number of query strings: "))
    queries = []
    for i in range(m):
        queries.append(input("Enter query string #%d: " % (i + 1)))

    sparse_arrays = SparseArrays(strings)
    results = sparse_arrays.count(queries)

    print("For each query, the number of times it occurs in the list of input strings is:")
    for result in results:
        print(result)
