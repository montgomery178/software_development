class Car:
    """Автомобиль с различными конфигурациями"""

    def __init__(self):
        self.seats: int = None
        self.engine: str = None
        self.steering_wheel: str = None
        self.gps: bool = None

    def __str__(self) -> str:
        return f"Автомобиль с {self.seats} местами, двигателем {self.engine}, " \
               f"{'леворульный' if self.steering_wheel == 'левый' else 'праворульный'}, " \
               f"{'с GPS' if self.gps else 'без GPS'}"


class Manual:
    """Руководство автомобиля для пользователя"""

    def __init__(self):
        self.seats_description: str = ""
        self.engine_description: str = ""
        self.steering_wheel_description: str = ""
        self.gps_description: str = ""

    def __str__(self) -> str:
        return f"Руководство: \nМеста: {self.seats_description}\nДвигатель: {self.engine_description}\n" \
               f"Руль: {self.steering_wheel_description}\nGPS: {self.gps_description}"


class Builder:
    """Строитель, объявляющий методы для конфигурации продукта"""

    def reset(self) -> None:
        raise NotImplementedError

    def setSeats(self, number: int) -> None:
        raise NotImplementedError

    def setEngine(self, engine: str) -> None:
        raise NotImplementedError

    def setSteeringWheel(self, steering_wheel: str) -> None:
        raise NotImplementedError

    def setGPS(self, has_gps: bool) -> None:
        raise NotImplementedError


class CarBuilder(Builder):
    """Конкретный строитель, создающий машины"""

    def reset(self) -> None:
        self.car: Car = Car()

    def setSeats(self, number: int) -> None:
        self.car.seats = number

    def setEngine(self, engine: str) -> None:
        self.car.engine = engine

    def setSteeringWheel(self, steering_wheel: str) -> None:
        self.car.steering_wheel = steering_wheel

    def setGPS(self, has_gps: bool) -> None:
        self.car.gps = has_gps

    def getResult(self) -> Car:
        return self.car


class CarManualBuilder(Builder):
    """Конкретный строитель, создающий руководство"""

    def reset(self) -> None:
        self.manual: Manual = Manual()

    def setSeats(self, number: int) -> None:
        self.manual.seats_description = f"В этом автомобиле {number} мест."

    def setEngine(self, engine: str) -> None:
        self.manual.engine_description = f"Этот автомобиль оснащен двигателем {engine}."

    def setSteeringWheel(self, steering_wheel: str) -> None:
        self.manual.steering_wheel_description = f"Этот автомобиль {steering_wheel}."

    def setGPS(self, has_gps: bool) -> None:
        self.manual.gps_description = "Этот автомобиль оснащен системой GPS." if has_gps else "Этот автомобиль не оснащен системой GPS."

    def getResult(self) -> Manual:
        """Возвращает построенный объект Manual."""
        return self.manual


class Director:
    """Директор, управляющий работой по созданию продукта с помощью строителей"""

    # builder: Builder – значит что на вход должен подаваться экземпляр строителя
    def constructCar(self, builder: Builder, seats: int, engine: str, steering_wheel: str, gps: bool) -> None:
        builder.reset()
        builder.setSeats(seats)
        builder.setEngine(engine)
        builder.setSteeringWheel(steering_wheel)
        builder.setGPS(gps)


class Application:
    """Класс, который объединяет все воедино"""

    def makeCar(self, seats: int, engine: str, steering_wheel: str, gps: bool) -> None:
        director = Director()

        car_builder = CarBuilder()
        director.constructCar(car_builder, seats, engine, steering_wheel, gps)
        car = car_builder.getResult()
        print(car)

        manual_builder = CarManualBuilder()
        director.constructCar(manual_builder, seats, engine, steering_wheel, gps)
        manual = manual_builder.getResult()
        print(manual)


if __name__ == "__main__":
    app = Application()
    
    seats = 4
    engine = "V8"
    steering_wheel = "левый"
    gps = True
    app.makeCar(seats, engine, steering_wheel, gps)
