import random
from .character import Character


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=80)
        self.attack_power = 18
        self.mana = 100
        self.max_mana = 100

    def attack(self):
        print(f"{self.name}가 공격했습니다 데미지 : {self.attack_power}")
        return self.attack_power

    def special_attack(self, target):
        mana_cost = 20
        attack_name = "fireball"
        if self.mana < mana_cost:
            print(f"⚠️ {self.name}의 마나가 부족합니다. 특수 공격을 할 수 없습니다.")
            return  # 공격하지 않고 함수 종료

        damage = int(self.attack_power * 1.5)
        self.mana -= mana_cost
        print(f"{self.name}가 특수 공격 '{attack_name}'을 했습니다. {target.name}에게 데미지: {damage} 입힘. 남은 마나: {self.mana}")
        target.take_damage(damage)

    def show_status(self):
        print(
            f"이름 : {self.name} : 체력: {self.hp}/{self.max_hp} : 마나:{self.mana}/{self.max_mana}")

    def reset_health(self):
        super().reset_health()
        self.mana = self.max_mana
        print(f"{self.name}의 마나가 {self.max_mana}로 회복되었습니다.")
