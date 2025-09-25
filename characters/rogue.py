from .character import Character
import random


class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=90)
        self.attack_power = 12

    def attack(self):
        print(f"{self.name}가 기본 공격했습니다. 데미지: {self.attack_power}")
        return self.attack_power

    def special_attack(self, target):
        attack_name = "Ambush"
        success_chance = 0.7
        if random.random() < success_chance:
            damage = int(self.attack_power * 3)
            print(
                f"{self.name}의 특수공격 '{attack_name}' 성공! {target.name}에게 {damage} 데미지!")
            target.take_damage(damage)
        else:
            print(f"{self.name}의 특수공격 '{attack_name}' 실패! 공격이 빗나갔습니다.")

    def show_status(self):
        print(f"이름: {self.name} | 체력: {self.hp}/{self.max_hp}")

    def reset_health(self):
        super().reset_health()
