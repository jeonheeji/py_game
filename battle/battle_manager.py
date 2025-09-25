import random
import time


class BattleManager:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def start_battle(self):
        print("⚔️ 전투 시작!")
        time.sleep(1)

        # 선공자 랜덤 결정
        if random.random() < 0.5:
            attacker, defender = self.character1, self.character2
        else:
            attacker, defender = self.character2, self.character1

        print(f"🎲 {attacker.get_name()}이(가) 선공합니다!")
        time.sleep(1)

        # 전투 루프
        while attacker.is_alive() and defender.is_alive():
            self.perform_turn(attacker, defender)
            time.sleep(1.5)

            if defender.is_alive():
                self.perform_turn(defender, attacker)
                time.sleep(1.5)

            # 상태 출력
            attacker.show_status()
            defender.show_status()
            print("-" * 30)
            time.sleep(1.5)

        # 전투 종료
        winner = attacker if attacker.is_alive() else defender
        print(f"🏆 {winner.get_name()}의 승리!")

    def perform_turn(self, attacker, defender):
        try:
            if random.random() < 0.7:
                # 기본 공격
                damage = attacker.attack()
                defender.take_damage(damage)
            else:
                # 특수 공격
                attacker.special_attack(defender)
        except Exception as e:
            print(f"⚠️ {attacker.get_name()}의 특수 공격 실패: {str(e)}")
