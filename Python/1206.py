'''
10회 반복해서 진행
건물의 갯수, 높이 입력받음
각 건물마다(3~98) 양옆 두칸에 더 높은 건물이 있는지
    없다면 네 건물 중 가장 높은 건물만큼 뺀 값이 조망권
횟수와 조망권 수 출력
'''

count = 0 #테스트 케이스를 셀 변수 선언
while count < 10 : # 10개의 테스트 케이스가 되도록 반복
    N = int(input()) # 건물의 개수 입력받음
    buildings = list(map(int,input().split())) # 건물들의 높이 입력받음
    jomang = 0 # 조망권을 셀 변수 선언
    for i in range(2,N-2): # 첫 건물부터 마지막 건물 까지
        others = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
        # 양 옆에 2개씩 총 4개의 건물을 리스트로 생성
        others_max = others[0] # 구간 내 첫 건물을 기준으로
        for j in range(1,4): # 기준으로 삼은 첫 건물을 제외한 다른 건물들
            if others[j] > others_max: # 기준보다 크다면
                others_max = others[j] # 새로 기준값이 됨
            else :
                pass # 그 외의 경우 pass
        if buildings[i] > others_max: # 기준값보다 가운데 건물이 큰 경우
            jomang += buildings[i] - others_max # 큰 만큼 조망권에 합산
    print(f'#{count+1} {jomang}') # 출력
    count += 1
