# gg_pywords_game
파이썬 단어 게임

## 게임 실행 방법
```
uv run app.py
```

## 프로젝트 초기 세팅
- git 클론
- uv 가상환경 구성
- pygame 라이브러리 설치
```bash
git colne <ssh url>
cd [프로젝트 폴더명]
uv init --bare --python 3.12 --name words-game
uv add pygame
```


#### Windows 환경에서 세팅하기
```bash
[1] PowerShell에서 uv 설치

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


[2] PowerShell 종료 후 다시 실행


[3] uv 설치 확인

uv --version


[4] Git Bash 실행


[5] 프로젝트를 받을 폴더로 이동

cd /c/Users/Admin/Desktop


[6] GitHub 저장소 Clone

git clone https://github.com/happymaker1024/gg1th_mediapipe_ex_win.git


[7] 프로젝트 폴더 이동

cd 저장소명


[8] uv 프로젝트 환경 구성

uv sync


[9] Python 버전 확인

python --version


[10] uv 버전 확인

uv --version


[11] 프로젝트 실행

uv run python 11_hand_tracking.py

uv run python 12_hand_tracking.py

```