# 1.1 isUnique

## Description
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure?

## Approach 1: Using Set

### Explanantion
In this approach, we use **set()** in which we store all the alphabets of the given *String*. Then, we can simply return the *boolean* value by checking if the length of the *String* is equal to the characters present in the **set()**. As set only stores unique value so if the set is equal to the length of string then it returns as *True* else *False*.

### Complexity
#### Time Complexity:

- O(n), where n is the length of the string.
- This is due to:
    - Creating a set from the string: O(n) time on average for most Python set implementations.
    - Comparing lengths: O(1) time, as it's a simple comparison.
#### Space Complexity:

- O(n), considering the worst-case scenario.
- It involves:
    - The set: It might hold up to n unique characters in the worst case.
    - Additional space: While constant, there's some extra space used for variables and function calls.
### Python Code

```python
def isUnique(string):
    return len(set(string)) == len(string)

string = "kwjxbhewybc"
result = isUnique(string)
print(result)
```

## Approach 2: Without using additional Data Structure

### Explanantion
In above approach, we use **set()** as an additional data structure to find whether the *string* has unique elements or not but in this method we checks if a *string* has all unique characters using nested loops. The outer loop iterates through each character, and the inner loop compares it with all subsequent characters. If a duplicate is found, the function returns *False*.

### Complexity
#### Time Complexity:

- O(n^2), where n is the length of the string.
- The nested loops iterate n * (n-1) / 2 times in the worst case (every character is compared with all subsequent characters).
- This can be inefficient for larger strings.
#### Space Complexity:

- O(1), constant space complexity.
- The function uses a fixed amount of extra space for variables like i, j, and the return value, regardless of the input string length.
### Python Code

```python
def isUnique(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

string = "kwjxbhewybc"
result = isUnique(string)
print(result)
```
