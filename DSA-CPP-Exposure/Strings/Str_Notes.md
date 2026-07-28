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





Pattern:
String Traversal

Recognition:
Need to find the common beginning shared by all strings.

Core Idea:
Take the first string as the reference.
Compare one character position at a time with every other string.
If every string matches, extend the prefix.
Stop immediately when:
• Any string ends.
• Any character differs.

Time:
O(N × M)

N = number of strings
M = length of shortest/common checked prefix

Space:
O(1)