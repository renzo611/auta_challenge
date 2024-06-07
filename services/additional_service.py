
class AdditionalService:
    @staticmethod
    def is_balanced_word(word: str):
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in word:
            if char in matching_brackets.values():
                stack.append(char)
            elif char in matching_brackets.keys():
                if stack == [] or stack.pop() != matching_brackets[char]:
                    return False
            else:
                continue
        return stack == []