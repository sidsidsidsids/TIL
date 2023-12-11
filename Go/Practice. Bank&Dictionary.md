### Private&Public
함수명을 소문자로 시작하면 private
함수명을 대문자로 시작하면 public
### Constructor
Go는 Construtctor가 없다. -> function으로 construct하거나 struct를 만들어야 함
### 2.0 Review
#### Error
에러명
main.go:6:2: no required module provides package github.com/sidsidsidsids/learngo/banking: go.mod file not found in current directory or any parent directory; see 'go help modules'
해결
go mod init
#### Question
>return &account 의 반환값은 주소값인데..  main의 fmt.Println(account) 결과값은 &{nico 0} 이렇게 나옵니다.  이해가 안가는 부분은 주소값은 예를 들어 "0x2334a255" 이런 주소값으로 반환되어야 하는거 아닌가요?

&account는 변수 account의 주소를 나타냅니다. 주소는 실제로 메모리 상의 위치를 나타내는 값으로, 예를 들어 "0x2334a255"와 같은 형태일 수 있습니다. 하지만 Go 언어에서는 fmt.Println() 함수가 변수를 포맷팅하여 출력할 때 주소 값이 아닌 해당 변수의 내용을 출력합니다.  
  
Go 언어에서 구조체(struct)는 필드의 모음입니다. &account는 구조체 변수 account의 주소를 반환합니다. fmt.Println(account)는 account 변수의 내용을 출력하는데, 여기서 내용은 구조체의 필드 값들입니다.  
  
예를 들어, account 구조체에 name 필드와 balance 필드가 있다고 가정해봅시다. account 변수의 주소가 "0x2334a255"라면, fmt.Println(account)는 account의 내용을 출력할 때 해당 주소로 접근하여 구조체의 필드 값들을 출력합니다. 출력 결과로는 구조체의 필드 값들이 보여지는 것이기 때문에 "&{nico 0}"와 같은 형태가 나타날 수 있습니다.  
  
결론적으로, fmt.Println()은 변수의 주소 값이 아니라 변수의 내용을 출력하며, 구조체 변수의 경우 필드 값들이 출력됩니다.

>NewAccount 부분에서 이해가 안되는게 있습니다. return 타입을 *Account로 지정하였고 실제 리턴되는 것은 &account인데 왜 *Account과 &account는 같은 타입인건가요? &은 메모리 주소이고 *은 &의 실제 값인 걸로 알고 있는데 그러면 둘의 타입이 달라보이는데 어떻게 동작하는 건가요?

자문자답 남깁니다. 리턴 타입에 붙은 *는 메모리 값을 나타내는 것이 아니라 포인터 타입이라는 것을 나타내는 것이군요

### Method
```
// Deposit x amount on your account

func (a Account) Deposit(amount int) {

    a.balance += amount

}
```
func와 func 이름 사이에 receiver ( )를 넣어서 method를 만듬
(a Account) = a의 type이 Account다 라는 의미

지금 이게 작동할까요? 안되죠
왜냐? receiver가 복사본을 받고 있으니까
복사본을 만들지 않고 실제 값을 증가시켜줘야하죠
go에게 account나 receiver를 복사하지 않도록
```
// Deposit x amount on your account

func (a *Account) Deposit(amount int) {

    a.balance += amount

}
```

**포인터는 구조체(struct)일 경우에만 사용**
(maps 같은 경우 Go가 자동으로 * 사용)
### Error Handling
Go는 exception이 없다 (try-except, try-catch 같은 거)
직접 handling 해줘야 함
```
// Withdraw x amount from your account

func (a *Account) Withdraw(amount int) error {

    if a.balance < amount {

        return errors.New("can't withdraw")

    }

    a.balance -= amount

    return nil

}
```

Go에서는 error가 발생해도 프로젝트가 종료되지 않음
종료하려면 다음과 같이 작성
```
err := account.Withdraw(30)

    if err != nil {

        log.Fatalln(err)

    }
```

log.Fatal =print후 프로그램을 종료시킴

### String 호출
python class 에서의 _ _ str _ _ 출력과 같이 하는 법
```
func (a Account) String() string {

    return fmt.Sprint(a.Owner(), "'s account. \nHas: ", a.Balance())

}
```
```
func main() {

    account := accounts.NewAccount("nico")

    account.Deposit(10)

    fmt.Println(account)

}
```
결과:
nico's account. 
Has: 10

### 2.6 Review
>Why "Update" method doesn't include point receiver(*) beside Dictionary? Is this reason equal to why "Delete" method doesn't include point receiver?(reason: Dictionary is hash map)  
  So, if I use struct, when I make a Update, Delete method, must I use point receiver? Plz reply! Thanks! :)

Correct!

### Code
```
package main

  

import (

    "fmt"

  

    "github.com/sidsidsidsids/learngo/mydict"

)

  

func main() {

    dictionary := mydict.Dictionary{"first": "First word"}

    baseword := "hello"

    dictionary.Add(baseword, "First")

    dictionary.Search(baseword)

    dictionary.Delete(baseword)

    word, err := dictionary.Search(baseword)

    if err != nil {

        fmt.Println(err)

    }

    fmt.Println(word)

}
```