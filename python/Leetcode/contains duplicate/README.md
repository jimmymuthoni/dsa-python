### [2. Cotains Duplicate](https://leetcode.com/problems/contain-duplicate/)

Given an integer array nums, return true if any value appers at least twice in the array, and return false if every element in distict.

### Idea
- time complexity: O(n)
- space complexity: O(n)

The idea is to implement set since it only store distict values. This reduces time timplexity from 0(n^2) if we dicided to use brute force and O(nlogn) if we decied frist to compare adjacent values to O(n)