from abc import ABC, abstractmethod
from typing import Union

class Sportsmen(ABC):
  competition_level: list[str] = ["Областной", "Международный", "Чемпионат мира"]
  people_world: tuple[str] = ("Русские","Татары", "Белорусы")

  def __init__(self, name: str, age: int, type_sport: str):
    self._name = name
    self._age = age
    self._type_sport = type_sport

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, value: str) -> None:
    self._name = value

  @property
  def age(self) -> int:
    return self._age

  @age.setter
  def age(self, value: int) -> None:
    self._age = value

  @property
  def type_sport(self) -> str:
    return self._type_sport

  @type_sport.setter
  def type_sport(self, value: str) -> None:
    self._type_sport = value

  @abstractmethod
  def sportsmen_train(self) -> None:
    print(f"{self.name} тренируется в течение 2 часов.")

    for i in range(2):
      print(f"Тренировка: {i+1} час.")

  @abstractmethod
  def sportsmen_compete(self) -> None:
    print(f"{self.name} участвует в соревнованиях.")

    if self.type_sport == "Футбол":
      print("Это футбольный матч.")
    else:
      print(f"Соревнования по {self.type_sport}.")

  @staticmethod
  def get_type_sport(type_sport: str) -> str:
    level: int = int(input("Введите уровень соревнований(0-10):"))

    if level < 4:
      print(Sportsmen.competition_level[0])
    elif 3 < level < 7:
      print(Sportsmen.competition_level[1])
    else:
      print(Sportsmen.competition_level[2])

    if type_sport in ["Футбол", "Баскетбол", "Волейбол"]:
      return "Командный"
    return "Индивидуальный"

  @classmethod
  def create_sportsmen(cls, data: dict) -> Union["TeamSportsmen", "IndividualSportsmen"]:
    if data["type_sport"] in ["Футбол", "Баскетбол", "Волейбол"]:
      return TeamSportsmen(data["name"], data["age"], data["type_sport"], data["team"])
    return IndividualSportsmen(data["name"], data["age"], data["type_sport"], data["record"])

class TeamSportsmen(Sportsmen):
  stadiums: dict[str] = ["Волга", "Волга-Спорт-Арена", "Труд"]
  count_team: int = 5

  def __init__(self, name: str, age: int, type_sport: str, team: str):
    super().__init__(name, age, type_sport)
    self.__team = team

  def get_team(self) -> str:
    return self.__team

  def set_team(self, value: str) -> None:
    self.__team = value

  def sportsmen_train(self) -> None:
    print(f"{self.name} тренируется в клубе {self.__team}.")
    teammates = [self.name, "Валентин Солодаренко", "Дмитрий Каменщиков"]
    print(f"Клуб: {self.__team}")

    for teammate in teammates:
      print(f" - {teammate}")

  def sportsmen_compete(self) -> None:
    print(f"{self.name} участвует в соревнованиях за {self.__team}.")

    if self.__team == "Волга":
      print(f"Я болею за {self.__team}!")
    else:
      print(f"Команда соперника против {self.__team}.")

class IndividualSportsmen(Sportsmen):
  best_record: int = 25
  count_sportsmen: int = 1350

  def __init__(self, name: str, age: int, type_sport: str, record: int):
    super().__init__(name, age, type_sport)
    self.__record = record

  def get_record(self) -> int:
    return self.__record

  def set_record(self, value: int):
    self.__record = value

  def sportsmen_train(self) -> None:
    print(f"{self.name} тренируется индивидуально.")

    if self.__record < IndividualSportsmen.best_record:
      print(f"Это новый рекорд - {self.__record}")
    else:
      print("Все равно молодец!")

  def sportsmen_compete(self) -> None:
    print(f"{self.name} участвует в соревнованиях по {self.type_sport}.")

    if self.type_sport == "Плавание":
      print("Это заплыв на скорость.", "Возможные дистанции:", sep='\n')
      for i in ['50', '100', '200', '400']:
        print(f' - {i} метров')
    else:
      print(f"Соревнования по {self.type_sport}.")

print(Sportsmen.get_type_sport("Футбол"), '\n')

sportsmen_data1: dict = {"name": "Евгений Рылов", "age": 28, "type_sport": "Плавание", "record": 23.7}
sportsmen_data2: dict = {"name": "Денис Еремеев", "age": 19, "type_sport": "Футбол", "team": "Волга"}
new_sportsmen1 = Sportsmen.create_sportsmen(sportsmen_data1)
new_sportsmen2 = Sportsmen.create_sportsmen(sportsmen_data2)
print((new_sportsmen1.name, new_sportsmen1.age), (new_sportsmen2.name, new_sportsmen2.age), '\n')

print(new_sportsmen1.get_record(), '\n')

print(new_sportsmen2.get_team(), '\n')

IndividualSportsmen.sportsmen_train(new_sportsmen1)
IndividualSportsmen.sportsmen_compete(new_sportsmen1)
print()
TeamSportsmen.sportsmen_train(new_sportsmen2)
TeamSportsmen.sportsmen_compete(new_sportsmen2)
