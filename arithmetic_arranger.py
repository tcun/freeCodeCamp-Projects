def arithmetic_arranger(problems, show = False):
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for i in problems:
      items = i.split()
      num_1 = items[0]
      num_2 = items[-1]
      symbol = items[1]

      width = max(len(num_1), len(num_2)) + 2

      if not num_1.isdigit() or not num_2.isdigit():
        return "Error: Numbers must only contain digits."

      else:
        if symbol == "+":
          answer = int(num_1) + int(num_2)
        elif symbol == "-":
          answer = int(num_1) - int(num_2)
        else:
          return "Error: Operator must be '+' or '-'."

      if len(num_1) > 4 or len(num_2) > 4:
        return "Error: Numbers cannot be more than four digits."

      first_line += str(num_1).rjust(width)
      second_line += symbol + str(num_2).rjust(width - 1)
      dash_line += "-" * width
      answer_line += str(answer).rjust(width)

      if len(problems) >= 1:
        first_line += "    "
        second_line += "    "
        dash_line += "    "
        answer_line += "    "
      

      if show == True:
        arranged_problems = (first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip() + "\n" + answer_line.rstrip())
      else:
        arranged_problems = (first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip())

  return arranged_problems