package scrapper

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
	id    string
	title string
	corp  string
}

// Scrape Indeed by a term
func Scrape(term string) {
	var baseURL string = "https://www.saramin.co.kr/zf_user/search/recruit?&searchword=" + term
	var jobs []extractedJob
	c := make(chan []extractedJob)
	totalPages := getPages(baseURL)
	for i := 0; i < totalPages; i++ {
		go getPage(i, baseURL, c)
	}

	for i := 0; i < totalPages; i++ {
		extractedJobs := <-c
		jobs = append(jobs, extractedJobs...)
	}

	writeJobs(jobs)
	fmt.Println(len(jobs), "개의 데이터를 추출했습니다")
}

func getPage(page int, url string, mainC chan<- []extractedJob) {
	var jobs []extractedJob
	c := make(chan extractedJob)
	pageURL := url + "&recruitPage=" + strconv.Itoa(page+1)
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
	title := Cleanstring(card.Find(".area_job>.job_tit>a").Text())
	corp := Cleanstring(card.Find(".area_corp>.corp_name>a").Text())
	c <- extractedJob{
		id:    id,
		title: title,
		corp:  corp}
}

func getPages(url string) int {
	pages := 0
	res, err := http.Get(url)
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
	defer file.Close()

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

func Cleanstring(str string) string {
	return strings.Join(strings.Fields(strings.TrimSpace(str)), " ")
}
