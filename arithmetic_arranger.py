def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    operators = []
    first_line_numbers = []
    second_line_numbers = []

    for problem in problems:
        p = problem.split()
        first_line_numbers.append(p[0])
        operators.append(p[1])
        second_line_numbers.append(p[2])

    for operator in operators:
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

    numbers = '0123456789'
    for number in first_line_numbers + second_line_numbers:
        if not all(char in numbers for char in number):
            return 'Error: Numbers must only contain digits.'

    for number in first_line_numbers + second_line_numbers:
        if len(number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    first_line = ''
    second_line = ''
    dashes = ''
    answers = ''

    for i in range(len(problems)):
        first = first_line_numbers[i]
        operator = operators[i]
        second = second_line_numbers[i]
        
        if len(first) < len(second):
            first = first.rjust(len(second))
        else:
            second = second.rjust(len(first))
        
        width = max(len(first), len(second)) + 2
        first_line += first.rjust(width) + '    '
        second_line += operator + ' ' + second + '    '
        dashes += '-' * width + '    '
        
        if show_answers:
            if operator == '+':
                answer = str(int(first_line_numbers[i]) + int(second_line_numbers[i]))
            else:
                answer = str(int(first_line_numbers[i]) - int(second_line_numbers[i]))
            answers += answer.rjust(width) + '    '

    problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip()
    if show_answers:
        problems += '\n' + answers.rstrip()

    return problems

print(f'{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')
