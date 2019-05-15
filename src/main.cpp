#include <string>
#include <iostream>
#include <fstream>
#include <vector>

#include "reader.h"
#include "driver.h"
#include "fcn.h"
#include "fitter.h"
#include "acceptReject.h"

using std::string;
using std::cout;
using std::endl;

using namespace llfit;

std::vector<Event> loadData(const string& fname, bool simple) {
    ReaderTxt reader(fname, simple);
    std::vector<Event> events;
    while (!reader.eof()) {
        events.emplace_back(reader.readEvent());
    }
    cout << events.size() << " events" << endl;
    return std::move(events);
}

inline std::vector<Event> loadNormData() {
    return loadData("/home/vitaly/ctau/LambdaLambda/ll.dat", false);
}

inline std::vector<Event> loadSignalData() {
    return loadData("/home/vitaly/ctau/LambdaLambda/build/ll_xi1.txt", true);
}

int generateData(double xi) {
    Driver driver(0.6, 0.5*3.1415, 0.6, -0.6, xi);
    auto data = loadNormData();

    std::ofstream ofile("ll_xi1.txt", std::ofstream::out);
    AcceptReject ar(driver, 1);
    size_t nevt = ar.run(data, ofile);
    ofile.close();

    cout << nevt << " events saved" << endl;

    return 0;
}

int fitData() {
    Driver driver(0.3, 0., 0.7, -0.7, 1.);

    auto dataNorm = loadNormData();
    auto dataSignal = loadSignalData();

    std::vector<Event> data(dataSignal.begin(), dataSignal.begin()+20000);
    std::vector<Event> norm(dataNorm.begin() + 500000, dataNorm.begin()+700000);

    TheFCN fcn(driver, data, norm);
    Fitter fitter(fcn);
    auto fitres = fitter.fit();
    cout << fitres;

    return 0;
}

int main(int argc, char** argv) {
    if (argc == 1) {
        return fitData();
    } else if (argc == 2) {
        string cmd(argv[1]);
        if (cmd == "fit") return fitData();
        else if (cmd == "gen") return generateData(1.);
    }
    cout << "Wrong use" << endl;
    return -1;
};
