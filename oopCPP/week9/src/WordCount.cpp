#include "WordCount.h"

#include <cctype>
#include <fstream>
#include <iostream>

void FileReader::processFile(const std::string& filename) {
        std::ifstream file(filename, std::ios::binary);

        std::string line;
        bool in_word = false;

        if (!file.is_open()) {
            std::cerr << "Ошибка при открытии файла." << std::endl;
            return;
        }

        // Переводим указатель в конец файла
        file.seekg(0, std::ios::end);
         // Получаем размер файла в байтах
        bytes = file.tellg();
        // Возвращаем указатель в начало файла
        file.seekg(0, std::ios::beg);

        while(getline(file, line)) {
            lines++;

            for (char ch : line) {
                if (isalpha(static_cast<unsigned char>(ch))) { // если текущий символ — буква
                    letters++;
                    if (!in_word) { // если ещё не находимся внутри слова
                        in_word = true; // начинаем новое слово
                        words++; // увеличиваем счётчик слов
                    }
                } else { // если текущий символ не альфа-цифровой
                    in_word = false; // заканчиваем слово
                }
            }
        }
        file.close(); // Закрываем файл после завершения чтения
    }

void FileReader::reset() {
    lines = 0;
    bytes = 0;
    words = 0;
    letters = 0;
}

void Parsing::parse(int argc, char* argv[]) {
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];

        if (arg.size() > 1 && arg[0] == '-' && arg[1] != '-') {
            for (size_t j = 1; j < arg.size(); ++j) {
                switch (arg[j]) {
                    case 'l': printLines = true; break;
                    case 'w': printWords = true; break;
                    case 'c': printBytes = true; break;
                    case 'm': printLetters = true; break;
                    default:
                        std::cerr << "Неизвестная опция: " << arg[j] << std::endl;
                        break;
                }
            }
        }

        else if (arg == "-l" || arg == "--lines") {
            printLines = true;
        } else if (arg == "-c" || arg == "--bytes") {
            printBytes = true;
        } else if (arg == "-w" || arg == "--words") {
            printWords = true;
        } else if (arg == "-m" || arg == "--chars") {
            printLetters = true;
        } else if (arg == "-lwc" || arg == "-l -w -c" || arg == "-l -c -w") {
        // Комбинированные опции (например, -lwc)
            printLines = true;
            printWords = true;
            printBytes = true;
        } else if (arg[0] != '-') {
            filenames.push_back(arg);
        } else {
            std::cerr << "Неизвестная опция: " << arg << std::endl;
        }
    }
        // Если ни одна опция не задана, выводим всё
        if (!printLines && !printBytes && !printWords && !printLetters) {
            printLines = true;
            printWords = true;
            printBytes = true;
        }
    }

void PrintInfo::print(const FileReader& reader, const Parsing& options, const std::string& filename) const {
    if (!filename.empty()) {
        std::cout << "Файл: " << filename << std::endl;
    }
    if (options.printLines) 
        std::cout << "Количество строк: " << reader.lines << "\n";
    if (options.printBytes) 
        std::cout << "Количество байтов: " << reader.bytes << "\n";
    if (options.printWords) 
        std::cout << "Количество слов: " << reader.words << "\n";
    if (options.printLetters) 
        std::cout << "Количество букв: " << reader.letters << "\n";
    std::cout << std::endl;
}