// vector::size
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, u = 0;  
        while (i < nums.size()) {
            if (nums[i] != nums[u]) {
                u += 1;
                nums[u] = nums[i];
            }
            i += 1;
        }
        return u + 1;
    } 
};


int main() {
    std::vector<int> v = {1, 1};
    Solution s;
    int a = s.removeDuplicates(v);
    cout << a;
    cout << "\n";
    for (int i = 0; i < a; i++) {
        cout << v[i];
        cout << "\n";
    }
}
