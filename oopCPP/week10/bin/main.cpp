#include "../lib/number.h"
#include <iostream>

int main() {
    // Создание чисел
    uint2022_t a = from_uint(123456);
    uint2022_t b = from_string("75323456789876543212345678987678900987654345678909876432345678");

    // Арифметические операции
    std::cout << "a + b = " << a + b << std::endl;
    std::cout << "b - a = " << b - a << std::endl;
    std::cout << "a * b = " << a * b << std::endl;
    std::cout << "b / a = " << b / a << "\n\n";

    std::cout << "a * b = " << a * b << std::endl;
    std::cout << "b / a = " << b / a << "\n\n";

    // Сравнение
    std::cout << "a == b: " << (a == b ? "true" : "false") << std::endl;
    std::cout << "a != b: " << (a != b ? "true" : "false") << std::endl;

    return 0;
}