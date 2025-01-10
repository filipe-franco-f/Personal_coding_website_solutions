#include<iostream>
#include<algorithm>

/* Definition for a binary tree node. */

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 

class Solution {

typedef struct treeInfo {
  int depth;
  bool balanced;
} treeInfo;

public:
    treeInfo getTreeInfo(TreeNode* root) {
        treeInfo ti;
        if (root == NULL) {
            ti.depth = 0;
            ti.balanced = true;
        } else {
            treeInfo tiLeft = getTreeInfo(root->left);
            treeInfo tiRight = getTreeInfo(root->right);
            int max_depth = std::max(tiLeft.depth, tiRight.depth);
            int min_depth = std::min(tiLeft.depth, tiRight.depth);
            ti.depth = max_depth + 1;
            ti.balanced = max_depth - min_depth <= 1;
            if (tiLeft.balanced == false || tiRight.balanced == false) {
                ti.balanced = false;
            } 
        }
        return ti;
    }

public:
    bool isBalanced(TreeNode* root) {
        treeInfo ti = getTreeInfo(root);
        return ti.balanced;        
    }
};