# [Gold V] 마을의 친밀도 - 9763 

[문제 링크](https://www.acmicpc.net/problem/9763) 

### 성능 요약

메모리: 117348 KB, 시간: 3968 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2022년 7월 4일 19:14:22

### 문제 설명

<p>세 마을의 좌표가 (x<sub>1</sub>, y<sub>1</sub>, z<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>, z<sub>2</sub>), (x<sub>3</sub>, y<sub>3</sub>, z<sub>3</sub>)이라고 가정해보자. 이때, 세 마을을 친밀도는 아래와 같이 구할 수 있다.</p>

<p>친밀도 = d<sub>12</sub> + d<sub>23</sub> (d<sub>ij</sub> = |x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>| + |z<sub>i</sub> - z<sub>j</sub>|)</p>

<p>마을이 주어졌을 때, 가장 작은 세 마을의 친밀도를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 마을의 수 N (3 ≤ N ≤ 10,000)이 주어진다. 다음 N개 줄에는 마을의 위치 (x, y, z)가 주어진다. (-1000 ≤ x,y,z ≤ 1000)</p>

### 출력 

 <p>세 마을의 친밀도 중 가장 작은 값을 출력한다.</p>

