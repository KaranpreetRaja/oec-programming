import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from './pages/home';
import Login from "./pages/login";
import Signup from "./pages/signup";
import Dashboard from "./pages/dashboard";
import Assessment from "./pages/assessment";

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />}/>
            <Route path="/login" element={<Login />}/>
            <Route path="/signup" element={<Signup />}/>
            <Route path="/dashboard/:uid" element={<Dashboard />} />
            <Route path="/dashboard/:uid/assessment/:sid" element={<Assessment />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App