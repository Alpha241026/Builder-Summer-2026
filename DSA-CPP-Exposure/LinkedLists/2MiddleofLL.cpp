#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* middleNode(Node* head) {
    Node* slow = head;
    Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}

int main() {
    Node* head = new Node{1, NULL};
    head->next = new Node{2, NULL};
    head->next->next = new Node{3, NULL};
    head->next->next->next = new Node{4, NULL};
    head->next->next->next->next = new Node{5, NULL};

    Node* mid = middleNode(head);
    cout << "Middle node: " << mid->data << endl;

    while (head != NULL) {
        Node* del = head;
        head = head->next;
        delete del;
    }

    return 0;
}