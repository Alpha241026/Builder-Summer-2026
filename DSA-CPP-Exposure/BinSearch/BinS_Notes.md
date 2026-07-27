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





Pattern:
Binary Search Variant (Lower Bound)

Recognition:
Need the first position where a condition becomes true, not just whether an element exists.

Core Idea:
Maintain the first valid candidate found so far.
Whenever arr[mid] >= x:
• mid is a valid candidate.
• Store it.
• Continue searching the left half for an earlier valid index.
Otherwise:
• Eliminate the left half and search right.

Time:
O(log n)

Space:
O(1)





Pattern:
Binary Search Variant (Search Insert Position)

Recognition:
Need to return the position where an element exists or should be inserted while maintaining sorted order.

Core Idea:
This is exactly the Lower Bound problem.
Return the first index where arr[i] >= target.
If no such index exists, return n.

Time:
O(log n)

Space:
O(1)