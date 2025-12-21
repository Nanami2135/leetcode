#include <vector>
#include <deque>
#include <iostream>
using std::cout;
using std::endl;

using std::vector;
using std::deque;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == nullptr)
            return vector<vector<int>>();

        auto q = std::deque<TreeNode*>();
        q.push_back(root);

        auto level_nodes = vector<TreeNode*>();
        auto level = 0;
        vector<vector<int>> result;
        while (!q.empty()) {
            level_nodes.clear();
            level_nodes.reserve(q.size());
            auto level_size = q.size();

            vector<int> numbers;
            numbers.reserve(q.size());

            for (size_t i = 0; i < level_size; i++) {
                level_nodes.push_back(q.front());
                q.pop_front();
            }

            for (TreeNode* node : level_nodes){
                numbers.push_back(node->val);
                if (level % 2 != 0) {
                    if (node->right != nullptr) {
                        q.push_front(node->right);
                    }
                    if (node->left != nullptr) {
                        q.push_front(node->left);
                    }
                }
                if (level % 2 == 0) {
                    if (node->left != nullptr) {
                        q.push_front(node->left);
                    }
                    if (node->right != nullptr) {
                        q.push_front(node->right);
                    }
                }
            }

            result.push_back(numbers);
            level++;
        }
        return result;
    }
};


int main() {
    // Helper lambda to print the zigzag result
    auto print_result = [](const vector<vector<int>>& res) {
        cout << "[";
        for (size_t i = 0; i < res.size(); ++i) {
            cout << "[";
            for (size_t j = 0; j < res[i].size(); ++j) {
                cout << res[i][j];
                if (j + 1 < res[i].size()) cout << ",";
            }
            cout << "]";
            if (i + 1 < res.size()) cout << ",";
        }
        cout << "]" << endl;
    };

    Solution sol;

    // Test 1: Empty tree
    {
        TreeNode* root = nullptr;
        auto res = sol.zigzagLevelOrder(root);
        cout << "Test 1 (Empty tree): ";
        print_result(res);
    }

    // Test 2: Single node
    {
        TreeNode* root = new TreeNode(1);
        auto res = sol.zigzagLevelOrder(root);
        cout << "Test 2 (Single node): ";
        print_result(res);
        delete root;
    }

    // Test 3: Perfect binary tree
    //        1
    //      /   \
    //     2     3
    //    / \   / \
    //   4   5 6   7
    {
        TreeNode* n4 = new TreeNode(4);
        TreeNode* n5 = new TreeNode(5);
        TreeNode* n6 = new TreeNode(6);
        TreeNode* n7 = new TreeNode(7);
        TreeNode* n2 = new TreeNode(2, n4, n5);
        TreeNode* n3 = new TreeNode(3, n6, n7);
        TreeNode* root = new TreeNode(1, n2, n3);
        auto res = sol.zigzagLevelOrder(root);
        cout << "Test 3 (Perfect tree): ";
        print_result(res);
        delete n4; delete n5; delete n6; delete n7; delete n2; delete n3; delete root;
    }

    // Test 4: Left-skewed tree
    // 1 -> 2 -> 3 -> 4
    {
        TreeNode* n4 = new TreeNode(4);
        TreeNode* n3 = new TreeNode(3, n4, nullptr);
        TreeNode* n2 = new TreeNode(2, n3, nullptr);
        TreeNode* root = new TreeNode(1, n2, nullptr);
        auto res = sol.zigzagLevelOrder(root);
        cout << "Test 4 (Left-skewed): ";
        print_result(res);
        delete n4; delete n3; delete n2; delete root;
    }

    // Test 5: Right-skewed tree
    // 1 -> 2 -> 3 -> 4 (right children)
    {
        TreeNode* n4 = new TreeNode(4);
        TreeNode* n3 = new TreeNode(3, nullptr, n4);
        TreeNode* n2 = new TreeNode(2, nullptr, n3);
        TreeNode* root = new TreeNode(1, nullptr, n2);
        auto res = sol.zigzagLevelOrder(root);
        cout << "Test 5 (Right-skewed): ";
        print_result(res);
        delete n4; delete n3; delete n2; delete root;
    }

    // Test 6: Mixed tree
    //        1
    //      /   \
    //     2     3
    //      \   /
    //       5 4
    {
        TreeNode* n5 = new TreeNode(5);
        TreeNode* n4 = new TreeNode(4);
        TreeNode* n2 = new TreeNode(2, nullptr, n5);
        TreeNode* n3 = new TreeNode(3, n4, nullptr);
        TreeNode* root = new TreeNode(1, n2, n3);
        auto res = sol.zigzagLevelOrder(root);
        cout << "Test 6 (Mixed tree): ";
        print_result(res);
        delete n5; delete n4; delete n2; delete n3; delete root;
    }

    return 0;
}
