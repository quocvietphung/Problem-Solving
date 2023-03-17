class CamelCase:
    @staticmethod
    def split_camel_case(string):
        words = [string[0]]
        for char in string[1:]:
            if char.isupper():
                words.append(' ')
            words[-1] += char
        return ' '.join(words).lower()

    @staticmethod
    def combine_camel_case(words, type):
        if type == 'M':
            return words.replace(' ', '').capitalize() + '()'
        elif type == 'C':
            return words.replace(' ', '').capitalize()
        else:
            return CamelCase.split_camel_case(words)

if __name__ == '__main__':
    print("Welcome to Camel Case program!")
    while True:
        try:
            line = input("Please enter your operation: ")
            op, t, s = line.split(';')
            if op == 'S':
                print(CamelCase.split_camel_case(s))
            else:
                print(CamelCase.combine_camel_case(s, t))
        except:
            break
