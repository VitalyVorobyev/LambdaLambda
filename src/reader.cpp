#include "reader.h"

#include <iostream>

using std::cerr;
using std::endl;
using std::string;

using namespace llfit;

ReaderTxt::ReaderTxt(const std::string& f, bool shortEvent) :
    m_ifile(std::ifstream(f, std::ifstream::in)), c_short(shortEvent) {
    if (!m_ifile.good()) {
        cerr << "Can't open file " << f << endl;
        throw 1;
    }
}

Event ReaderTxt::readEvent() {
    if (c_short) return readEventSimple();
    
    static string line;
    for (size_t i = 0; i < 5; ++i) {  // skip 4 lines and read the 5th
        getline(m_ifile, line);
    }
    
    static double th, th1, ph1, th2, ph2;
    m_ifile >> th >> th1 >> ph1 >> th2 >> ph2;
    for (size_t i = 0; i < 2; ++i) {  // skip another two lines
        getline(m_ifile, line);
    }
    return Event(th, th1, ph1, th2, ph2);
}

Event ReaderTxt::readEventSimple() {
    static double th, th1, ph1, th2, ph2;
    m_ifile >> th >> th1 >> ph1 >> th2 >> ph2;
    return Event(th, th1, ph1, th2, ph2);
}
