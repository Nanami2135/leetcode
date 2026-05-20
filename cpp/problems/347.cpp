#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using std::vector;
using std::cout;
using std::endl;


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freq{};
        for (const auto &x : nums) {
            ++freq[x];
        };

        // first: value, second: frequency
        vector<std::pair<int, int>> h{};
        h.reserve(freq.size());

        auto cmp = [](const auto& a, const auto& b) {
            return a.second > b.second; // min-heap by second
        };

        for (const auto& kv : freq) {
            h.push_back(kv);
            std::push_heap(
                h.begin(),
                h.end(),
                cmp
            );

            if (h.size() > k) {
                std::pop_heap(
                    h.begin(),
                    h.end(),
                    cmp
                );
                h.pop_back();
            };
        }

        vector<int> result{};
        for (auto p : h) {
            result.push_back(p.first);
        }
        return result;
    }
};

static void print_vector(const vector<int>& values) {
    cout << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        cout << values[i];
        if (i + 1 < values.size()) {
            cout << ",";
        }
    }
    cout << "]";
}

static bool same_contents(vector<int> lhs, vector<int> rhs) {
    std::sort(lhs.begin(), lhs.end());
    std::sort(rhs.begin(), rhs.end());
    return lhs == rhs;
}

int main() {
    Solution sol;

    {
        vector<int> nums{1, 1, 1, 2, 2, 3};
        int k = 2;
        auto result = sol.topKFrequent(nums, k);
        vector<int> expected{1, 2};
        cout << "Example 1: ";
        print_vector(result);
        cout << " expected [1,2]";
        cout << (same_contents(result, expected) ? " OK" : " MISMATCH") << endl;
    }

    {
        vector<int> nums{1};
        int k = 1;
        auto result = sol.topKFrequent(nums, k);
        vector<int> expected{1};
        cout << "Example 2: ";
        print_vector(result);
        cout << " expected [1]";
        cout << (same_contents(result, expected) ? " OK" : " MISMATCH") << endl;
    }

    {
        vector<int> nums{1, 2, 1, 2, 1, 2, 3, 1, 3, 2};
        int k = 2;
        auto result = sol.topKFrequent(nums, k);
        vector<int> expected{1, 2};
        cout << "Example 3: ";
        print_vector(result);
        cout << " expected [1,2]";
        cout << (same_contents(result, expected) ? " OK" : " MISMATCH") << endl;
    }

    return 0;
}
