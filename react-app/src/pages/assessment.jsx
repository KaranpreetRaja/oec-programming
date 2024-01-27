import { useEffect, useState } from "react";
import Navbar from "../components/navbar";
import { useLocation, useParams } from "react-router-dom";
import Score from "../components/score";
import { ReactPainter } from "react-painter";
import axios from "axios";

export default function Assessment() {
  const { state } = useLocation();
  const { uid, sid } = useParams();
  const [exercise, setExercise] = useState(1);
  const [isScore, setIsScore] = useState(!true);
  const [accuracy, setAccuracy] = useState(0);

  const Drawable = () => (
    <ReactPainter
      width={800}
      height={700}
      onSave={(blob) => console.log(blob)}
      render={({ triggerSave, canvas, imageDownloadUrl }) => (
        <div className="flex flex-col justify-center">
          <div className="bg-white">{canvas}</div>
          <button
            onClick={() => {
              triggerSave();
            }}
            className={`${
              !isScore ? "" : "hidden"
            } ml-auto mr-auto mt-6 w-36 text-2xl bg-blue-400 text-white px-6 py-2 rounded-lg hover:bg-blue-500 focus:outline-none focus:ring focus:border-blue-300`}
          >
            Save
          </button>
          {imageDownloadUrl ? (
            <button
              onClick={() => {
                handleFinish(imageDownloadUrl);
              }}
              className={`${
                !isScore ? "" : "hidden"
              } ml-auto mr-auto mt-6 w-36 text-4xl bg-blue-800 text-white px-6 py-2 rounded-lg hover:bg-blue-800 focus:outline-none focus:ring focus:border-blue-300`}
            >
              Finish
            </button>
          ) : null}
        </div>
      )}
    />
  );

    function dataURLtoBlob(dataurl) {
      return fetch(dataurl).then((response) => response.blob());
    }


    const handleFinish = async (url) => {

        const blob = dataURLtoBlob(url)

        const session_id = sid;
        const user_id = uid;
        const answer = blob
        const prompt = state.prompts[exercise-1].prompt

        const question = {
            prompt,
            answer
        }
        
        try {
            const response = await axios.post('http://127.0.0.1:5000/api/session/submit', {
                session_id,
                user_id,
                question
            });
            console.log('Drawing sent successful! :', response.data);
            const accuracy = response.data.accuracy;
            setAccuracy(accuracy)
            setIsScore((prevIsScore) => !prevIsScore)
        } catch (error) {
            console.error('Login failed:', error.message);
        }
  };

  const handleNext = () => {
    if (exercise < state.prompts.length) {
      setExercise((prevExercise) => prevExercise + 1);
      setIsScore((prevIsScore) => !prevIsScore);
    }
  };

  return (
    <div>
      <Navbar logged={true} userId={uid} />
      <div className="bg-gray-200 w-screen h-draw flex flex-col justify-start items-center bg-gradient-to-r from-indigo-500 via-purple-300 to-red-400">
        <div className="flex flex-col items-center space-y-2">
          <span className="text-5xl">Draw {state.prompts[exercise - 1].prompt}</span>
          <span className="text-2xl ">Exercise {exercise}</span>
        </div>

        <div className={!isScore ? "" : "hidden"}>
          <Drawable />
        </div>

        <Score visibility={isScore} accuracy={accuracy} />
        <div className="mt-6">
          <button
            onClick={handleNext}
            className={`${
              isScore ? "" : "hidden"
            } text-4xl bg-blue-800 text-white px-6 py-2 rounded-lg hover:bg-blue-800 focus:outline-none focus:ring focus:border-blue-300`}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}
