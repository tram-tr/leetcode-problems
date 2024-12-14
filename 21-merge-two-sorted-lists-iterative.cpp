/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
// Iterative Solution
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* res = new ListNode();
        ListNode* ptr = res;
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                res->next = new ListNode(list1->val);
                list1 = list1->next;
            }
            else {
                res->next = new ListNode(list2->val);
                list2 = list2->next;
            }
            res = res->next;
        }
        while (list1 != nullptr) {
            res->next = new ListNode(list1->val);
            list1 = list1->next;
            res = res->next;
        }
        while (list2 != nullptr) {
            res->next = new ListNode(list2->val);
            list2 = list2->next;
            res = res->next;
        }
        return ptr->next;
    }
};
