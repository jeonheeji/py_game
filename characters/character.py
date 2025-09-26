from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    # 기본공격 (추상메서드)
    @abstractmethod
    def attack(self):
        pass

    # 특수공격 (추상메서드)
    @abstractmethod
    def special_attack(self, target):
        pass

    # 피해를 입으면 체력이 감소
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name}이 {amount}데미지지를 입었다. 현재 체력은 {self.hp}")

    # 체력이 0 이하이면 false 반환
    def is_alive(self):
        return self.hp > 0

    # 캐릭터의 정보를 출력
    def show_status(self):
        print(f"이름:{self.name} : 체력 {self.hp}/{self.max_hp}")

    # 캐릭터의 체력을 초기화
    def reset_health(self):
        self.hp = self.max_hp
        print(f"{self.name}의 체력이 {self.max_hp}로 돌아왔습니다")

    # 캐릭터의 이름을 가져옴
    def get_name(self):
        return self.name
