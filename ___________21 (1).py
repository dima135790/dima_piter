# TODO Написать 3 класса с документацией и аннотацией типов
    # TODO работоспособность экземпляров класса проверить с помощью doctest


import doctest

class WindowSill:
    """
    Абстрактный класс, представляющий подоконник.

    Атрибуты:
        length (int): Длина подоконника в сантиметрах.
        width (int): Ширина подоконника в сантиметрах.
        max_weight (int): Максимальный вес, который может выдержать подоконник, в килограммах.
    """
    def __init__(self, length: int, width: int, max_weight: int) -> None:
        """
        Конструктор класса WindowSill.

        Args:
            length (int): Длина подоконника в сантиметрах.
            width (int): Ширина подоконника в сантиметрах.
            max_weight (int): Максимальный вес, который может выдержать подоконник, в килограммах.

        Raises:
            ValueError: Если длина, ширина или максимальный вес отрицательные.
        """
        if length <= 0:
            raise ValueError("Длина должна быть положительной")
        if width <= 0:
            raise ValueError("Ширина должна быть положительной")
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть положительным")

        self.length = length
        self.width = width
        self.max_weight = max_weight

    def place_item(self, item_weight: int) -> None:
        """
        Размещает предмет на подоконнике.

        Args:
            item_weight (int): Вес предмета, который нужно разместить на подоконнике, в килограммах.

        Raises:
            ValueError: Если вес предмета превышает максимальный вес, который может выдержать подоконник.

        Examples:
            >>> sill = WindowSill(length=150, width=30, max_weight=20)
            >>> sill.place_item(item_weight=5)
        """
        if item_weight > self.max_weight:
            raise ValueError("Вес предмета превышает максимальный вес для подоконника")
        ...

    def clean(self) -> None:
        """
        Очищает подоконник.

        Examples:
            >>> sill = WindowSill(length=150, width=30, max_weight=20)
            >>> sill.clean()
        """
        ...

    def get_area(self) -> int:
        """
        Возвращает площадь подоконника.

        Returns:
           int: Площадь подоконника в квадратных сантиметрах.

        Examples:
            >>> sill = WindowSill(length=150, width=30, max_weight=20)
            >>> sill.get_area()
            4500
        """
        return self.length * self.width

class Bed:
    """
    Абстрактный класс, представляющий кровать.

    Атрибуты:
        length (int): Длина кровати в сантиметрах.
        width (int): Ширина кровати в сантиметрах.
        max_occupants (int): Максимальное количество человек, которое может поместиться на кровати.
    """

    def __init__(self, length: int, width: int, max_occupants: int) -> None:
        """
        Конструктор класса Bed.

        Args:
            length (int): Длина кровати в сантиметрах.
            width (int): Ширина кровати в сантиметрах.
            max_occupants (int): Максимальное количество человек, которое может поместиться на кровати.

        Raises:
             ValueError: Если длина, ширина или максимальное количество проживающих отрицательное.
        """
        if length <= 0:
            raise ValueError("Длина должна быть положительной")
        if width <= 0:
            raise ValueError("Ширина должна быть положительной")
        if max_occupants <= 0:
            raise ValueError("Максимальное количество проживающих должно быть положительным")

        self.length = length
        self.width = width
        self.max_occupants = max_occupants

    def sleep(self, occupants: int) -> None:
        """
        Положить спать определенное количество человек на кровать.

        Args:
            occupants(int): Количество человек, спящих на кровати.

        Raises:
            ValueError: Если количество спящих превышает максимальное количество проживающих на кровати.

        Examples:
            >>> bed = Bed(length=200, width=150, max_occupants=2)
            >>> bed.sleep(occupants=1)
        """
        if occupants > self.max_occupants:
            raise ValueError("Количество спящих превышает максимальное количество проживающих на кровати")
        ...

    def make_bed(self) -> None:
        """
        Заправить кровать.

        Examples:
            >>> bed = Bed(length=200, width=150, max_occupants=2)
            >>> bed.make_bed()
        """
        ...

    def get_bed_area(self) -> int:
        """
        Возвращает площадь кровати.

        Returns:
           int: Площадь кровати в квадратных сантиметрах.

        Examples:
            >>> bed = Bed(length=200, width=150, max_occupants=2)
            >>> bed.get_bed_area()
            30000
        """
        return self.length * self.width

class Car:
    """
    Абстрактный класс, представляющий автомобиль.

    Атрибуты:
        max_speed (int): Максимальная скорость автомобиля в километрах в час.
        fuel_capacity (int): Емкость топливного бака автомобиля в литрах.
        current_fuel (int): Текущее количество топлива в баке в литрах.
    """

    def __init__(self, max_speed: int, fuel_capacity: int, current_fuel: int) -> None:
        """
        Конструктор класса Car.

        Args:
            max_speed (int): Максимальная скорость автомобиля в километрах в час.
            fuel_capacity (int): Емкость топливного бака автомобиля в литрах.
            current_fuel (int): Текущее количество топлива в баке в литрах.

        Raises:
            ValueError: Если максимальная скорость, емкость топливного бака или текущее количество топлива отрицательные, или если текущее количество топлива больше емкости бака.
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительной")
        if fuel_capacity <= 0:
            raise ValueError("Емкость топливного бака должна быть положительной")
        if current_fuel < 0:
            raise ValueError("Текущее количество топлива не может быть отрицательным")
        if current_fuel > fuel_capacity:
            raise ValueError("Текущее количество топлива не может превышать емкость бака")

        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel

    def drive(self, distance: int, fuel_consumption: int) -> None:
        """
        Проехать на автомобиле определенное расстояние.

        Args:
            distance (int): Расстояние, которое нужно проехать на автомобиле, в километрах.
            fuel_consumption (int): Расход топлива на 100 км, в литрах.

        Raises:
            ValueError: Если расстояние отрицательное, или расход топлива отрицательный, или если не хватает топлива на поездку.

        Examples:
            >>> car = Car(max_speed=200, fuel_capacity=60, current_fuel=40)
            >>> car.drive(distance=200, fuel_consumption=10)
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным")
        fuel_needed = (distance/100) * fuel_consumption
        if fuel_needed > self.current_fuel:
            raise ValueError("Недостаточно топлива для поездки")
        ...

    def refuel(self, fuel_amount: int) -> None:
        """
        Заправить автомобиль на заданное количество литров.

        Args:
            fuel_amount (int): Количество топлива для заправки, в литрах.

        Raises:
            ValueError: Если количество топлива для заправки отрицательное, или если после заправки общее количество топлива превысит емкость бака.

        Examples:
            >>> car = Car(max_speed=200, fuel_capacity=60, current_fuel=40)
            >>> car.refuel(fuel_amount=20)
        """
        if fuel_amount <= 0:
            raise ValueError("Количество топлива для заправки должно быть положительным")
        if (self.current_fuel + fuel_amount) > self.fuel_capacity:
             raise ValueError("Превышена емкость бака")
        ...

    def get_remaining_range(self, fuel_consumption: int) -> int:
        """
         Возвращает оставшийся пробег на текущем количестве топлива.

        Args:
             fuel_consumption(int): Расход топлива на 100 км, в литрах.

        Returns:
             int: Оставшийся пробег на текущем количестве топлива, в километрах.

        Examples:
             >>> car = Car(max_speed=200, fuel_capacity=60, current_fuel=40)
             >>> car.get_remaining_range(fuel_consumption=10)
             400
        """
        if fuel_consumption <= 0:
             raise ValueError("Расход топлива должен быть положительным")
        return int((self.current_fuel/fuel_consumption) * 100)


if __name__ == "__main__":
    doctest.testmod()