Pattern:
Linked List Reversal (Iterative)


Recognition:
Reverse the direction of links between nodes
without creating a new list.


Core Idea:
Maintain three pointers:
prev -> already-reversed portion
curr -> current node
next -> saved remainder


Every iteration:
1. Save curr->next in next.
2. Point curr->next to prev.
3. Advance prev to curr.
4. Advance curr to next.


After the loop:
Update head to prev.


Time:
O(n)


Space:
O(1) auxiliary space





Pattern:
Middle of the Linked List (Slow/Fast Pointers)


Recognition:
Find the middle node of a linked list in a single traversal.


Core Idea:
Maintain two pointers:

slow -> moves one node at a time

fast -> moves two nodes at a time


Every iteration:
1. Advance slow by one node.
2. Advance fast by two nodes.
3. Stop when fast or fast->next reaches NULL.


Answer:
slow points to the middle node.

For an even number of nodes, returns the second middle.


Time:
O(n)


Space:
O(1) auxiliary space





Pattern:
Linked List Cycle (Floyd's Cycle Detection)


Recognition:
Determine whether a linked list contains a cycle.


Core Idea:
Maintain two pointers:

slow -> moves one node at a time

fast -> moves two nodes at a time


Every iteration:
1. Advance slow by one node.
2. Advance fast by two nodes.
3. If slow == fast, a cycle exists.


Stopping Condition:
If fast or fast->next becomes NULL, no cycle exists.


Time:
O(n)


Space:
O(1) auxiliary space