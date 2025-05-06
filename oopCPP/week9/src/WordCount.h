#ifndef WORDCOUNT_H
#define WORDCOUNT_H

#include <string>
#include <vector>

class FileReader {
public:
    int lines = 0;
    int bytes = 0;
    int words = 0;
    int letters = 0;

    void processFile(const std::string& filename);
    void reset();
};

class Parsing {
public:
    bool printLines = false;
    bool printBytes = false;
    bool printWords = false;
    bool printLetters = false;
    std::vector<std::string> filenames;

    void parse(int argc, char* argv[]);
};

class PrintInfo {
public:
    void print(const FileReader& reader, const Parsing& options, const std::string& filename = "") const;
};

#endif