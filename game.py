from battle.battle_manager import BattleManager
from characters.rogue import Rogue
from characters.warrior import Warrior
from characters import Mage
print("mage 모듈 임포트 성공")


def choose_character(prompt):
    while True:
        print(f"\n{prompt}")
        print("1. Mage (마법사)")
        print("2. Warrior (전사)")
        print("3. Rogue (도적)")
        choice = input("번호를 선택하세요: ")

        if choice == '1':
            return Mage("마법사")
        elif choice == '2':
            return Warrior("전사")
        elif choice == '3':
            return Rogue("도적")
        else:
            print("⚠️ 올바른 번호를 입력하세요.")


def main():
    print("🎮 게임 시작!")

    # 사용자 캐릭터 선택
    player = choose_character("당신의 캐릭터를 선택하세요")

    while True:
        # 적 캐릭터 선택
        enemy = choose_character("상대 캐릭터를 선택하세요")

        # 체력/마나 초기화
        player.reset_health()
        enemy.reset_health()

        # 전투 시작
        battle = BattleManager(player, enemy)
        battle.start_battle()

        # 전투 결과 확인
        if player.is_alive():
            again = input("🎉 승리했습니다! 다시 싸우시겠습니까? (y/n): ").lower()
            if again != 'y':
                print("👋 게임을 종료합니다.")
                break
        else:
            print("💀 당신은 패배했습니다. 게임 종료.")
            break


if __name__ == "__main__":
    main()
