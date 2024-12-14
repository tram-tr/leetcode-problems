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
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode* ans = &head;

        int carry = 0;
        while (carry > 0 || l1 || l2) {
            carry = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            ans->next = new ListNode(carry % 10);
            ans = ans->next;
            carry = carry / 10;

            if (l1) 
                l1 = l1->next;
            if (l2)
                l2 = l2->next;
        }

        return head.next;
    }
};
