# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
#
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі). Вивідіть дві
# функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.

class Student:
    name = "Daria"
    grades = [10, 10, 9, 9, 4, 7, 12, 12, 12]

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

    def list_of_grades(self):
        print(f"There is my grades list: {self.grades}")


student_daria = Student()
student_daria.say_hello()
student_daria.list_of_grades()

student_andrii = Student()
student_andrii.name = "Andrii"
student_andrii.grades = [12, 12, 2, 2, 8, 8, 8, 12, 12]
student_andrii.say_hello()
student_andrii.list_of_grades()
