def beautify(solution):
    def remove_four_in_a_row(solution):
        for j in range(len(solution) - 3):
            temp = solution[j]
            if j + 4 > len(solution):
                break
            elif (solution[j + 1] == temp and
                    solution[j + 2] == temp and
                    solution[j + 3] == temp):
                del solution[j:j + 3]

    def reverse_three_in_a_row(solution):
        for j in range(len(solution) - 2):
            temp = solution[j]
            if j + 3 > len(solution):
                break
            elif (solution[j + 1] == temp and
                    solution[j + 2] == temp):
                del solution[j:j+2]
                solution[j] = temp + "'"

    def convert(solution):
        newSolution = []
        for i in range(len(solution)):
            if solution[i] == 'L':
                solution[i] = 'Left'
            elif solution[i] == 'R':
                solution[i] = 'Right'
            elif solution[i] == 'U':
                solution[i] = 'Up'
            elif solution[i] == 'D':
                solution[i] = 'Down'
            elif solution[i] == 'F':
                solution[i] = 'Front'
            elif solution[i] == 'B':
                solution[i] = 'Back'
            elif solution[i] == 'C':
                solution[i] = 'Rotate Clockwise'
            elif solution[i] == "L'":
                solution[i] = 'Left Inverted'
            elif solution[i] == "R'":
                solution[i] = 'Right Inverted'
            elif solution[i] == "U'":
                solution[i] = 'Up Inverted'
            elif solution[i] == "D'":
                solution[i] = 'Down Inverted'
            elif solution[i] == "F'":
                solution[i] = 'Front Inverted'
            elif solution[i] == "B'":
                solution[i] = 'Back Inverted'
            elif solution[i] == "C'":
                solution[i] = 'Rotate Counter-Clockwise'

    def double_up(solution):
        for j in range(len(solution) - 1):
            temp = solution[j]
            if j + 2 > len(solution):
                break
            elif (solution[j + 1] == temp):
                del solution[j+1]
                solution[j] = temp + " Twice"

    remove_four_in_a_row(solution)
    reverse_three_in_a_row(solution)
    print(solution)
    convert(solution)
    double_up(solution)
