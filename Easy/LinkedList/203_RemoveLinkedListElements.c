/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* start = head;
    struct ListNode* back = NULL;
    while(start != NULL && start->val == val){
        start = start->next;
        head = start;
        back = start;
    }

    while(start!=NULL){
        if(start->val == val){
            back->next = start->next;
            free(start);
        }else{
            back = start;
        }
        start = back->next;
    }
    return head;
}