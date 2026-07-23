Pattern: Traversal

Recognition: Need to inspect every element once.

Core Idea: Initialize the answer with the first element and update it while traversing the array.

Time: O(n) - One complete pass through all n elements.

Space: O(1) - Only one extra variable (largest); memory doesn't grow with input size.





Pattern: Two Pointers (Explorer + Maintainer)

Recognition: Need to rearrange elements in-place while preserving the relative order of selected elements.

Core Idea: One pointer explores every element.
Another pointer maintains the boundary of the correctly arranged region.
Whenever a valid element is found, place it at the next position of the maintained region, then grow the boundary.

Time: O(n) — Every element is explored exactly once.

Space: O(1) — Only constant extra variables/pointers are used.





Pattern:
Running Sum / Dynamic Programming (State Transition)

Recognition:
Need to find the maximum/minimum value of a contiguous subarray or make an optimal decision while traversing once.

Core Idea:
Maintain the best subarray sum ending at the current index (local state).
At each element, there are only two legal choices:
• Start a new subarray from the current element.
• Extend the best subarray ending at the previous index.
Also maintain the best answer seen anywhere (global state).

Time:
O(n) — One pass through the array.

Space:
O(1) — Only constant extra variables are used.