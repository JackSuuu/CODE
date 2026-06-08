#include <cstdint>
#include <cstdio>
#include <iostream>
using namespace std;

//  Definition for singly-linked list.
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int main() {
    ListNode* head = new ListNode(1);
    ListNode* second_node = new ListNode(2);
    ListNode* third_node = new ListNode(3);

    head->next = second_node;
    second_node->next = third_node;

    ListNode* cur = head;

    while (cur != nullptr)
    {
        cout << cur->val << " >> ";
        cur = cur->next;
    }

    return 0;
}