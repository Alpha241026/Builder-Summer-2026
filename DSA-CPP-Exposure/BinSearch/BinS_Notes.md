Pattern:
Binary Search

Recognition:
Sorted array or monotonic condition where half the search space can be eliminated after every comparison.

Core Idea:
Maintain the invariant:
"If the target exists, it is inside the current search interval."

Maintain two boundaries:
l → first possible index
u → last possible index

Every iteration:
1. Inspect the middle.
2. Eliminate one impossible half.
3. Preserve the invariant.

Time:
O(log n)

Space:
O(1)