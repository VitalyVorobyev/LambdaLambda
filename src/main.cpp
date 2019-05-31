#include <string>
#include <iostream>
#include <fstream>
#include <vector>

#include "reader.h"
#include "driver.h"
#include "fcn.h"
#include "fitter.h"
#include "acceptReject.h"

#include "PodioReader.h"
#include "LLKine.h"

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
    return loadData("../data/llraw.dat", false);
}

inline std::vector<Event> loadSignalData() {
    // return loadData("./ll_xi1.txt", true);
    return loadData("../data/ll_xi1.dat", true);
}

int generateData(double xi) {
    // alpha, dphi, alpha1, alpha2, xi
    Driver driver(0.6, 0.5*3.1415, 0.6, -0.6, xi);
    auto data = loadNormData();

    std::ofstream ofile("../data/ll_xi1.txt", std::ofstream::out);
    AcceptReject ar(driver, 1);
    size_t nevt = ar.run(data, ofile);
    ofile.close();

    cout << nevt << " events saved" << endl;

    return 0;
}

int fitData() {
    // alpha, dphi, alpha1, alpha2, xi
    Driver driver(0.3, 0., 0.7, -0.7, 1.);

    auto dataNorm = loadNormData();
    auto dataSignal = loadSignalData();

    for (size_t i = 0; i < 10; i++) {
        cout << dataNorm[i] << endl;
    }

    for (size_t i = 0; i < 10; i++) {
        cout << dataSignal[i] << endl;
    }

    std::vector<Event> data(dataSignal.begin(), dataSignal.begin()+20000);
    std::vector<Event> norm(dataNorm.begin() + 500000, dataNorm.begin()+700000);

    TheFCN fcn(driver, data, norm);
    Fitter fitter(fcn);
    auto fitres = fitter.fit();
    cout << fitres;

    return 0;
}

void writeEvent(const PodioReader& pr, std::ofstream& os) {
    os << "Event" << endl
       << pr.p4p() << endl
       << pr.p4pbar() << endl
       << pr.p4pip()  << endl
       << pr.p4pin() << endl;
    auto xi = LLKine::xi(pr.p4p(), pr.p4pin(), pr.p4pbar(), pr.p4pip());
    for (auto x : xi) {
        os << x << " ";
    }
    os << endl;
}

int processPodio() {
    PodioReader pr("/home/vitaly/CTau/Data/fccedm/jpsipppipi.root");
    std::ofstream os("../data/llraw.dat", std::ofstream::out);

    for (size_t i = 0; i < pr.nEvt(); i++) {
        if (!((i+1) % 10000)) {
            cout << i+1 << " events" << endl;
        }
        pr.event();
        writeEvent(pr, os);
    }
    return 0;
}

int main(int argc, char** argv) {
    if (argc == 1) {
        return fitData();
    } else if (argc == 2) {
        string cmd(argv[1]);
        if (cmd == "fit") {
            return fitData();
        } else if (cmd == "gen") {
            return generateData(1.);
        } else if (cmd == "podio") {
            return processPodio();
        }
    }
    cout << "Wrong use" << endl;
    return -1;
};
