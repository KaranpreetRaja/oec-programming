import { Link } from "react-router-dom";
import Navbar from "../components/navbar";

export default function Home() {
    return (
       <div>
            <Navbar/>
            <div className="home-section bg-gradient-to-r from-indigo-400 h-screen">
                    <div className="home-content">
                        <h1 className="home-text">Grow <span className='highlight'>Independance</span> Effortlessly with AI-Powered Writing Training</h1>
                        <Link to="/signup" className="text-black font-bold text-xl">
                            <button className='home-btn hover:bg-blue-700 transition ease-in-out duration-300'>Get started</button>
                        </Link>
                        <p>Practice Writing</p>
                    </div>
            </div>
       </div> 
    )
}