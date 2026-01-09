#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::unordered_map;
using std::unordered_set;
using std::vector;
using std::cout;
using std::unique_ptr;
using std::make_unique;

// template <typename T>
// void print2d(const unordered_map<int, vector<T>>& umap) {
//     for (const auto& pair : umap) {
//         cout << "Key: " << pair.first << " | Values: ";
//         for (const auto& element : pair.second) {
//             cout << element << " | ";
//         }
//         cout << "\n";
//     }
// }

class Solution {
private:
    unique_ptr<unordered_set<int>> visited;
    void dfs(const int& i, const unordered_map<int, vector<int>>& graph) {
        auto stack = vector<int>{i};
        this->visited->insert(i);

        while (stack.size() > 0) {
            auto node_index = stack.back();
            stack.pop_back();

            const auto& children = graph.at(node_index);
            printf("At node %d with %zu children\n", node_index, children.size());
            for (auto& child : children) {
                if (this->visited->contains(child)) continue;
                stack.push_back(child);
                this->visited->insert(child);
            }
        }

        printf("Starting dfs at %d\n", i);
    }

public:
    Solution() : visited(make_unique<unordered_set<int>>()) {}
    int findCircleNum(vector<vector<int>> &isConnected) {
        auto graph = unordered_map<int, vector<int>>();

        for (size_t i = 0; i < isConnected.size(); i++) {
            graph[i] = vector<int>();
        }

        for (size_t i = 0; i < isConnected.size() - 1; i++) {
            for (size_t j = i + 1; j < isConnected.size(); j++) {
                printf("At node (%zu, %zu)\n", i, j);
                // c -- connection
                int& c = isConnected[i][j];
                if (c == 1) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }
        // print2d(graph);

        int num_provinces = 0;
        for (size_t city = 0; city < isConnected.size(); city++) {
            if (this->visited->contains(city)) {
                continue;
            }
            dfs(city, graph);
            num_provinces++;
        }

        return num_provinces;
    }
};


int main() {
    // Create 2d matrix of 1s
    auto example1 = vector<vector<int>>{
        {1, 1, 0, 1},
        {1, 1, 0, 0},
        {0, 0, 1, 0},
        {1, 0, 0, 1},
    };
    Solution *s = new Solution();
    int result = (*s).findCircleNum(example1);
    printf("Result: %d\n", result);

    delete s;

    return result;
}
