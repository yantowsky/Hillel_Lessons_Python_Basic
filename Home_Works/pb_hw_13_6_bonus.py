class TemperatureValueError(Exception):
    pass


class TemperatureConverter:
    def validate(self, celsius):
        if celsius < -273.15:
            raise TemperatureValueError("Invalid temperature value")

    def convert_celsius_to_fahrenheit(self, celsius):
        try:
            self.validate(celsius)

        except TemperatureValueError as e:
            return e

        else:
            return celsius * 9 / 5 + 32


# Перевірка:
converter = TemperatureConverter()
result_1 = converter.convert_celsius_to_fahrenheit(25)  # Очікуваний результат: 77.0
print(result_1)

result_2 = converter.convert_celsius_to_fahrenheit(
    -300)  # Очікуваний результат: TemperatureValueError: Invalid temperature value
print(result_2)
