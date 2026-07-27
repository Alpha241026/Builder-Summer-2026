Pattern:
Frequency Counting / Hashing

Recognition:
Need to compare the frequency of characters (or numbers), regardless of their order.

Core Idea:
If two strings are anagrams, every character appears the same number of times.
Maintain a frequency array.
• Increment for the first string.
• Decrement for the second string.
If every frequency becomes zero, the strings are anagrams.

Time:
O(n) — One traversal of both strings.

Space:
O(1) — Frequency array of fixed size (26 for lowercase English letters).