from .character import Character


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100)
        self.attack_power = 15

    def attack(self):
        print(f"{self.name}가 공격했습니다 데미지 : {self.attack_power}")
        return self.attack_power

    def special_attack(self, target):
        attack_name = "power_strike"
        damage = int(self.attack_power*2)
        self.take_damage(5)
        print(f"""{self.name}가 특수 공격{attack_name}을 했습니다 
                 {target.name}에게 데미지: {damage} 입힙""")
        target.take_damage(damage)

    def show_status(self):
        print(f"이름 : {self.name} : 체력: {self.hp}/{self.max_hp}")

    def reset_health(self):
        super().reset_health()
