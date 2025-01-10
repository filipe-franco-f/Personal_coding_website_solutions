#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        int y = 1;
        std::string s = std::to_string(x);
        if (x < 0) {
            std::reverse(s.begin() + 1, s.end());
        } else {
            std::reverse(s.begin(), s.end());
        }
        try {
            y = stoi(s);
        }
        catch (...) {
            y = 0;
        }
        return y;
    }
};

int main(){
    Solution s;

    cout << s.reverse(2000000007);
}