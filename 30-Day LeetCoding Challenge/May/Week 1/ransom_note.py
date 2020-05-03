class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for m in magazine:
            if m not in mag:
                mag[m] = 1
            else:
                mag[m] += 1

        for letter in ransomNote:
            check = mag.get(letter)
            if check:
                mag[letter] -= 1
            else:
                return False
        return True