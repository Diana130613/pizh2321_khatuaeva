#include "WordCount.h"

#include <iostream>

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Использование: " << argv[0] << " [OPTION] filename [filename...]" << std::endl;
        return 1;
    }

    Parsing parser;
    parser.parse(argc, argv);
    PrintInfo printer;
    FileReader reader;

    for (const auto& filename : parser.filenames) {
        reader.reset();
        reader.processFile(filename);
        printer.print(reader, parser, parser.filenames.size() > 1 ? filename : "");
    }

    return 0;
}