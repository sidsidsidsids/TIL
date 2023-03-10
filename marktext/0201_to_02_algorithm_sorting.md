# TIL

### 알고리즘의 성능

- 정확성
  
  - 얼마나 정확하게 동작하는가

- 작업량
  
  - 얼마나 적은 연산으로 원하는 결과를 얻는가

- 메모리 사용량
  
  - 얼마나 적은 메모리를 사용하는가

- 단순성
  
  - 얼마나 단순한가

- 최적성
  
  - 더 이상 개선할 여지없이 최적화되었는가

- 시간 복잡도 (Large O)
  
  - 알고리즘의 작업량을 표현하며 실제 걸리는 시간을 측정
  
  - 알고리즘의 작업량을 표현하며 실제 걸리는 시간을 측정
  
  - 실행되는 명령문의 개수를 계산

### 배열

- `arr = []` , `arr = [0]*10` 꼴로 1차원 배열 생성

- 최대값 max 안쓰고 구하기
  
  - `max = 0 ; if arr[i] > max : max = arr[i] `

### 정렬

- **Bubble Sort**
  
  - 인접한 두 개의 원소를 비교하며 자리를 계속 교환
  
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하며 맨 마지막 자리까지 이동함
  
  - O(n^2), n은 리스트 길이

- *Counting Sort*
  
  - 집합에 각 항목이 몇 개씩 있는지 세는 작업을 통해 선형 시간에 정렬
    
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
  
  - O(n+k) , n은 리스트 길이, k는 정수의 최대값

- **Selection Sort**
  
  - 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환
    
    - 최소값을 리스트의 맨 앞에 위치한 값과 교환하며 맨 앞을 줄이며 반복
    
    - k번째로 작거나 큰 값 찾을 때 유용
  
  - O(n^2), n은 리스트 길이

- Quick Sort

- Insertion Sort

- Merge Sort

### 접근 방법

- 완전 검색
  
  - 문제의 해법으로 생각할 수 있는 모든 경우의 수 나열 및 확인
  
  - 일반적으로 경우의 수가 상대적으로 작을 때 유용
  
  - 순열을 이용 (nPr)

- 탐욕 알고리즘 (Greedy)
  
  - 최적해를 구하는 데 사용되는 근시안적 방법
  
  - 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라 생각하는 것을 선택해 나가는 방식으로 머릿속에 떠오른 생각을 검증 없이 바로 구현하는 것

### 2차원 배열

- 1차원 리스트를 묶어놓은 리스트

- 선언 : 세로길이(행의 개수), 가로길이(열의 개수)
  
  - 빈 배열 선언 : [ [0] * n for _ in range (n) ]

- 행 우선 순회
  
  - ```python
    for i in range(n):
        for j in range(m):
            Array[i][j]
    ```

- 열 우선 순회
  
  - ```python
    for j in range(m):
        for i in range(n):
            Array[i][j]
    ```

- 지그재그 순회
  
  - ```python
    for i in range(n):
        for j in range(m):
            Array[i][j + (m-1-2*j) * (i%2)]
    # i가 짝수일 때 [j + (m-1-2*j) * (i%2)] = j , j : 0 -> m-1
    # i가 홀수일 때 [j + (m-1-2*j) * (i%2)] = m-1 - j , j : m-1 -> 0
    ```

- 델타 이용 2차 배열 탐색 : 2차 배열의 한 좌표에서 4방향의 인접 배열 요소 탐색 방법
  
  - ```python
    '''
    arr[0...N-1][0...N-1] # N*N 배열
    di[] <- [0, 0, -1, 1] 
    dj[] <- [-1, 1, 0, 0] # 좌, 우, 상, 하
    for i : 0 -> N-1:
        for j : 0 -> N-1:
            for k in range(4):
                ni <- i + di[k]
                nj <- j + dj[k]
                if 0 <= ni < N and 0 <= nj < N # 유효한 인덱스인지 확인
                    test(arr[ni][nj])
    '''
    for i in range(N):
        for j in range(N):
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < N:
                    print(i, j, ni, nj)
    ```
  
  - 이를 응용하여 상하좌우 뿐만 아니라 대각선, 8방향 등으로도 활용 가능
    
    - 8방향의 경우 그냥 사각형으로 인덱싱 하는게 더 편하긴 함

- 전치 행렬 (transpose)
  
  - ```python
    for i in range(n) :
        for j in range(m) :
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```

### 부분 집합

> 부분집합의 수 : 집합의 원소가 n개일 때 공집합을 포함한 부분집합의 개수는 2^n개

- loop를 이용한 부분집합 확인 및 생성 방법
  
  - ```python
    bit = [0, 0, 0, 0]
    for i in range(2):
        bit[0] = i # 0번째 원소
        for j in range(2):
            bit[1] = j # 1번째 원소
            for k in range(2):
                bit[2] = k # 2번째 원소
                for l in range(2):
                    bit[3] = l # 3번째 원소
                    print_subset(bit) # 생성된 부분집합 출
    ```

### 비트 연산자

> 비트 : 단위
> 
> | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   |
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

- '&'' : 비트 단위로 AND 연산
  
  - i & (1<<j) : i의 j번째 비트가 1인지 아닌지 검사

- '|' : 비트 단위로 OR 연산

- '<<'' : 피연산자의 비트 열을 왼쪽으로 이동시킨다
  
  - 1 << n : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수 의미

- '>>' : 비트 열을 오른쪽으로 이동시킨다

### 검색

> 저장되어 있는 자료 중 원하는 항목을 찾는 작업 (목적하는 탐색 키)
> 
> 순차 검색 / 이차 검색 / 해쉬

### 순차 검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법. '순차구조'로 구현된 자료에서 찾을 때 유용함

- 검색 대상이 많은 경우 수행시간이 급격히 증가하여 비효율적

- 검색 과정
  
  - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
  
  - 찾으면 인덱스 반환, 없으면 실패

### 이진 검색

- 자료의 가운데 있는 항목의 키 값과 비교하여 다음 검색의 위치를 정하고 검색을 진행

- **자료가 정렬된 상태**일 때 가능

- 검색 과정
  
  - 자료의 중앙에 있는 원소를 골라 그 값과 목표 값을 비교
  
  - 목표 값이 더 작으면 왼쪽에 대해서 새로 검색, 더 크면 오른쪽에 대해서 새로 검색
  
  - 찾을 때까지 반복, 없으면 실패

### 인덱스

> 데이터베이스에서 유래했으며 테이블에 대한 동작 속도를 높여주는 자료 구조
> 
> 키-필드만을 갖고 있고 테이블의 다른 세부 항목들은 갖고 있지 않다

### 문자열

> 메모리는 숫자만을 저장할 수 있기 때문에 각 문자에 대응되는 숫자를 정하고 이를 메모리에 저장하는 방법으로 문자를 표현한다.
> 
> 문자 인코딩 표준 ASCII : 7bit 인코딩으로 128문자를 표현하며 33개의 출력 불가 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져있음
> 
> 유니코드 : 다국어 처리를 위해 만든 표준 문자

- 0과 1 두 가지의 값 중 하나를 저장하는 메모리 단위 Bit

- Bit룰 8개 묶은 것이 Byte
  
  - 보통 Byte 단위로 저장됨

- python에서의 문자열
  
  - char 타입 없음
  
  - 텍스트 데이터 취급방법 통일됨
  
  - 문자열 기호 : '(홑따옴표), "(쌍따옴표), '''(따옴표 3개)
    
    - += (연결) , *(반복)
  
  - replace(), split(), isalpha(), find()
  
  - 튜플과 같이 요소값을 변경 할 수 없음(immutable)

- 문자열 비교
  
  - == : 메모리 참조가 같은지를 비교하는 것 (내부적으로 _ _eq _ _()를 호출 )

- 변환 함수(숫자를 정수로)
  
  - int, float, str, repr

### 패턴 매칭

- 고지식한 패턴 검색 알고리즘 (Brute Force)
  
  - 처음부터 끝까지 차례대로 순회하며 패턴 내 문자들을 일일이 비교
  
  - 최악의 경우 O(MN)이 된다

- KMP 알고리즘
  
  - 불일치가 발생한 스트링 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
  
  - 패턴을 전처리하여 배열 next[M] (불일치가 발생할 경우 이동할 다음 위치)
    을 구해 잘못된 시작을 최소화함
  
  - O(M+N), Theta(N) (theta : 보통 걸리는 정도)

- 보이어-무어 알고리즘
  
  - 오른쪽에서 왼쪽으로 비교, 대부분의 소프트웨어에서 채택한 알고리즘
  
  - 오른쪽 끝 문자가 불일치하고 이 문자가 패턴 내 존재하지 않는 경우 패턴 길이만큼 이동하게 됨
    
    - 불일치하고 문자가 패턴 내 존재하면 그 만큼 이동
  
  - Omega(N) (omega : 최소한의 걸리는 정도)

### 스택

> 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
> 
> Last In First Out, 자료를 선형으로 저장할 저장소

- 연산
  
  - 삽입(push)
    
    - append 메소드를 통해 리스트의 마지막에 데이터를 삽입
      
      - 단점 : 느림
    
    - ```python
      def push(item,size):
          global top
          top += 1
          if top==size:
              print('overflow')
          else:
              stack[top] = item
      ```
      
      size = 10
      stack = [0] * size
      top = -1
      
      push(10, size)
      top += 1 # push(20)
      stack[top] = 20 #
      
      ```
      
      ```

- 삭제(pop)
  
  - ```python
    def pop():
        global top
        if top == -1:
            print('underflow')
            return 0
        else:
            top -= 1
            return stack[top+1]
    
    print(pop())
    
    if top > -1: # pop()
        top -= 1
        print(stack[top+1])
    ```

- 공백인지 아닌지 확인(isEmpty)

- top에 있는 item 반환(peek), (top : 마지막으로 들어온 원소가 저장된 위치)

- 스택의 응용
  
  - 괄호검사
    
    - 괄호의 조건
      
      - 왼쪽 괄호와 오른쪽 괄호의 개수가 같다
      
      - 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다
      
      - 괄호 사이에는 포함 관계만 존재한다
    
    - '(' 를 push, ')'가 나올 때 '(' pop
      
      - 이 과정을 끝냈을 때 남아있는 '('가 있으면 오류
  
  - Function call
    
    - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조 -> 이를 이용한 수행순서 관리
    
    - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
    
    - 함수의 실행이 끝나면 시스템 스택의 top 원소를 pop하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
    
    - 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다

- 재귀호출
  
  - 자기 자신을 호출하여 순환 수행
  
  - 프로그램의 크기를 줄이고 간단하게 작성할 수 있음
  
  - Memoization
    
    - 이전에 계산한 값을 메모리에 저장하여 매번 다시 계산하지 않도록 함

### 동적계획 (DP)

> 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
> 
> 입력 크기가 작은 부분 문제들을 모두 해결한 후 이를 잉하여 큰 부분 문제들을 해결

### 깊이우선탐색 (DFS)

> 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함
> 
> 가장 마지막에 만난 갈림길의 정점으로 되돌아가 다시 탐색하므로 스택(LIFO) 사용

- 알고리즘
  
  - 시작 정점 v를 결정하여 방문한다
  
  - 정점 v에 인접한 정점 중
    
    - 방문하지 않은 정점 w가 있다면 v를 스택에 push 후 w 방문
      그리고 w를 v로 하여 다시 반복
    
    - 방문하지 않은 점점이 없다면 탐색 방향을 바꾸기 위해 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 반복
  
  - 스택이 공백이 될 때까지 2) 반복

### 스택 이용 풀이

- 계산기1
  
  - 중위표기식(A + B)을 후위표기식(A B +)으로 바꾸어 스택을 이용하여 푸는 방법 
    (연산자를 스택에 넣어 식 변환)

- 계산기2
  
  - 후위표기법으로 표현된 수식을 스택에 넣음
    (피연산자를 스택에 넣어 계산)

- 백트래킹
  
  - 해를 찾는 도중에 막히면(해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이며 최적화와 결정 문제를 해결할 수 있다
    
    - 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지에 대한 문제
      
      - 미로 찾기
        
        - DFS 처럼 지나온 길들을 기록하고 막히면 pop해서 갈림길로
        
        - 백트래킹과 DFS의 차이는 백트래킹은 불필요한 경로를 조기에 차단함
        
        - 일반적으로 DFS보다 백트래킹이 경우의 수가 줄어듬(일부 경우에서는 지수함수 시간을 요해 처리 불가능할 수 있음)
      
      - n-Queen
      
      - Map coloring
      
      - subset sum
  
  - 백트래킹 기법은 어떤 노드의 유망성을 점검한 후 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
    
    - 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려 X
  
  - 절차
    
    - 상태 공간 트리의 깊이 우선 검색을 실시한다
    
    - 각 노드가 유망한지를 점검한다
    
    - 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색함
  
  - 부분집합 구하기
    
    - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는 true/false 값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법 이용
    
    - ```python
      # 4 elements combination
      bit = [0,0,0,0]
      for i in range(2):
          bit[0] = i
          for j in range(2):
              bit[1] = j
              for k in range(2):
                  bit[2] = k
                  for l in range(2):
                      bit[3] = l
                      print(bit)
      ```
    
    - ```python
      # 1,2,3 permutation
      for i1 in range(1,4):
          for i2 in range(1,4):
              if i2 != i1:
                  for i3 in range(1,4):
                      if i3 != i1 and i3 != i2:
                          print(i1, i2, i3)
      ```
    
    - ```python
      # permutaion with backtracking
      def backtrack(a, k, input):
          global MAXCANDIDATES
          c = [0] * MAXCANDIDATES
      
          if k == input:
              for i in range(1, k+1):
                  print(a[i], end=" ")
              print()
      
          else:
              k += 1
              ncandidates = construct_candidates(a, k, input, c)
              for i in range(ncandidates):
                  a[k] = c[i]
                  backtrack(a, k, input)
      
      def construct_candidates(a, k, input, c):
          in_perm = [False] * NMAX
      
          for i in range(1,k):
              in_perm[a[i]] = True
      
          ncandidates = 0
          for i in range(1, input+1):
              if in_perm[i] == False:
                  c[ncandidates] = i
                  ncandidates += 1
          return ncandidates
      
      NMAX = 11
      MAXCANDIDATES = 10
      a = [0] * NMAX
      backtrack(a, 0, 3)
      ```
    
    - ```python
      # combination with function
      def f(i, k):
          if i == k:
              print(bit)
          else:
              bit[i] = 1
              f(i+1, k)
              bit[i] = 0
              f(i+1, k)
      A = {1,2,3,0,9}
      N = len(A)
      bit = [0]*N
      f(0, N)
      ```

### 분할 정복 알고리즘

> 나폴레옹이 사용한 전략이 유래이며 분할, 정복, 통합으로 이루어짐

- 거듭제곱
  
  - ```python
    def Power(Base, Exponent):
        if Base == 0:
            return 1
        result = 1 # Base^0은 1이므로
        for i in range(Exponent):
            result *= Base
        return result
    ```

- 퀵 정렬 (Quick Sort)
  
  - 주어진 배열을 두 개로 분할하고 각각을 정렬한다
  
  - 합병정렬은 그냥 두 부분으로 나누지만 퀵 정렬은 기준 아이템 중심으로 나눔
  
  - 후처리 과정이 필요 없음
  
  - ```python
    def quickSort(a, begin, end):
        if begin < end:
            p = partition(a, begin, end)
            quickSort(a, begin, p-1)
            quickSort(a, p+1, end)
    ```
  
  - ```python
    def partition(a, begin, end):
        pivot = (begin + end) // 2
        L = begin
        R = end
        while L < R:
            while(L<R and a[L] < a[pivot]) : L += 1
            while(L<R and a[R] >= a[pivot]) : R -= 1
            if L < R:
                if L == pivot : pivot = R
                a[L], a[R] = a[R], a[L]
        a[pivot], a[R] = a[R], a[pivot]
        return R
    ```

### 큐(Queue)

> 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
> 
> 선입선출 (First In First Out)

- 연산
  
  - enQueue(item)
    
    - 큐의 뒤쪽에 원소를 삽입
  
  - deQueue()
    
    - 큐의 앞쪽에 원소를 삭제하고 반환
  
  - createQueue()
    
    - 공백 큐 생성
  
  - isEmpty()
    
    - 큐가 공백상태인지 확인
  
  - isFull()
    
    - 큐가 포화상태인지 확인
  
  - Qpeek()
    
    - 큐의 앞쪽에서 원소를 삭제 없이 반환

- 선형큐
  
  - 1차원 배열을 이용한 큐
    
    - 큐의 크기 = 배열의 크기
    
    - front : deQueue된 원소 (저장된 첫 번째 원소의 인덱스)
    
    - rear : 저장된 마지막 원소의 인덱스
  
  - 상태 표현
    
    - 초기 상태 : front = rear = -1
    
    - 공백 상태 : front == rear
    
    - 포화 상태 : rear == n-1 (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)
  
  - 구현
    
    - 크기가 n인 1차원 배열 생성
    
    - front와 rear를 -1로 초기화
    
    - enQueue(item)
      
      - ```python
        def enQueue(item):
            global rear
            if isFull() : print('Full')
            else:
                rear <- rear + 1;
                Q[rear] <- item;
        ```
      
      - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
        
        - rear 값을 하나 증가시켜 새 원소를 삽입할 자리 마련
        
        - 그 인덱스에 해당하는 배열원소 Q[rear]에 item 저장
    
    - deQueue()
      
      - ```python
        deQueue()
            if(isEmpty()) then Queue_Empty();
            else{
                front <- front+1;
                return Q[front];
            }
        ```
      
      - 가장 앞에 있는 원소를 삭제하기 위해
        
        - front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
        
        - 새 첫 원소를 리턴함으로써 삭제와 동일한 기능
    
    - isEmpty(). isFull()
      
      - ```python
        def isEmpty():
            return front == rear
        def isFull():
            return rear == len(Q) - 1
        ```
      
      - 공백상태 : front == rear
      
      - 포화상태 : rear == n-1 (n: 배열의 크기, n-1 : 배열의 마지막 인덱스)
    
    - Qpeek()
      
      - ```python
        def Qpeek():
            if isEmpty() : print("Queue_Empty")
            else : return Q[front+1]
        ```
      
      - 가장 앞에 있는 원소를 검색하여 반환
      
      - 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫 원소를 반환
  
  - 선형 큐 이용시 문제점
    
    - 잘못된 포화상태 인식
      
      - 선형 큐 이용 원소 삽입 삭제의 경우 배열 앞부분에 활용할 수 있는 공간이 있음에도 불구하고 포화상태로 인식하여 더 이상 삽입을 수행하지 않음
      
      - 해결방법 1
        
        - 매 연산이 이루어질 때마다 원소들을 배열 앞부분으로 이동시키기
          
          - 비효율적
      
      - 해결방법 2
        
        - 1차원 배열을 사용하되 논리적으로 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
          
          - 초기 공백 상태
            
            - front = rear = 0
          
          - index 순환
            
            - front와 rear 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후,
              그 다음 논리적 순환을 이루어 배열의 첫 인덱스인 0으로 이동
            
            - 이를 위해 나머지 연산자 mod 사용
          
          - front
            
            - 공백/포화 구분을 쉽게 하기 위해 항상 빈자리로 둠
          
          - 삽입 위치 및 삭제 위치
            
            - | --  | 삽입위치                    | 삭제위치                      |
              | --- | ----------------------- | ------------------------- |
              | 선형큐 | rear = rear + 1         | front = front + 1         |
              | 원형큐 | rear = (rear + 1) mod n | front = (front + 1) mod n |
          
          - 초기 공백 큐 생성
            
            - 크기가 n인 1차원 배열 생성
            
            - front와 rear를 0으로 초기화
          
          - 공백상태 및 포화상태
            
            - 공백상태 : front == rear
            
            - 포화상태 : (rear + 1) mod n == front
            
            - ```python
              def isEmpty():
                  return front == rear
              def isFull():
                  return (rear+1) % len(cQ) == front
              ```
          
          - 삽입
            
            - ```python
              def enQueue(item):
                  global rear
                  if isFull():
                      print('Full')
                  else:
                      rear = (rear+1) % len(cQ)
                      cQ[rear] = item
              ```
            
            - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
              
              - rear 값을 조정하여 새 원소를 삽입할 자리를 마련
              
              - 그 인덱스에 해당하는 배열원소 cQ[rear]에 item 저장
          
          - 삭제
            
            - ```python
              def deQueue():
                  global front
                  if isEmpty():
                      print("Empty")
                  else:
                      front = (front + 1) % len(cQ)
                      return cQ[front]
              ```
            
            - 가장 앞에 있는 원소를 삭제하기 위해
            
            - front 값을 조정하여 삭제할 자리 준비
            
            - 새 front 원소를 리턴 함으로써 삭제와 동일한 기능

- 버퍼(Buffer)
  
  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
  
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작
  
  - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용되며 큐 구조임

- BFS
  
  - 탐색 시작점의 인접한 정점들을 모두 차례로 방문한 후에 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
  
  - 인접한 정점들에 대해 탐색 후 다시 너비우선탐색을 진행해야 하므로 큐 활용
  
  - ```python
    def BFS(G, v): # graph G, start point V
        visited = [0] * (n+1) # n : amount of points
        queue = [] # create queue
        queue.append(v) # enQueue v in queue
        while queue: # if queue is not empty
            t = queue.pop(0) # return queue's first element
            if not visited[t]: # if not visited point
                visited[t] = True # change status : visit
                visit(t) # the thing should do in point t
                for i in G[t]: # all the points that related to t
                    if not visited[i]: # if not visited point
                        queue.append(i) # enQueue in queue
    ```
  
  - 초기 상태
    
    - visited 배열 초기화(중복방지용)
    
    - Q 생성
    
    - 시작점 enqueue

### 트리(Tree)

> 한 개 이상의 노드로 이루어진 유한 집합
> 
> 최상위 노드를 루트(root), 나머지 노드들은 분리 집합으로 분리될 수 있다.

- 개념
  
  - 비선형 구조
  
  - 원소들 간 1:n 관계를 가지며 계층관계를 가짐
  
  - 상위에서 하위로 내려가며 확장되는 트리모양의 구조

- 용어
  
  - 노드(node) : 트리의 원소
  
  - 간선(edge) : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
  
  - 루트 노드(root node) : 트리의 시작 노드
  
  - 형제 노드(sibling node) : 같은 부모 노드의 자식 노드들
  
  - 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
  
  - 서브트리(subtree) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
  
  - 자손 노드 : 서브 트리에 이는 하위 레벨의 노드들
  
  - 차수(degree)
    
    - 노드의 차수 : 노드에 연결된 자식 노드의 수
    
    - 트리의 차수 : 트리에 있는 노드의 차수 중 가장 큰 값
    
    - 단말 노드 (리프 노드) : 차수가 0인 노드 -> 자식 노드가 없는 노드
  
  - 높이(level)
    
    - 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
    
    - 트리의 높이 : 트리에 있는 노드의 높이 중 가장 큰 값, 최대 레벨

- 이진트리
  
  - 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
  
  - 각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리
  
  - 레벨 i에서 노드의 최대 개수는 2^i개이며 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개, 최대 개수는 (2^(h+1) - 1)개가 된다
  
  - 포화 이진 트리 (Full Binary Tree)
    
    - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
    
    - 높이가 h일 때 최대의 노드 개수인 (2^(h+1) - 1)의 노드를 가진 이진 트리
      
      - 높이가 3일 때 (2^(3+1) - 1) = 15 개의 노드
    
    - 루트를 1번으로 하여 2^(h+1) - 1 까지 정해진 위치에 대한 노드 번호를 가짐
  
  - 완전 이진 트리 (Complete Binary Tree)
    
    - 높이가 h이고 노드가 n개일 때 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리 (중간에 비지 않고 마지막은 왼쪽부터 노드가 있는 트리)
  
  - 편향 이진 트리 (Skewed Binary Tree)
    
    - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드를 갖는 트리

- 순회
  
  - 전위순회(preorder traversal) VLR : 부모노드 방문 후 자식노드를 좌,우 순서로 방문
    
    - ```python
      def preorder_traverse(T)
          if T: # T is not None
              visit(T) # print(T.item)
              preorder_traverse(T.left)
              preorder_traverse(T.right)
      ```
    
    - 현재 노드 n 방문하여 처리 -> V
    
    - 현재 노드 n의 왼쪽 서브트리로 이동 -> L
    
    - 현재 노드 n의 오른쪽 서브트리로 이동 -> R
  
  - 중위순회(inorder traversal) LVR : 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 방문
    
    - ```python
      def inorder_traverse(T):
          if T: # T is not None
              inorder_traverse(T.left)
              visit(T) # print(T.item)
              inorder_traverse(T.right)
      ```
    
    - 현재 노드 n의 왼쪽 서브트리로 이동 -> L
    
    - 현재 노드 n 방문하여 처리 -> V
    
    - 현재 노드 n의 오른쪽 서브트리로 이동 -> R
  
  - 후위순회(postorder traversal) LRV : 자식노드 좌우 먼저 방문 후 부모노드 방문
    
    - ```python
      def postorder_traverse(T):
          if T: # T is not none
              postorder_traverse(T.left)
              postorder_traverse(T.right)
              visit(T) # print(T.item)
      ```
    
    - 현재 노드 n의 왼쪽 서브트리로 이동 -> L
    
    - 현재 노드 n의 오른쪽 서브트리로 이동 -> R
    
    - 현재 노드 n 방문하여 처리 -> V

- 이진 트리의 표현
  
  - 1차원 배열을 이용하여 표현
    
    - 루트의 번호를 1로 함
    
    - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n부터 2^(n+1) - 1
  
  - 노드 번호의 성질
    
    - 노드 번호가 i인 노드의 부모 노드 번호 : i // 2
    
    - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : i * 2
    
    - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : i * 2 + 1
    
    - 레벨 n의 노드 번호 시작 번호 : 2^n
  
  - 높이가 h인 이진 트리를 위한 배열의 크기  = 2^(h+1) - 1 

- 이진 트리의 저장
  
  - 부모 번호를 인덱스로 자식 번호를 저장
  
  - 자식 번호를 인덱스로 부모 번호를 저장
  
  - 배열을 이용하면 편향 이진 트리의 경우 메모리 공간 낭비 발생 및 수정 불편
    
    - 연결리스트를 이용하여 표현하면 단점 극복 가능

- 이진 탐색 트리
  
  - 탐색작업을 효율적으로 하기 위한 자료구조이며 모든 원소는 서로 다른 유일한 키를 가진다
  
  - key(왼쪽 subtree) < key(root 노드) < key(오른쪽 subtree)
  
  - 중위 순회하면 오름차순으로 졍렬된 값을 얻을 수 있다
  
  - 연산
    
    - 탐색연산
      
      - 루트에서 시작해 탐색할 키 값 x를 루트 노드의 키 값과 비교한다
        
        - 키 값 x == 루트 노드 키 값 : 탐색 성공
        
        - 키 값 x < 루트 노드 키 값 : 루트 노드의 왼쪽 subtree 탐색
        
        - 키 값 x > 루트 노드 키 값 : 루트 노드의 오른쪽 subtree 탐색
    
    - 삽입연산
      
      - 탐색 연산을 수행해 실패가 결정되는 위치에 원소를 삽입한다
  
  - 성능
    
    - 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다.
      
      - 평균 O(log n) (균형적인 이진트리 경우)
      
      - 최악 O(n) (한쪽으로 치우친 경사 이진트리 경우)

- 힙(heap)
  
  - 완전 이진 트리에 있는 노드 중 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해 만든 자료구조
  
  - 최대 힙
    
    - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
    
    - 루트 노드 : 키 값이 가장 큰 노드
  
  - 최소 힙
    
    - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
    
    - 루트 노드 : 키 값이 가장 작은 노드
  
  - 힙 연산
    
    - 삽입
      
      - 삽입할 자리 확장
      
      - 확장한 자리에 삽입할 원소 저장
      
      - 힙 조건(최대힙/최소힙)에 맞게 자리 바꾸기
    
    - 삭제
      
      - 힙에서는 루트 노드의 원소만을 삭제할 수 있음
      
      - 루트 노드 원소 삭제
      
      - 마지막 노드 삭제하고 원소를 루트 노드에 부여
      
      - 힙 조건에 맞게 자리 바꾸기(두 자식 노드 중 큰 값(오른쪽)과 비교)
