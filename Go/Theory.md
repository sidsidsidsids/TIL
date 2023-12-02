### Go PATH
Go는 Node.js, Python과 같이 원하는 폴더에서 작업할 수 없다
(Window 기준 C:/Users/(사용자이름)/go 에서 작업)

### Package
go의 표준 라이브러리는 매우매우매우 광범위하다
#### main
```
package main

func main() {

}
```
컴파일을 위한 정의, 선택이 아닌 필수
#### fmt
formatting을 위한 package
#### export
함수를 대문자로 작성하면(Pascal Case) 패키지를 import 해올 수 있음

### Variables/Constants
JavaScript와 비슷한 개념 (변수와 상수)
#### Constant
```
const name string = "name"
```
#### Variable
```
var name string = "name"
```
```
# short way, go find type for the variable
name := "name"
# it only works to variable *in func*
```

### Function
#### Example
```
func multiply(a int, b int) int {
    return a * b
}
func multiply(a, b int) int {
    return a * b
}
```
TypeScript처럼 받는 인자가 어떤 type인지, return 값이 어떤 type인지 명시해줘야 함
#### Multiple Return
```
func lenAndUpper(name string) (int, string) {
    return len(name), strings.ToUpper(name)
}
```
Go는 여러 타입의 값을 return할 수 있음
#### _
Go에서는 사용하지 않는 값이 있으면 작동하지 않음 -> 이를 해결하기 위해 _ 사용
ex) totalLength, _  := lenAndUpper(name)
#### Repeat
```
func repeatMe(words ...string) {
    fmt.Println(words)
}
func main() {
    repeatMe("a", "b", "c")
}
```
#### Naked Return
```
func lenAndUpper(name string) (length int,uppercase string) {
    length = len(name)
    uppercase = strings.ToUpper(name)
    return
}
```
어떤 Variable을 return할 지 정의함으로써 표현할 수 있다
#### defer
function이 값을 return한 후 실행될 코드
#### Loop
```
func superAdd(numbers ...int) int {
    for index, number := range numbers {
        fmt.Println(index, number)
    }
    return 3
}

func superAdd(numbers ...int) int {
    for i := 0; i < len(numbers); i++ {
        fmt.Println(numbers[i])
    }
    return 3
}
```
range 쓸 때 index에 _ 쓰면 값만 사용할 수 있겠죠
#### if else
```
func canIdrink(age int) bool {
    if age < 18 {
        return false
    }
    return true
}

### variable expression
func canIdrink(age int) bool {
    if koreanAge := age + 2; koreanAge < 18 {
        return false
    }
    return true
}

```
#### Switch
값을 체크하는 방법. JavaScript와 비슷
```
switch {
case age < 18:
	return false
case age == 18:
	return true
}
return false
```
### Pointers
Low level Programming
& : 주소
** : 주소에 담긴 값
```
func main() {
    a := 2
    b := a
    fmt.Println(a, b)
}
```
이 상황에서 a 값이 바뀌어도 b의 값은 변하지 않는다. b의 값은 복사할 때의 그 값을 유지
```
func main() {
    a := 2
    b := &a
    a = 5
    fmt.Println(a, *b)
}
```
값이 함께 바뀌도록 하려면 메모리 주소값을 복사해야함(&)
(b를 그대로 print하면 메모리 주소값이 출력, 별표를 붙여 그 주소의 값이 출력되게끔 함)
```
func main() {
    a := 2
    b := &a
    *b = 21
    fmt.Println(a)
}
```
b를 바꿔 a값을 갱신할 수도 있음
### Arrays and Slices
#### Array
제한이 있는 list, 배열 크기 정의해줘야함
```
func main() {
    names := [5]string{"a", "b", "c"}
    names[3] = "d"
    names[4] = "e"
    names[5] = "f" // error!
}
```
#### Slice
제한이 없는 array(파이썬의 list 같은 개념)
```
func main() {
    names := []string{"a", "b", "c"}
    names = append(names, "f")
}
```
### Maps
key, value를 가짐 (python dictionary와 유사)
```
func main() {
    nico := map[string]string{"name": "nico", "age": "12"}
    fmt.Println(nico)
}
```
### Structs
class + object?
```
package main

import "fmt"

type person struct {
    name    string
    age     int
    favFood []string
}

func main() {
    foods := []string{"ramen", "kimbab"}
    nico := person{name: "nico", age: 18, favFood: foods}
    fmt.Println(nico)
}
```
Go는 Class, Object가 없다. constructor method도 없다 (python에서의 init, javascript에서의 constructor())