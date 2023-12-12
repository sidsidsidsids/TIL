### 배열 합치기
핵심은 배열에 ... 을 넣는냐 안넣느냐
#### 배열 안 내용물 합치기
```
var jobs []extractedJob

    totalPages := getPages()

    fmt.Println(totalPages)

    for i := 0; i < totalPages; i++ {

        extraction := getPage(i)

        jobs = append(jobs, extraction...)

    }
```

#### 배열 안 배열 넣기
```
var jobs []extractedJob

    totalPages := getPages()

    fmt.Println(totalPages)

    for i := 0; i < totalPages; i++ {

        extraction := getPage(i)

        jobs = append(jobs, extraction)

    }
```
### 4.4 Review (Error)
> mac 기준 vsc에서는 잘 보이는데 excel에서 한글 깨져서 열리시는 분 인코딩 문제이니  
file, err := os.Create("jobs.csv") 
checkErr(err)  
밑에  
utf8bom := []byte{0xEF, 0xBB, 0xBF}  
file.Write(utf8bom)  
추가해주시면 vsc, excel 둘다 잘 보입니당
### Code
```
package main

  

import (

    "encoding/csv"

    "fmt"

    "log"

    "net/http"

    "os"

    "strconv"

    "strings"

  

    "github.com/PuerkitoBio/goquery"

)

  

type extractedJob struct {

    id    string

    title string

    corp  string

}

  

var baseURL string = "https://www.saramin.co.kr/zf_user/search/recruit?&searchword=python"

  

func main() {

    var jobs []extractedJob

    c := make(chan []extractedJob)

    totalPages := getPages()

    for i := 0; i < totalPages; i++ {

        go getPage(i, c)

    }

  

    for i := 0; i < totalPages; i++ {

        extractedJobs := <-c

        jobs = append(jobs, extractedJobs...)

    }

  

    writeJobs(jobs)

    fmt.Println(len(jobs), "개의 데이터를 추출했습니다")

}

  

func getPage(page int, mainC chan<- []extractedJob) {

    var jobs []extractedJob

    c := make(chan extractedJob)

    pageURL := baseURL + "&recruitPage=" + strconv.Itoa(page+1)

    res, err := http.Get(pageURL)

    checkErr(err)

    checkCode(res)

  

    defer res.Body.Close()

  

    doc, err := goquery.NewDocumentFromReader(res.Body)

    checkErr(err)

  

    searchCards := doc.Find(".item_recruit")

  

    searchCards.Each(func(i int, s *goquery.Selection) {

        go extractJob(s, c)

  

    })

  

    for i := 0; i < searchCards.Length(); i++ {

        job := <-c

        jobs = append(jobs, job)

    }

    mainC <- jobs

  

}

  

func extractJob(card *goquery.Selection, c chan<- extractedJob) {

    id, _ := card.Attr("value")

    title := cleanString(card.Find(".area_job>.job_tit>a").Text())

    corp := cleanString(card.Find(".area_corp>.corp_name>a").Text())

    c <- extractedJob{

        id:    id,

        title: title,

        corp:  corp}

}

  

func getPages() int {

    pages := 0

    res, err := http.Get(baseURL)

    checkErr(err)

    checkCode(res)

  

    defer res.Body.Close()

  

    doc, err := goquery.NewDocumentFromReader(res.Body)

    checkErr(err)

    doc.Find(".pagination").Each(func(i int, s *goquery.Selection) {

        pages = s.Find("a").Length()

    })

    return pages

}

func writeJobs(jobs []extractedJob) {

    file, err := os.Create("jobs.csv")

    checkErr(err)

    utf8bom := []byte{0xEF, 0xBB, 0xBF}

    file.Write(utf8bom)

  

    w := csv.NewWriter(file)

    defer w.Flush()

  

    headers := []string{"ID", "Title", "Corp"}

  

    wErr := w.Write(headers)

    checkErr(wErr)

  

    for _, job := range jobs {

        jobSlice := []string{job.id, job.title, job.corp}

        jwErr := w.Write(jobSlice)

        checkErr(jwErr)

    }

}

func checkErr(err error) {

    if err != nil {

        log.Fatalln(err)

    }

}

  

func checkCode(res *http.Response) {

    if res.StatusCode != 200 {

        log.Fatalln("Request failed with Status: ", res.StatusCode)

    }

}

  

func cleanString(str string) string {

    return strings.Join(strings.Fields(strings.TrimSpace(str)), " ")

}
```