import Headers from "./header/Headers";
import { BrowserRouter,Routes,Route } from "react-router-dom";
import Home from "./home/Home";
import Login from "./auth/Login";
import Register from "./auth/Register";

function App() {
  return (
    <div className="">
      <BrowserRouter>
         <Routes>
            <Route path="/" element={<Home/>}> </Route>
            <Route path="/login"  element={<Login/>}></Route>
            <Route path="/register" element={<Register/>}></Route>
         </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
