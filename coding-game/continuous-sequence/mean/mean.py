# https://www.codingame.com/clashofcode/clash/report/15457837ed283a112cc0fe14186505580aa9a79

Calculate a running mean of a sequence of integers of size L given a window size W.

A more detailed explanation: given a sequence of size L of integers calculate the average of W numbers by sliding from the beginning of the sequence to its end in steps of size 1.

Window size W cannot exceed the length of the sequence L.
Input
Line 1: An integer L equal to the length of the sequence.
Line 2: An integer W equal to the window size.
Line 3: Space separated sequence of integers for calculating the running mean.
Output
Space separated sequence of averaged values in floating point format with one decimal place.

There will be no rounding ambiguity.
Constraints
1 ≤ L ≤ 50
1 ≤ W ≤ L
Each integer in the sequence does not exceed 10.
Example
Input

8
3
1 2 3 4 5 6 7 8

Output

2.0 3.0 4.0 5.0 6.0 7.0

# ====


Standard Output Stream:

8
5
1
2
3
4
5
6
7
8

Failure
Found:

8

Expected:

3.0 4.0 5.0 6.0

# ==== 


Standard Output Stream:

15
1
5
4
1
3
2
3
4
2
6
1
3
7
8
5
6

Failure
Found:

15

Expected:

5.0 4.0 1.0 3.0 2.0 3.0 4.0 2.0 6.0 1.0 3.0 7.0 8.0 5.0 6.0


# ===


Standard Output Stream:

15
15
5
6
8
9
4
2
4
4
7
9
6
6
5
3
5

Failure
Found:

15

Expected:

5.5

