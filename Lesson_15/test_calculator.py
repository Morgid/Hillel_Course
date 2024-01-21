# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми запустили тест
#  та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
#  використайте вже відому вам бібліотеку дататайм

import pytest
from datetime import datetime
from hw_lesson_15 import Calculator


class TestCalculator:

    @classmethod
    def setup_class(cls):
        with open("log.txt", "a") as file:
            file.write(f"{50 * "*"}\n")
            file.write(f"Start Test at {datetime.now()} \n")

    @classmethod
    def teardown_class(cls):
        with open("log.txt", "a") as file:
            file.write("\n")
            file.write(f"End Test at {datetime.now()} \n")
            file.write(f"{50 * "*"}\n")

    @pytest.mark.parametrize("number_1, number_2, result", [
        pytest.param(2, 2, 4, id="Positive int"),
        pytest.param(21.1, 0.9, 22, id="Positive float"),
        pytest.param(-2, 2, 0, id="Result 0"),
        pytest.param(-2, -2, -4, id="Negative numbers"),
        pytest.param(23, 0, 23, id="Using 0")])
    def test_calculator_addition(self, number_1, number_2, result):
        assert Calculator.addition(self, number_1, number_2) == result

    @pytest.mark.parametrize("number_1, number_2, result", [
        pytest.param(2, 2, 1, id="Positive int"),
        pytest.param(21.1, 0.9, 23.44, id="Positive greater than zero with float "),
        pytest.param(-2, 2, -1, id="Result int with minus"),
        pytest.param(33, -125, -0.26, id="Less than zero with float"),
        pytest.param(23, 0, "Ділити на 0 не можна", id="Division by Zero")])
    def test_calculator_division(self, number_1, number_2, result):
        assert Calculator.division(self, number_1, number_2) == result
