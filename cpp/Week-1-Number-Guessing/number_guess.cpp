#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

string checkGuess(int secret, int guess) {

}

int calculateScore(int attempts) {

}

string giveHint(int secret, vector<int> history) {
}


// -------- CLI PART (DO NOT MODIFY) --------

int main() {

    srand(time(0));
    int secret = rand() % 100 + 1;

    vector<int> history;
    int attempts = 0;

    cout << "Welcome to Smart Number Guessing Game!" << endl;

    while (true) {
        int guess;
        cout << "Enter guess: ";
        cin >> guess;

        attempts++;
        history.push_back(guess);

        string result = checkGuess(secret, guess);

        if (result == "CORRECT") {
            cout << "Correct!" << endl;
            cout << "Score: " << calculateScore(attempts) << endl;
            break;
        }

        cout << result << endl;
        cout << "Hint: " << giveHint(secret, history) << endl;
    }

    return 0;
}
