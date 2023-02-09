// Time:  O(n)
// Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 // Two pointers solution.
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        if (!head) {
            return nullptr;
        }

        auto dummy = new ListNode{0};
        dummy->next = head;

        auto left = dummy, right = head;
        while (right->next) {
            if (right->val != 9) {
                left = right;
            }
            right = right->next;
        }

        if (right->val != 9) {
            ++right->val;
        } else {
            ++left->val;
            right = left->next;
            while (right) {
                right->val = 0;
                right = right->next;
            }
        }

        if (dummy->val == 0) {
            head = dummy->next;
            delete dummy;
            return head;
        }

        return dummy;
    }
};

// Time:  O(n)
// Space: O(1)
class Solution2 {
public:
    ListNode* plusOne(ListNode* head) {
        auto rev_head = reverseList(head);

        auto curr = rev_head;
        int carry = 1;
        while (curr && carry) {
            curr->val += carry;
            carry = curr->val / 10;
            curr->val %= 10;
            if (carry && !curr->next) {
                curr->next = new ListNode(0);
            }
            curr = curr->next;
        }

        return reverseList(rev_head);
    }

private:
    ListNode* reverseList(ListNode* head) {
        ListNode dummy{0};
        auto curr = head;

        while (curr) {
            auto tmp = curr->next;
            curr->next = dummy.next;
            dummy.next = curr;
            curr = tmp;
        }

        return dummy.next;
    }
};
