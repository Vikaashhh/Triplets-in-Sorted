# 📅 Day 51 – GFG 160 Days DSA Challenge
### 🧩 Problem: Count Triplets with Sum Equal to Target
### 💻 Language: Python
### 📈 Difficulty: Medium

## 📝 Problem Statement:
Given an array of integers and a target sum, determine the total number of triplets (i, j, k) such that:

arr[i] + arr[j] + arr[k] == target

And i < j < k

## 🚀 Optimized Approach – Two Pointers (after Sorting):
1. Sort the array.

2. For each element arr[i], use two-pointer technique to find all valid pairs (arr[left], arr[right]) such that their sum equals target - arr[i].

3. Special care is taken when duplicates are involved (using frequency count logic).

4. Handles both:

- Triplets with all equal elements.

- Triplets with duplicates on either side.

## 📊 Time & Space Complexity:
Time Complexity: O(n²)

Space Complexity: O(1) – apart from sorting.

## 📢 Hashtags:
#Day51 #gfg160 #geekstreak2025
#twopointertechnique #dsainpython #tripletcount
#framesbyvikash #codingchallenge #100daysofcode #developerjourney
