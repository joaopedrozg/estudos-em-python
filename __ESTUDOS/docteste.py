import doctest

class fib:

    def calculo_fib(self, n):
        """
            Método para calcular o fibonacci

            >>> f.calculo_fib(10)
            55
            >>> f.calculo_fib(1)
            1
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    doctest.testmod(extraglobs={'f':fib()})
