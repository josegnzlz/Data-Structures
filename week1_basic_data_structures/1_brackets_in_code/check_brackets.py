# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def reverse(char):
    if char == ")":
        c = "("
    elif char == "]":
        c = "["
    elif char == "}":
        c = "{"
    return c


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            br = Bracket(next, i+1)
            opening_brackets_stack.append(br)

        if next in ")]}":
            # Process closing bracket, write your code here
            br = Bracket(next, i+1)
            if len(opening_brackets_stack) > 0 and reverse(next) == opening_brackets_stack[-1].char:
                opening_brackets_stack.pop()
            elif len(opening_brackets_stack) == 0:
                return br.position
            else:
                return br.position
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0].position
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
