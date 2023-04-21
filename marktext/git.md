# Git Advanced

### Git undoing

- Working Directory 에서
  
  - git restore {파일 이름}
  
  - 지정 파일을 수정 전(직전 커밋)으로 되돌림
  
  - 되돌리면 내용 복원할 수 없으니 주의

- Staging Area에서
  
  - git rm --cached {파일 이름} (root-commit이 없는 경우, 저장소에 한 번도 commit 안 한 경우)
  
  - git restore --staged {파일 이름} (root-commit이 있는 경우)
  
  - Staging Area에 반영된 파일을 Working Directory로 되돌리기 (== unstage)

- Repository에서 (In local, not git repo)
  
  - git commit --amend
    
    - Staging Area에 새로 올라온 내용이 없다면 직전 커밋 메시지만 수정
    
    - Staging Area에 새로 올라온 내용이 있다면 직전 커밋을 덮어쓰기

### Git reset & revert

- git reset [옵션] {커밋 ID}
  
  - 프로젝트를 특정 커밋 상태로 되돌림, 해당 커밋 이후 쌓았던 커밋들은 전부 사라짐
  
  - 옵션
    
    - --soft
      
      - 되돌아간 커밋 이후 파일들을 Staging Area로 돌려놓음
    
    - --mixed
      
      - 되돌아간 커밋 이후 파일들을 Working Directory로 돌려놓음
      
      - git reset 옵션의 기본값
    
    - --hard
      
      - 되돌아간 커밋 이후 파일들을 모두 삭제
      
      - 기존 Untracked 파일은 사라지지 않고 Untracked로 남아있음
  
  - git reflog
    
    - reset 하기 전의 과거 커밋 내역 모두 조회
    
    - 이후 해당 커밋으로 reset 하면 hard 옵션으로 삭제된 파일도 복구 가능
    
    - 사용 지양하기

- git revert {커밋 ID}
  
  - 과거를 없었던 일로 만드는 행위로 이전 커밋을 취소한다는 새로운 커밋 생성
  
  - 커밋 ID는 취소하고 싶은 커밋 ID를 작성
    
    - reset은 커밋 내역을 삭제, revert는 새 커밋을 생성
      
      - ex) git reset 5sd2f42 : 5sd2f42라는 커밋으로 되돌린다
      
      - ex) git revert 5sd2f42 : 5sd2f42라는 커밋 한 개를 취소한다
        (이 커밋을 취소한다는 내용의 새 커밋을 생성함)

### Git branch

> 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 도구
> 
> 원본(master)에 대한 protection의 필요

- 조회
  
  - git branch # 로컬 저장소의 브랜치 목록 확인
  
  - git branch -r # 원격 저장소의 브랜치 목록 확인

- 생성
  
  - git branch {브랜치 이름} # 새 보랜치 생성
  
  - git branch {브랜치 이름} {커밋 ID} # 특정 커밋 기준으로 브랜치 생성

- 삭제
  
  - git branch -d {브랜치 이름} # 병합된 브랜치만 삭제 가능
  
  - git branch -D {브랜치 이름} # 강제 삭제

- git switch
  
  - 현재 브랜치에서 다른 브랜치로 HEAD를 이동시킴
  
  - git switch {브랜치 이름} # 다른 브랜치로 이동
  
  - git switch -c {브랜치 이름} # 브랜치를 새로 생성 및 이동
  
  - git switch -c {브랜치 이름} {커밋 ID} # 특정 커밋 기준으로 브랜치 생성 및 이동
  
  - switch 하기 전에 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의

### Git merge

> 분기된 브랜치들을 하나로 합치는 명령어
> 
> master 브랜치가 상용이므로 주로 master 브랜치에 병합

- git merge {합칠 브랜치 이름}
  
  - Fast-Forward
    
    - 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
  
  - 3-way Merge
    
    - 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법
  
  - Merge Conflict
    
    - 같은 부분을 수정하여 충돌이 발생했을 때 이를 해결하며 병합하는 방법
