#include <cassert>
#include <vector>
#include <iostream>
using namespace std;

string checkGuess(int secret, int guess) {
    // Paste the same implementation of checkGuess from number_guess.cpp here
}

int calculateScore(int attempts) {
    // Paste the same implementation of calculateScore from number_guess.cpp here

}

string giveHint(int secret, vector<int> history) {
    // Paste the same implementation of giveHint from number_guess.cpp here
}

int main() {

    assert(checkGuess(50, 70) == "HIGH");
    assert(checkGuess(50, 30) == "LOW");
    assert(checkGuess(50, 50) == "CORRECT");

    assert(calculateScore(2) == 100);
    assert(calculateScore(5) == 70);
    assert(calculateScore(8) == 40);
    assert(calculateScore(12) == 10);

    vector<int> h1 = {20, 80};
    assert(giveHint(60, h1) == "Try between 21 and 79");

    vector<int> h2 = {10, 90, 40, 70};
    assert(giveHint(60, h2) == "Close!");

    vector<int> h3 = {5, 95, 10};
    assert(giveHint(50, h3) == "Try between 11 and 94");

    vector<int> h4 = {10, 90, 55};
    assert(giveHint(60, h4) == "Very Close!");

    cout << "All tests passed!" << endl;

    return 0;
}
