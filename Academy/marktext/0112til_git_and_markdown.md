# Today I Learned

### GIT

- git / github (학생 인증하여 깃헙프로 무료 이용 가능)
1. git : 분산 버전 관리 프로그램
   
   > 중앙 집중식 관리가 아닌, 서버 그리고 개발자 개인의 PC에도 버전이 동시에 관리가 되어서 리소스를 분산으로 관리하는 것.
   > 
   > 백업 / 복구 / 협업 가능
   
   - Git 문법
     
     - 깃 시작하기
       
       1. 초기화 : `git init` : git local repository 초기화
          
          1. 로컬 레포지토리 생성 후 버전으로 관리할 파일을 `git add`로 단 한번이라도 Staging area에 옮겨줘야 한다.
             Why? `git init`해도 git은 어떤 파일의 버전을 관리해야 하는지 모름.
          
          2. 파일의 상태
             
             1. 최초 생성 시 untracked
             
             2. git add 후 staged
             
             3. git commit 후 tracked
             
             4. 파일의 수정이 있을 때 modified
             
             5. 최신이면 up-to-date
       
       2. `git add` : staging area로 버전관리 할 파일 옮기기
          
          1. `git add .` : 현재 위치한 WD(working directory)에 생긴 모든 변화 사항을 stage
          
          2. `git add {file name}` : file을 지정해서 stage
          
          3. `git commit -m '커밋 메세지'` :
             
             1. 커밋 메세지는 해당 버전이 어떤 목적에서 생성됐는지.
                
                1. 길이의 제한 O
       
       ---
   1. git 기본
      
      1. Working Directory
      
      2. Staging Area
      
      3. Repository
   
      2. VScode (terminal에서 bash로 열어야 함)
   
              1. git add .
   
              2. git commit -m '코멘트'
   
   3. git 명령어
      
      1. cd(경로 변경), mkdir(폴더 생성), rmdir(폴더 제거), touch(파일 생성), rm(파일 제거), ..(상위 폴더), ls(리스트 보기)
      
      ---

2. Remote Repository(원격 레포지토리 / 깃허브)
   
   - 레포지토리 연결하기 : `git remote add origin remote_repo url`
   
   - `git push origin master` : local -> remote로 upload
     
     - 인증 : remote repository에 push할 권한이 있는지 확인
   
   - add -> commit -> push
   1. github
      1. `git remote add origin remote_repo`
         `git push -u origin master`
         `(git remote remove origin)`
      2. 깃허브 상에서는 수정하지 말기
      3. add와 commit 후 git push 입력하여 github에 업로드
   2. local (git init 먼저)
      1. 로컬 폴더에서 `git config --global user.name` , `git config --global user.email`
      2. 수정 시 `git config --global user.name {계정명}` , 
         `git config --global user.email {이메일}` 입력
      3. **git init을 상하위 폴더에서 동시에 하면 오류 발생 + 최상위 폴더에서 get init 하지 말기**

### MARKDOWN

- 문서의 구조를 나타내기 위해 사용. 디자인으로 사용 X

- obsidian

- marktext

#### markdown 태그

> 프로그램마다 사용 방법 조금씩 다를 수 있음

1. '#'은 제목을 나타내며 1~6까지 문서 구조를 잡아주는 역할
   
   1. 글자 크기 조절용으로 사용하지 말기
   
   2. 3부터는 크기 차이 크게 없음
   
   3. 에디터에 따라 1~6을 넘어 더 많은 헤딩을 제공하기도 함

2. 별표('*')와 언더바('_')를 글 앞뒤에 붙여 스타일 편집 가능

          1. *한개는 이탤릭*  

          2. **두개는 볼드**

          3. ~~('~')를 통해 취소선 가능~~

3. 백틱(`)을 이용하여 코드 블럭 사용 (marktext : alt + ctrl + c)
   
      1. `print('백틱 한 쌍을 사용할 때')`
   
      2. 
   
   ```python
   print('백틱 세 쌍을 사용할 때')
   a = 25
   ```

4. URL이나 이미지 첨부 시 '[]'와 '()'를 사용하여 이용
   
   1. URL 첨부시 '[표시할 이름]''(해당 링크)' 방법으로 사용
   
   2. 이미지는 '![표시할 이름]''(해당 링크)' 로 사용 (이미지 크기 조절은 불가)
      
      [puppy]([puppy - Google 검색](https://www.google.com/search?q=puppy&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgqP2PhMH8AhUTad4KHatbBNEQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1))
      
      ![](0112til_assets/2023-01-12-11-57-40-image.png)

5. 언더바, 별표, 빼기를 세 개 사용하여 가로선 작성 가능(marktext : alt + ctrl + -)

---

___

***

6. | 와 -를 이용하여 표 작성 가능(marktext : ctrl + shift + t)
   
   | 제목1 | 제목2 |
   | --- | --- |
   | 내용1 | 내용2 |
