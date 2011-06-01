/**
 *  Fibonacci numbers, the same that ran slow on python
 */
#include <stdio.h>
#include <stdlib.h>

#define __LIMIT__ 4000000

int fibonacci(int n) {
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int counter = 1;
    int result = 0;
    int fib = 0;
    while (fib < __LIMIT__) {
        fib = fibonacci(counter);
        if (fib % 2 == 0) result += fib;
        counter++;
    }
    printf("%i\n", result);
    return EXIT_SUCCESS;
}
