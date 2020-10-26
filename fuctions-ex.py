name = input("Enter name: ")
hwk_mark = int(input("Enter homework mark out of 25: "))
ass_mark = int(input("Enter assessment mark out of 50: "))
final_mark = int(input("Enter final mark out of 100: "))

def grade(name, hwk_mark, ass_mark, final_mark):
    avg_mark = ((((hwk_mark/25) + (ass_mark/50) + (final_mark/100))/3)*100)
    
    if avg_mark >= 90:
        print(name, "achieved", ''.join((str(avg_mark),'%')), "A*")
    elif avg_mark >= 80:
        print(name, "achieved", ''.join((str(avg_mark),'%')), "A")
    elif avg_mark >= 70:
        print(name, "achieved", ''.join((str(avg_mark),'%')), "B")
    elif avg_mark >= 60:
        print(name, "achieved", ''.join((str(avg_mark),'%')), "C")
    elif avg_mark >= 50:
        print(name, "achieved", ''.join((str(avg_mark),'%')), "D")
    else:
        print(name, "achieved", ''.join((str(avg_mark),'%')), "F")
        

grade(name, hwk_mark, ass_mark, final_mark)