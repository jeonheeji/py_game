from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def special_attack(self, target):
        pass

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name}이 {amount}데미지지를 입었다. 현재 체력은 {self.hp}")

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"이름:{self.name} : 체력 {self.hp}/{self.max_hp}")

    def reset_health(self):
        self.hp = self.max_hp
        print(f"reset {self.name}의 체력이 {self.max_hp}로 돌아왔습니다")

    def get_name(self):
        return self.name
