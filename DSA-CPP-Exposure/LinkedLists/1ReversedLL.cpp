#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

//create and link nodes: 10 -> 20 -> 30 -> NULL
Node* createList() {
    Node* head = new Node();
    head->data = 10;
    head->next = NULL;

    Node* second = new Node();
    second->data = 20;
    second->next = NULL;

    Node* third = new Node();
    third->data = 30;
    third->next = NULL;

    head->next = second;
    second->next = third;

    return head;
}

void printList(Node* head) {
    Node* temp = head;

    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }

    cout << endl;
}

Node* reverseList(Node* head) {
    Node* prev = NULL;
    Node* curr = head;

    while (curr != NULL) {
        Node* next = curr->next;  //save the unprocessed remainder.
        curr->next = prev;        //reverse the current link.
        prev = curr;              //extend the reversed portion.
        curr = next;              //continue with the saved remainder.
    }

    return prev;  //new head of the reversed list.
}

int main() {
    Node* head = createList();

    cout << "Original list: ";
    printList(head);

    head = reverseList(head);

    cout << "Reversed list: ";
    printList(head);

    //free the nodes so this demonstration does not leak memory.
    while (head != NULL) {
        Node* del = head;
        head = head->next;
        delete del;
    }

    return 0;
}
