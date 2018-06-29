"""
Problem Statement
One day, Jamie noticed that many English words only use the letters A and B. Examples of such words include "AB" (short for abdominal), "BAA" (the noise a sheep makes), "AA" (a type of lava), and "ABBA" (a Swedish pop sensation).


Inspired by this observation, Jamie created a simple game. You are given two s: initial and target. The goal of the game is to find a sequence of valid moves that will change initial into target. There are two types of valid moves:

Add the letter A to the end of the string.
Reverse the string and then add the letter B to the end of the string.
Return "Possible" (quotes for clarity) if there is a sequence of valid moves that will change initial into target. Otherwise, return "Impossible".

Definition
Class: ABBA
Method: canObtain
Parameters: string, string
Returns: string
Method signature: def canObtain(self, initial, target):
"""


class ABBA:
    def canObtain(self, initial, target):
        result = self.checkCanObtain(initial, target)
        if result:
            return "Possible"
        else:
            return "Impossible"

    def checkCanObtain(self, initial, target):
        if initial == target:
            return True
        if len(initial) > len(target):
            return False

        case1 = self.checkCanObtain(initial + 'A', target)
        case2 = self.checkCanObtain(initial[::-1] + 'B', target)

        return case1 or case2


str1 = "A"
str2 = "BB"
x = ABBA().canObtain(str1, str2)
print(x)
