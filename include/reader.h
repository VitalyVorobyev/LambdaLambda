/** Text data reader **/

#ifndef READER_H__
#define READER_H__

#include <string>
#include <fstream>

#include "event.h"

namespace llfit {

class ReaderTxt {
    std::ifstream m_ifile;
    Event readEventSimple();
    const bool c_short;

 public:
    ReaderTxt(const std::string& f, bool shortEvent);

    bool eof() const {return m_ifile.eof();}
    Event readEvent();
};

}  // namespace llfit

#endif  // READER_H__
