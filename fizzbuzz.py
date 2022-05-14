class Fizzbuzz:
    @staticmethod
    def calculate(n):
        if n % 15 == 0:
            return 'fizzbuzz'
        elif n % 3 == 0:
            return 'fizz'
        elif n % 5 == 0:
            return 'buzz'
        else:
            return n
