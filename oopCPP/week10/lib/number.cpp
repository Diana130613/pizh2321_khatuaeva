#include "number.h"
#include <string>


uint2022_t from_uint(uint32_t i) {
    uint2022_t result;
    result.number[0] = i;
    return result;
}

// Переход из строки в число
uint2022_t from_string(const char* buff) {
    uint2022_t result = from_uint(0);
    
    for (int i = 0; buff[i] != '\0'; i++) {
        if (buff[i] < '0' || buff[i] > '9') {
            std::cerr << "Invalid character in number string" << std::endl;
            return from_uint(0);
        }
        
        // Умножение результата на 10 с последующим добавлением новой цифры
        result = result * from_uint(10);
        result = result + from_uint(buff[i] - '0');
    }
    
    return result;
}

// Сложение чисел
uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t sum;
    uint64_t t = 0; // Флаг переноса
    
    for (int i = 0; i < uint2022_t::SIZE; i++) {
        uint64_t res = (uint64_t)lhs.number[i] + rhs.number[i] + t;
        sum.number[i] = res & 0xFFFFFFFF;
        t = res >> 32;
    }
    
    return sum;
}

// Вычитание
uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint64_t borrow = 0; // Флаг заёма
    
    for (int i = 0; i < uint2022_t::SIZE; i++) {
        uint64_t res = (uint64_t)lhs.number[i] - rhs.number[i] - borrow;
        result.number[i] = res & 0xFFFFFFFF;

        if (res >> 32) {
            borrow = 1;
        } else {
            borrow = 0;
        }
    }
    
    return result;
}

// Умножение
uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint64_t t = 0;

    for (int i = 0; i < uint2022_t::SIZE; i++) {
        for (int k = 0; k < uint2022_t::SIZE - i; k++) {
            uint64_t temp = (uint64_t)lhs.number[i] * rhs.number[k] + result.number[i+k] + t;
            result.number[i+k] = temp & 0xFFFFFFFF;
            t = temp >> 32;
        }
    }
    
    return result;
}

// Деление
uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    // Проверка деления на нуль
    bool is_rhs_zero = true;
    for (int i = 0; i < uint2022_t::SIZE; i++) {
        if (rhs.number[i] != 0) {
            is_rhs_zero = false;
            break;
        }
    }

    uint2022_t quotient = from_uint(0); // Частное
    uint2022_t remainder = from_uint(0); // Остаток

    // Перебор битов с конца
    for (int i = uint2022_t::SIZE * 32 - 1; i >= 0; i--) {
        uint64_t t = 0;
        for (int k = 0; k < uint2022_t::SIZE; k++) {
            uint64_t res = (uint64_t)remainder.number[k] << 1 | t;
            remainder.number[k] = res & 0xFFFFFFFF;
            t = res >> 32;
        }

        int word = i / 32;
        int bit = i % 32;
        if (word < uint2022_t::SIZE && (lhs.number[word] & (1 << bit))) {
            remainder.number[0] |= 1;
        }

        // Пробное вычитание
        uint2022_t res_remainder = remainder;
        uint2022_t res_result = from_uint(0);
        bool can_subtract = true;
        uint64_t borrow = 0;

        for (int k = 0; k < uint2022_t::SIZE; k++) {
            uint64_t diff = (uint64_t)res_remainder.number[k] - rhs.number[k] - borrow;
            res_result.number[k] = diff & 0xFFFFFFFF;

            if ((diff >> 32) != 0) {
                borrow = 1;
            } else {
                borrow = 0;
            }
        }

        // Если вычитание прошло успешно (без borrow)
        if (borrow == 0) {
            remainder = res_result;
            // Устанавливаем текущий бит в quotient
            word = i / 32;
            bit = i % 32;
            if (word < uint2022_t::SIZE) {
                quotient.number[word] |= (1 << bit);
            }
        }
    }

    return quotient;
}

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = 0; i < uint2022_t::SIZE; i++) {
        if (lhs.number[i] != rhs.number[i]) {
            return false;
        }
    }
    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    // Если ноль
    if (value == from_uint(0)) {
        stream << "0";
        return stream;
    }

    uint2022_t temp = value;
    std::string result;

    while (temp != from_uint(0)) {
        // Получение последней цифры
        uint2022_t digit = temp - (temp / from_uint(10)) * from_uint(10);
        
        // Добавление цифры в начало строки
        result.insert(0, 1, '0' + digit.number[0]);
        
        // Деление на 10
        temp = temp / from_uint(10);
    }

    stream << result;
    return stream;
}
