import random
 # 수정하는 것을 테스트합니다
def generate_lotto_numbers():
    white_balls = random.sample(range(1, 70), 5)
    powerball = random.randint(1, 26)
    return sorted(white_balls), powerball

def main():
    print("로또 당첨 번호 추첨기")
    print("====================")
   
    while True:
        input("누르십시오... Enter를 누르면 번호를 추첨합니다.")
        
        white_balls, powerball = generate_lotto_numbers()
        
        print("추첨된 번호:")
        print("흰공:", white_balls)
        print("빨강공 (파워볼):", powerball)
        
        play_again = input("더 추첨하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()

