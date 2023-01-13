# 0113 TIL

### 복습

- ./ -> 현재 디렉토리. ls -a 를 통하여 ./ ../ 확인

- git init(초기화) : 상위 폴더에서 하지 말고 파일 버전이 있는 폴더에서 진행
  
  - ex) dev 폴더 내 project1, project2 폴더가 있으면 project 폴더들에서 각각 git init

- commit message : 목적(버전 설명) 넣기,  (대충 하면 실무자들이 뭐라함)

---

### github 계속

- shared repository
  
  - `git clone 링크` 를 통해서 repository 연결 (폴더 생성됨)
  
  - `git add ` `git commit -m ''`를 통해서 수정 후 커밋함
  
  - `git pull`를 통해 github 내용 로컬에서 업데이트
  
  - github repository - settings - collaborators 에서 협력자 초대

- shared repository 실습
  
  - 조장
    
    1. 로컬 레포지토리 생성
    
    2. README 및 파일 생성
    
    3. 원격 레포지토리 생성
    
    4. 로컬-원격 연결
    
    5. `git push` 이후 settings - Collaborator 추가
  
  - 조원
  1.    0. 초대 수락            
     
     1. 원격 레포지토리 `git clone 링크`
     
     2. 이후 `git pull`을 통해 변화 사항을 로컬로 가져옴 (업데이트)
     
     3. 파일 수정
     
     4. 원격 레포지토리에 `git push`    

- shared repository 와 fork의 차이와 유사
  
  - Repository의 권한
    
    - fork의 경우 원본의 직접적인 수정 불가능 -> 내 계정의 repo로 가져와 여기서 내가 권한을 갖게 됨
  
  - 병렬적인 작업환경 : 완전히 분리된 독립된 환경
  
  - fork와 PR(Pull Request)를 통하여 협업 가능

- .gitignore
  
  - 추가하지 않고자 할 파일들을 지정할 때 사용 (파일들을 추적하지 않음)
  
  - 적용 안될 때 `git rm -r --cached`

- git 되돌리기
  
  1. WD - 수정된 내용을 이전 상태(버전)로
  
  2. Staging Area 에서 WD로 다시 내리기
     
     1. root-commit 없는 경우 `git rm --cached <filename>`
     
     2. root-commit 있는 경우 `git restore --staged <filename>`
  
  3. Repository 단계 - 커밋이후 다시 Staging Area로
     
     git이 추적하고 있는 대상만 가능 (restore 이용)

- reset `git reset [옵션] <커밋 ID>`
  
  - 옵션
    
    - --soft : 돌아갈 commit 이후 commit 된 파일을 Staging Area로 돌려놓음
    
    - --mixed : 기본값, 돌아갈 commit 이후 commit 된 파일을 WD로 돌려놓음
                      (수정사항은 남는다)
    
    - --hard : untracked 파일 그대로
      
      | 옵션      | WD  | SA  | repo             |
      | ------- | --- | --- | ---------------- |
      | --soft  |     | ㅇ   | HEAD가 특정 커밋을 가르킴 |
      | --mixed | ㅇ   |     | HEAD가 특정 커밋을 가르킴 |
      | --hard  |     |     | HEAD가 특정 커밋을 가르킴 |
      
      > 
      > 단 `--hard` 옵션 사용시 기존 untracked 파일은 여전히 untracked로 남게 된다.
  
  - `git revert` : 새로운 커밋을 생성한다 = 이전의 커밋을 취소했다는 커밋
  
  - 



            
