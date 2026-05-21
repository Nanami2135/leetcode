#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

class Solution {
  public:
    vector<int> findClosestElements(vector<int> &arr, int k, int x) {
        // find element id that has minimal distance from x
        int min_id = 0;
        int min_distance = std::abs(arr[0] - x);
        // TODO: min can be optimized -- break when distance start to increase
        // or be equal
        // but verify that underlying number is different
        for (size_t i = 0; i < arr.size(); ++i) {
            int dist = std::abs(arr[i] - x);
            if (dist < min_distance) {
                min_distance = dist;
                min_id = i;
            }
        }

        // Now allocate a sliding window of size k
        // A window should start from min_id and to the left
        // as much as possible
        // The idea is that sliding window has to contain min_id
        // But to give priority to smaller numbers, we have to search
        // best sliding window from left to right
        // So if an optimal sliding window is found, we
        // can immediately stop, assuming it contains lesser
        // numbers rather than larger ones

        // min_id - (k - 1) => allocate k - 1 element to the left of min_id
        // or stop at 0 using std::max
        int left_id = std::max(0, min_id - k + 1);
        // allocate remaining elements k - (min_id - left_id + 1), starting from min_id =>
        // min_id + k - (min_id - left_id + 1), or take right bound if it's reached first, using std::max
        int arr_size = static_cast<int>(arr.size());
        int right_id = std::min(arr_size - 1, min_id + k - (min_id - left_id + 1));

        // Now slide the window from left to right
        // if leftmost distance from current sliding window is less than
        // right element outside of the window, stop
        // also stop if array limit is reached
        while (true) {
            // Stop if array limit is reached
            if (right_id == arr_size - 1)
                break;
            // Stop if right element outside has larger distance than left window edge
            // no point to continue
            auto left_edge_distance = std::abs(arr[left_id] - x);
            auto right_element_distance = std::abs(arr[right_id + 1] - x);
            if (left_edge_distance <= right_element_distance)
                break;

            // Advance the window to the right
            ++left_id;
            ++right_id;
        }

        std::vector<int> result;
        result.reserve(right_id - left_id + 1);
        for (int i = left_id; i <= right_id; ++i) {
            result.push_back(arr[i]);
        }
        return result;
    }
};

static void runTest(vector<int> arr, int k, int x, vector<int> expected) {
    Solution sol;
    vector<int> result = sol.findClosestElements(arr, k, x);

    cout << "arr = ";
    for (int v : arr)
        cout << v << " ";
    cout << "| k = " << k << ", x = " << x << "\n";

    cout << "expected: ";
    for (int v : expected)
        cout << v << " ";
    cout << "\n";

    cout << "result:   ";
    for (int v : result)
        cout << v << " ";
    cout << "\n";

    cout << (result == expected ? "PASS" : "FAIL") << "\n\n";
}

int main() {
    runTest({1, 2, 3, 4, 5}, 4, 3, {1, 2, 3, 4});
    runTest({1, 2, 3, 4, 5}, 4, -1, {1, 2, 3, 4});
    runTest({1, 1, 2, 3, 4, 5}, 4, -1, {1, 1, 2, 3});
    runTest({0, 1, 1, 1, 2, 3, 6, 7, 8, 9}, 9, 4, {0, 1, 1, 1, 2, 3, 6, 7, 8});

    return 0;
}
