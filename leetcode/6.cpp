#include <iostream>
using namespace std;


class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            string sol = s;
            return sol;
        }
        string sol = "";
        unsigned int value1 = 0;
        unsigned int value2 = 0;
        for (int i = 0; i < numRows; i ++) {
            if (i != 0 && i != numRows - 1) {
                value1 = i;
                value2 = 2 * numRows - 2 - i;
                while (value2 < s.size()) {
                    sol += s[value1];
                    sol += s[value2];
                    value1 += 2 * numRows - 2;
                    value2 += 2 * numRows - 2;
                } if (value1 < s.size()) {
                    sol += s[value1];
                }
            } else {
                value1 = i;
                while (value1 < s.size()) {
                    sol += s[value1];
                    value1 += 2 * numRows - 2;
                }
            }
        }
        return sol;
    }
};

int main() {

    string s = "PAYPALISHIRING";
    int numRows = 3;

    Solution solver;

    string solution = solver.convert(s, numRows);

    cout << solution;
}


