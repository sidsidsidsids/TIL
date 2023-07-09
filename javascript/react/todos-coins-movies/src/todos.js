import { useState } from "react"
function App() {
  const [toDo, settoDo] = useState("");
  const [toDos, settoDos] = useState([]);
  const onChange = (event) => settoDo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (toDo === "") {
      return;
    }
    settoDos((currentArray) => [toDo, ...currentArray])
    settoDo("");
    
  }
  console.log(toDos)
  return (
    <div>
      <h1>My Todos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input type="text"
        onChange={onChange}
        value={toDo}
        placeholder="Write your to do" />
        <button>Add to Do</button>
      </form>
      <hr />
      <ul>
        {toDos.map((todo, index) => (<li key={index}>{todo}</li>))}
      </ul>
    </div>
  );
}

export default App;
