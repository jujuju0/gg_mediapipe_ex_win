import random
from pygame import mixer
import csv
import time
import os


mixer.init()


FILE_PATH = "./data/word.txt"


# 워드 파일을 로딩하여 words 리스트에 대입
def wordLoad():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return [line.rstrip('\n').rstrip() for line in f]
    except FileNotFoundError:
        print(f"Error: {FILE_PATH} 파일을 찾을 수 없습니다.")
        return []

# 워드 게임 실행
def gameRun(word_list):
    ready = input("게임을 시작하려면 엔터를 누르세요.(종료: q)")
    if ready.lower() == 'q':
        print("게임을 종료합니다.")
        return

    print("게임이 시작됩니다!")
    start_time = time.time()

    count = 1
    result = 0
    while(count <= 5):
        print(f"Question #{count}")
        suggested_word = random.choice(word_list)
        print("제시 단어:", suggested_word)
        answer_word = input("정답 단어: ")

        try:
            if suggested_word == answer_word:
                print(suggested_word, answer_word)
                result += 1
                mixer.music.load('./assets/good.wav')
                print("정답!")
            else:
                mixer.music.load('./assets/bad.wav')
                print("땡~")
            
            mixer.music.play()
        except Exception as e:
            print("오류 발생:", e)
            
        count += 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    _scorePrint(elapsed_time, result)
    _saveResult(elapsed_time, result)


# 게임 결과 출력
def _scorePrint(elapsed_time, result):
    if result >= 3:
        print("합격입니다.")
        print(f"걸린 시간: {elapsed_time:.2f}초, 맞춘 개수: {result}")
    else:
        print("다시 시도해보세요.")
        print(f"걸린 시간: {elapsed_time:.2f}초, 맞춘 개수: {result}")   


# 게임 결과 누적 저장
def _saveResult(elapsed_time, result):
    file_path = "./result/word_game_socre.csv"

    # 파일의 상위 디렉터리 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        if os.path.getsize(file_path) == 0:
            writer.writerow(["elapsed_time", "result"])

        writer.writerow([elapsed_time, result])


if __name__ == "__main__":
    # 이 블록은 word_module.py를 '직접' 실행할 때만 작동한다.
    # app.py에서 'import'할 때는 이 아래 코드가 완전히 무시되므로 안전하다.
    print("--- 모듈 단독 테스트 모드 ---")
    test_list = ["apple", "banana", "cherry"]
    gameRun(test_list)