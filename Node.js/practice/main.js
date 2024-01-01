const http = require("http");
let count = 0;
const server = http.createServer((req, res) => {
  log(count);
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.write("Hello\n");
  setTimeout(() => {
    res.end("Node.js");
  }, 2000);
});

function log(count) {
  count = count + 1;
  console.log(count);
}

server.listen(8000, () => console.log("OPEN"));
