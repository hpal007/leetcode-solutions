"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

 

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

"""

from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
    output = []
    for i in range(len(words)):
        if x in words[i]:
            output.append(i)
    return output


word = ["leet", "code", "maz"]
x = "e"
findWordsContaining(word, x)
