class Student:
    class_ = "student"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def score_calculator(self, score1, score2, score3):
        total = score1 + score2 + score3
        avg_test_score = total/3
        return avg_test_score

John = Student("John", "21")
Jane = Student("Jane", "22")

print(John.class_)
print(Jane.score_calculator(6, 10, 20))