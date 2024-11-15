def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    operators = []
    second_operands = []
    separators = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]

        width = max(len(first_operand), len(second_operand)) + 2

        first_operands.append(first_operand.rjust(width))
        operators.append(operator + " " + second_operand.rjust(width - 2))
        separators.append("-" * width)

        if show_answers:
            if operator == "+":
                answer = str(int(first_operand) + int(second_operand))
            else:
                answer = str(int(first_operand) - int(second_operand))
            answers.append(answer.rjust(width))

    first_line = "    ".join(first_operands)
    second_line = "    ".join(operators)
    separator_line = "    ".join(separators)
    arranged_problems = f"{first_line}\n{second_line}\n{separator_line}"

    if show_answers:
        answer_line = "    ".join(answers)
        arranged_problems += f"\n{answer_line}"

    return arranged_problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')