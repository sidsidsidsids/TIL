### panic
컴파일러가 모르는 에러
초기화되지 않은 map에 어떤 값을 넣을 수 없다
### Goroutines
다른 함수와 동시에 실행시키는 함수
함수 작동할때 앞에 go 붙이면 됨
프로그램이 작동하는 동안에만 유효함
-> 이게 무슨 소리냐면 메인 함수가 실행하는 동안에만 유효

#### Channel
Goroutine을 여러 개 사용하기 위해 func와 main을 연결하는 통로
```
package main

  

import (

    "fmt"

    "time"

)

  

func main() {

    c := make(chan bool)

    people := [2]string{"nico", "flynn"}

    for _, person := range people {

        go isSexy(person, c)

    }

    result := <-c

    fmt.Println(result)

}

  

func isSexy(person string, c chan bool) {

    time.Sleep(time.Second * 5)

    c <- true

}
```
Channel에서의 응답을 받기 전까지 프로그램이 종료되지 않음.
Goroutine의 갯수를 알기 때문에 Channel을 그 갯수를 넘어서게 만들 수 없음
채널로부터 응답을 받는 것은 Blocking Operation (함수가 뭔가를 받기 전까지 멈춘다는 의미) 

```
func hitURL(url string, c chan<- result)
```
send only channel func 정의 방법
### 3.7 Review
#### Question
> 강의 너무 잘 보고 있습니다.  질문 남겨 봅니다.  
> js 의 promise all 과 go routines 의 차이점이 무엇인지 궁금합니다.  
> What is the difference between "js-promise all" and "go-routine" ?

I would say that the difference is that go routines can communicate between each other, they are also blocking, so the main function will not end until all the other go routines finish, I guess it provides more features that allow synchronisation
### Code
```
package main

  

import (

    "errors"

    "fmt"

    "net/http"

)

  

type requestResult struct {

    url    string

    status string

}

  

var errRequestFailed = errors.New("Request failed")

  

func main() {

    results := make(map[string]string)

    c := make(chan requestResult)

    urls := []string{

        "https://www.airbnb.com/",

        "https://www.google.com/",

        "https://www.amazon.com/",

        "https://www.reddit.com/",

        "https://www.google.com/",

        "https://soundcloud.com/",

        "https://www.facebook.com/",

        "https://www.instagram.com/",

        "https://academy.nomadcoders.co/",

    }

    for _, url := range urls {

        go hitURL(url, c)

    }

  

    for i := 0; i < len(urls); i++ {

        result := <-c

        results[result.url] = result.status

    }

  

    for url, status := range results {

        fmt.Println(url, status)

    }

}

  

func hitURL(url string, c chan<- requestResult) {

    resp, err := http.Get(url)

    status := "OK"

    if err != nil || resp.StatusCode >= 400 {

        status = "FAILED"

    }

    c <- requestResult{url: url, status: status}

}
```