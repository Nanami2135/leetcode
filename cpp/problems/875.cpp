#include <algorithm>
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

class Solution {
  public:
    int minEatingSpeed(vector<int> &piles, int h) {
        auto max_iter = std::max_element(piles.begin(), piles.end());

        int l = 1;
        int r = *max_iter;
        int answer = r;

        while (r - l >= 0) {
            int mid = (r + l) / 2;
            long hours = this->hoursToEatPile(piles, mid);

            // if speed is acceptable, search to the left to find
            // even smaller acceptable speed
            if (hours <= h) {
                // Save the result if no better result will be found
                answer = mid;
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }

        return answer;
    }

    private:
    long hoursToEatPile(const vector<int> &piles, int k) {
        // for each pile, count ceiling of pile / k
        // total hours to is is then the sum of the quotients
        long hours = 0;

        for (auto p: piles) {
            hours += (p + k - 1) / k;
        }
        return hours;
    }
};

static void run_test(const char *name, vector<int> piles, int h, int expected) {
    Solution sol;
    int result = sol.minEatingSpeed(piles, h);

    cout << name << ": " << result << " expected " << expected
         << (result == expected ? " OK" : " MISMATCH") << endl;
}

int main() {
    run_test("Example 1", {3, 6, 7, 11}, 8, 4);
    run_test("Example 2", {30, 11, 23, 4, 20}, 5, 30);
    run_test("Example 3", {30, 11, 23, 4, 20}, 6, 23);
    run_test("Speed 1 is enough", {1, 1, 1}, 3, 1);

    return 0;
}
