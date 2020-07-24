#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n) - Linear. n^3 / n^2 = n


b)  O(n*log(n)) - Logarithmic. The outer loop is n and the inner loop is log n.


c)  O(n) - Linear. It has a recursive call for each bunny.

## Exercise II

    It seems most time efficient to use binary search tree to find target f because the value of floors increase from ground to top.

    With a time complexity of O(n*log(n)), the midpoint will divide the number of floors in this building into two equal subarray. 

    If the midpoint breaks the egg, we search the bottom half of the building for the floor that first break the egg.

    If the midpoint does not break the egg, we search the top half of the building for the floor that first break the egg.

    We always throw egg at the midpoint of each subarray.