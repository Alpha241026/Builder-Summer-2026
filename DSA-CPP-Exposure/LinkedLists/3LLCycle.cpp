#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

bool hasCycle(Node* head) {
    Node* slow = head;
    Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) {
            return true;
        }
    }

    return false;
}

int main() {
    Node* head = new Node{1, NULL};
    head->next = new Node{2, NULL};
    head->next->next = new Node{3, NULL};
    head->next->next->next = new Node{4, NULL};

    // Create a cycle: node 4 points back to node 2.
    head->next->next->next->next = head->next;

    cout << (hasCycle(head) ? "Cycle detected" : "No cycle") << endl;

    // Break the cycle before deleting nodes.
    head->next->next->next->next = NULL;

    while (head != NULL) {
        Node* del = head;
        head = head->next;
        delete del;
    }

    return 0;
}