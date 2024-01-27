import { useEffect, useState } from "react";
import Navbar from "../components/navbar";
import { useLocation, useParams } from "react-router-dom";
import Prompt from "../components/prompt";

export default function Assessment() {
    const { state } = useLocation();
    const { uid, sid } = useParams();
    const [excercise, setExcercise] = useState(1)

    const prompts = [
        {
            "prompt": "A",
            "overlay": null,
        },
        {
            "prompt": "B",
            "overlay": null,
        },
        {
            "prompt": "C",
            "overlay": null,
        },
    ]

    const handleNext = () => {
        if (excercise < 3){
            setExcercise((prevExcercise) => prevExcercise + 1)
        }
    }
  
    const sendDrawing = async ()  => {

    }

    return (
        <div>
            <Navbar logged={true} userId={uid} />
            <div className='bg-gray-200 w-screen h-draw flex flex-col justify-start items-center bg-gradient-to-r from-indigo-500 via-purple-300 to-red-400'>
                <div className="flex flex-col items-center space-y-2">
                    <span className="text-5xl">Draw {prompts[excercise-1].prompt}</span>
                    <span className="text-2xl ">Excercise {excercise}</span>
                </div>
                
                <Prompt/>
                <div className="space-x-64 mt-6">
                    <button
                        onClick={handleNext}
                        className="text-4xl bg-blue-800 text-white px-6 py-2 rounded-lg hover:bg-blue-800 focus:outline-none focus:ring focus:border-blue-300">
                        Finish
                    </button>
                </div>
            </div>
        </div>
    )
}