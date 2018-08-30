from .a_stack import Stack


def multi_bracket_validation(input):

    if input:
        PAIR = {
            ']': '[',
            '}': '{',
            ')': '(',
        }

        stack = Stack()

        i = 0
        while i < len(input):
            if input[i] == '{' or input[i] == '[' or input[i] == '(':
                # import pdb; pdb.set_trace()
                stack.push(input[i])
                print(stack._top)
            elif input[i] == '}' or input[i] == ']' or input[i] == ')':
                if PAIR[input[i]] == stack._top._data:
                    stack.pop()
                else:
                    return False

            i += 1

        if stack._length == 0:
            return True
        else:
            return False
    else:
        return False
