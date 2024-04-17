def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Storing individual parts of the formatted output
    first_line = []
    second_line = []
    dashed_line = []
    answers_line = []
    
    for problem in problems:
        # Determine the operation and split accordingly
        if '+' in problem:
            parts = problem.split('+')
            op = '+'
        elif '-' in problem:
            parts = problem.split('-')
            op = '-'
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Strip spaces and assign operands
        arg1 = parts[0].strip()
        arg2 = parts[1].strip()
        
        # Check the length of the numbers
        if len(arg1) > 4 or len(arg2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Check if both parts are digits
        if not (arg1.isdigit() and arg2.isdigit()):
            return 'Error: Numbers must only contain digits.'

    
        # Determine spacing basedd on the longest operand
        max_length = max(len(arg1), len(arg2)) + 2
        first_operand = arg1.rjust(max_length)
        second_operand = op + " " + arg2.rjust(max_length-2)
        dash = '-'*max_length

        # Append to each of line lists
        first_line.append(first_operand)
        second_line.append(second_operand)
        dashed_line.append(dash)
        
        # Compute answer
        if show_answers:
            if op == '+':
                answer = int(arg1) + int(arg2)
            else:
                answer = int(arg1) - int(arg2)
            answers_line.append(str(answer).rjust(max_length))
        
    # Join the problem compenents into the final answer with four spaces between subproblems
    result = f"{ '    '.join(first_line) }"
    result += f"\n{ '    '.join(second_line) }"
    result += f"\n{ '    '.join(dashed_line) }"
    if show_answers:
        result += f"\n{ '    '.join(answers_line) }"

    return result

print(f'\n\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}\n\n')
print(f'\n\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}\n\n')