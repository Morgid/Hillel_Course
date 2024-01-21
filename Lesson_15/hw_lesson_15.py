# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, множення, ділення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class Calculator:

    @staticmethod
    def print_calculator_presentation():
        print("Привіт я калькулятор")

    def addition(self, number_1: int | float, number_2: int | float) -> int | float:
        result = number_1 + number_2
        return result

    def subtract(self, number_1: int | float, number_2: int | float) -> int | float:
        result = number_1 - number_2
        return result

    def multiplication(self, number_1: int | float, number_2: int | float) -> int | float:
        result = number_1 * number_2
        return result

    def division(self, number_1: int | float, number_2: int | float) -> int | float:
        if number_2 == 0:
            return "Ділити на 0 не можна"
        else:
            result = round((number_1 / number_2), 2)
            return result


calculate_obj = Calculator()
calculate_obj.print_calculator_presentation()

result_add = calculate_obj.addition(2, 2)
result_sub = calculate_obj.subtract(5, 2)
result_mult = calculate_obj.multiplication(10, 2)
result_div = calculate_obj.division(10, 1)

print(f"Додавання: {result_add}")
print(f"Віднімання: {result_sub}")
print(f"Множення: {result_mult}")
print(f"Ділення: {result_div}")
