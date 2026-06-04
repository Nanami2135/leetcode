#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using std::cout;
using std::endl;
using std::vector;

class Solution {
  public:
    int findMaximizedCapital(int k, int w, vector<int> &profits,
                             vector<int> &capital) {
        vector<std::pair<int, int>> pc_min_heap_capital{};
        pc_min_heap_capital.reserve(profits.size());
        for (size_t i = 0; i < profits.size(); ++i) {
            pc_min_heap_capital.push_back(std::pair<int,int>{profits[i], capital[i]});
        }


        // Order by capital in ascending order -- pick efficiently the
        // available projects
        auto greater_capital = [](std::pair<int,int> a, std::pair<int,int> b) {return a.second > b.second;};

        // Make a min heap of project/capital pairs ordered by capital
        std::make_heap(pc_min_heap_capital.begin(), pc_min_heap_capital.end(), greater_capital);


        // Take project if we can:
        //  - still have projects left to take
        //  - the project with min capital (top of the heap) is less/equal
        //    than our current capital w
        auto profits_max_heap = std::priority_queue<int>();

        while (k > 0) {
            // Take all projects available at our capital level
            // and push them to new heap of project profits
            while (pc_min_heap_capital.size() > 0 && pc_min_heap_capital[0].second <= w) {
                int profit = pc_min_heap_capital[0].first;

                std::pop_heap(pc_min_heap_capital.begin(), pc_min_heap_capital.end(), greater_capital);
                pc_min_heap_capital.pop_back();

                profits_max_heap.push(profit);
            }

            // No projects available
            if (profits_max_heap.size() == 0)
                break;

            // Greedy step -- take best available profit
            w += profits_max_heap.top();
            profits_max_heap.pop();

            --k;
        }

        return w;
    }
};

static void run_test(const char *name, int k, int w, vector<int> profits,
                     vector<int> capital, int expected) {
    Solution sol;
    int result = sol.findMaximizedCapital(k, w, profits, capital);

    cout << name << ": " << result << " expected " << expected
         << (result == expected ? " OK" : " MISMATCH") << endl;
}

int main() {
    run_test("Example 1", 2, 0, {1, 2, 3}, {0, 1, 1}, 4);
    run_test("Example 2", 3, 0, {1, 2, 3}, {0, 1, 2}, 6);

    run_test("No affordable projects", 2, 0, {1, 2}, {1, 2}, 0);
    run_test("Can choose fewer than k useful projects", 5, 1, {2, 3}, {1, 10},
             3);
    run_test("Zero selections", 0, 10, {1, 2, 3}, {0, 0, 0}, 10);
    run_test("Project order matters by capital", 3, 1, {1, 2, 10, 3},
             {0, 1, 3, 2}, 16);

    return 0;
}
