# About The Project
- 충전을 필요로 하는 전기차의 위치와 잔여 충전량을 기반으로 전기차 이동충전소가 최적의 경로로 자율주행 할 수 있는 환경을 강화학습을 통해 구축한다.

- 이를 통해 전기차 충전소 인프라 부족 현상을 해결하고자 한다.

# Getting Started
## Installation
```
1) conda create -n Multi-Agent-ChargingStation python=3.7

2) conda activate Multi-Agent-ChargingStation

3) pip install -e .

4) python main.py
```

# Output
https://user-images.githubusercontent.com/70676394/171130551-299b211d-a8cd-4229-8593-42aa0c9006be.mp4
- 다음 영상에서 빨간색은 전기차이고 파란색은 전기차 충전소이다. 

- 둘다 시간이 흐름에 따라 이동하며, 전기차는 전기차 충전소와 가까운 방향으로 이동하며 전기차 충전소는 상,하,좌,우에 있는 전기차 충전소를 충전한다. 

- 충전이 끝난 전기차는 화면에서 사라진다. 테스트 후반부로 갈수록 전기차가 충전됨을 볼 수 있다.