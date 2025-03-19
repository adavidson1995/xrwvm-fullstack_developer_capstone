import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Adjust the path based on your folder structure

function App() {
  return (
    <Routes>
      <Route path="/Login" element={<LoginPanel />} />
      <Route path="/Register" element={<Register />} />
    </Routes>
  );
}

export default App;