import random
from pygame import mixer
import csv
import time
import os


mixer.init()


FILE_PATH = "./data/word.txt"


class WordGame:

    def __init__(self):
        self.word_list = []
        self.count = 1
        self.result = 0

    # 워드 파일을 로딩하여 words 리스트에 대입
    def wordLoad(self):
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                return [line.rstrip('\n').rstrip() for line in f]
        except FileNotFoundError:
            print(f"Error: {FILE_PATH} 파일을 찾을 수 없습니다.")
            return []

    # 워드 게임 실행
    def gameRun(self):
        ready = input("게임을 시작하려면 엔터를 누르세요.(종료: q)")
        if ready.lower() == 'q':
            print("게임을 종료합니다.")
            return

        print("게임이 시작됩니다!")
        start_time = time.time()
    
        while(self.count <= 5):
            print(f"Question #{self.count}")
            suggested_word = random.choice(self.word_list)
            print("제시 단어:", suggested_word)
            answer_word = input("정답 단어: ")

            try:
                if suggested_word == answer_word:
                    print(suggested_word, answer_word)
                    self.result += 1
                    mixer.music.load('./assets/good.wav')
                    print("정답!")
                else:
                    mixer.music.load('./assets/bad.wav')
                    print("땡~")
                
                mixer.music.play()
            except Exception as e:
                print("오류 발생:", e)
                
            self.count += 1

        end_time = time.time()
        elapsed_time = end_time - start_time
        self._scorePrint(elapsed_time)
        self._saveResult(elapsed_time)


    # 게임 결과 출력
    def _scorePrint(self, elapsed_time):
        if self.result >= 3:
            print("합격입니다.")
            print(f"걸린 시간: {elapsed_time:.2f}초, 맞춘 개수: {self.result}")
        else:
            print("다시 시도해보세요.")
            print(f"걸린 시간: {elapsed_time:.2f}초, 맞춘 개수: {self.result}")   


    # 게임 결과 누적 저장
    def _saveResult(self, elapsed_time):
        file_path = "./result/word_game_socre.csv"

        # 파일의 상위 디렉터리 생성
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)

            if os.path.getsize(file_path) == 0:
                writer.writerow(["elapsed_time", "result"])

            writer.writerow([elapsed_time, self.result])
 

    def run(self):
        self.word_list = self.wordLoad()
        # 게임 실행
        self.gameRun()


if __name__ == "__main__":
    wg = WordGame()
    wg.run()