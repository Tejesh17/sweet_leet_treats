/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* p=NULL;
    struct ListNode* q=NULL;

    while(head!=NULL){
        p= head;
        head=head->next;
        p->next = q;
        q=p;
    }
    return p;
    
}