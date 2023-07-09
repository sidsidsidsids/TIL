import { useState, useEffect } from "react"

function Hello() {
  useEffect(() => {
    console.log("hi :)")
    return () => {
      console.log("bye :(")
    }
  }, [])
  return <h1>Hello</h1>;
}

function App() {
    const [counter, setValue] = useState(0);
    const [keyword, setKeyword] = useState("");
    const [showing, setShowing] = useState(false);
    const onClick = () => setValue((prev) => prev + 1);
    const onChange = (event) => setKeyword(event.target.value);
    useEffect(() => {console.log("I run only once")}, []);
    useEffect(() => {   
      console.log("i run when keyword changes")
    }, [keyword]);
    useEffect(() => {   
      console.log("i run when counter changes")
    }, [counter]);
    useEffect(() => {   
      console.log("i run when keyword & counter changes")
    }, [keyword, counter]);
    const onClick2 = () => setShowing((prev) => !prev)
    return(
      <div>
        {showing ? <Hello /> : null}
        <button onClick={onClick2}>{showing ? "Hide" : "Show"}</button>
        <br />
        <input 
        value={keyword} 
        onChange={onChange}
        type="text" 
        placeholder="Search here..." />
        <h1>{counter}</h1>
        <button onClick={onClick}>click me</button>
      </div>
    )

}

export default App;
