import stacks1


def is_match(ch1, ch2):

    match_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = stacks1.Stack()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size()==0

print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{hh+kk}"))