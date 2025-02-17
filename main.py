class Animal:
    """
    Базовый класс, представляющий животное.

    Attributes:
        name (str): Имя животного.
        species (str): Вид животного.
        age (int): Возраст животного.
        _weight (float): Вес животного (непубличный атрибут). Инкапсулирован, так как точный вес может быть
                       конфиденциальной информацией.
    """

    def __init__(self, name: str, species: str, age: int, weight: float) -> None:
        """
        Инициализирует животное.

        Args:
            name (str): Имя животного.
            species (str): Вид животного.
            age (int): Возраст животного.
            weight (float): Вес животного.
        """
        self.name = name
        self.species = species
        self.age = age
        self._weight = weight

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.
        """
        return f"{self.name} - {self.species}, {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление животного для отладки.
        """
        return f"Animal(name='{self.name}', species='{self.species}', age={self.age}, weight={self._weight})"

    def make_sound(self) -> str:
        """
        Издает звук, характерный для животного.
        """
        return "Generic animal sound"

    def get_weight(self) -> float:
        """
        Возвращает вес животного.

        Returns:
            float: Вес животного.
        """
        return self._weight


class Dog(Animal):
    """
    Класс, представляющий собаку, наследуется от Animal.

    Attributes:
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, weight: float, breed: str) -> None:
        """
        Инициализирует собаку.

        Args:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            weight (float): Вес собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, "Dog", age, weight)
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки.
        Перегружен, чтобы добавить информацию о породе.
        """
        return f"{super().__str__()} - Порода: {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление собаки для отладки.
        """
        return f"Dog(name='{self.name}', age={self.age}, weight={self._weight}, breed='{self.breed}')"

    def make_sound(self) -> str:
        """
        Издает звук, характерный для собаки.
        Перегружен, так как звук собаки отличается от звука обычного животного.
        """
        return "Woof!"

    def wag_tail(self) -> str:
        """
        Собака виляет хвостом.
        """
        return "Собака виляет хвостом"

    def get_human_age(self) -> int:
        """
        Унаследованный метод, который переводит возраст собаки в человеческий.
        Взято из открытых источников, что один год собаки равен семи годам человека.

        Returns:
            int: Возраст собаки в человеческих годах.
        """
        return self.age * 7


if __name__ == "__main__":
    animal = Animal("Барт", "Кот", 3, 5.5)
    print(animal)
    print(repr(animal))
    print(animal.make_sound())
    print(animal.get_weight())

    dog = Dog("Чарли", 5, 15.0, "Golden Retriever")
    print(dog)
    print(repr(dog))
    print(dog.make_sound())
    print(dog.wag_tail())
    print(dog.get_weight())
    print(dog.get_human_age())
