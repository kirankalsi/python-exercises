def grade_calculator(hwk_mark, ass_mark, final_mark):
    if hwk_mark > 25 or ass_mark > 50 or final_mark > 100:
        return False
    if hwk_mark < 0 or ass_mark < 0 or final_mark < 0:
        return False
    avg_mark = (((hwk_mark/25) + (ass_mark/50) + (final_mark/100))/3)*100
    return avg_mark
    
def grade_boundary(avg_mark):
    final_letter_grade = ""
    if avg_mark >= 90:
        final_letter_grade = "A*"
    elif avg_mark >= 80:
        final_letter_grade = "A"
    elif avg_mark >= 70:
        final_letter_grade = "B"
    elif avg_mark >= 60:
        final_letter_grade = "C"
    elif avg_mark >= 50:
        final_letter_grade = "D"
    else:
        final_letter_grade = "F"
    return final_letter_grade

name = input("Enter name: ")
hwk_mark = int(input("Enter homework mark out of 25: "))
ass_mark = int(input("Enter assessment mark out of 50: "))
final_mark = int(input("Enter final mark out of 100: "))

grade = grade_calculator(hwk_mark, ass_mark, final_mark)
if grade == False:
    print("Invalid scores entered")
else:
    letter_grade = grade_boundary(grade)
    print(f"{name} got {grade}% which is a {letter_grade}")