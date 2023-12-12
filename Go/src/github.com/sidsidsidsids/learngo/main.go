package main

import (
	"os"
	"strings"

	"github.com/labstack/echo"
	"github.com/sidsidsidsids/learngo/scrapper"
)

const FileName string = "jobs.csv"

func handleHome(c echo.Context) error {
	return c.File("home.html")
}
func handleScrape(c echo.Context) error {
	defer os.Remove(FileName)
	term := strings.ToLower(scrapper.Cleanstring(c.FormValue("term")))
	scrapper.Scrape(term)
	return c.Attachment(FileName, FileName)
}
func main() {
	e := echo.New()
	e.GET("/", handleHome)
	e.POST("/scrape", handleScrape)
	e.Logger.Fatal(e.Start(":1323"))
}
