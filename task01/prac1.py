import random


def solve():
    random_number = random.randint(1, 1000)
    print(random_number)
    while True:
        try:
            input_num = int(input("1~1000사이 숫자를 입력하세요:"))
            if input_num == random_number:
                print("정답")
                break
            elif input_num > random_number:
                print("더 작은 수")
            else:
                print("더 큰 수")
        except:
            print("잘못된 입력")


if __name__ == "__main__":
    assert solve()
