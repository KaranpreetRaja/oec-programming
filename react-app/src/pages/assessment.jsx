import { useEffect, useState } from "react";
import Navbar from "../components/navbar";
import { useLocation, useParams } from "react-router-dom";
import Prompt from "../components/prompt";
import Score from "../components/score";
import { ReactPainter } from "react-painter";
import axios from "axios";

export default function Assessment() {
  const { state } = useLocation();
  const { uid, sid } = useParams();
  const [exercise, setExercise] = useState(1);
  const [isScore, setIsScore] = useState(!true);
  const [accuracy, setAccuracy] = useState(0);

  const [data, setData] = useState(null);

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
                handleTesting(imageDownloadUrl);
              }}
              className={`${
                !isScore ? "" : "hidden"
              } ml-auto mr-auto mt-6 w-36 text-4xl bg-blue-800 text-white px-6 py-2 rounded-lg hover:bg-blue-800 focus:outline-none focus:ring focus:border-blue-300`}
            >
              Finish
            </button>
          ) : null}
          {imageDownloadUrl ? (
            <a href={imageDownloadUrl} download>
              Download
            </a>
          ) : null}
        </div>
      )}
    />
  );

  const fileToDataUri = (file) =>
    new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (event) => {
        resolve(event.target.result);
      };
      reader.readAsDataURL(file);
    });

  function dataURLtoBlob(dataurl) {
    return fetch(dataurl).then((response) => response.blob());
  }

  const handleTesting = async (url) => {
    console.log(url);
    const blob = dataURLtoBlob(url);

    // console.log(blob)
    // try {
    //     const response = await axios.post('http://oecprogramming.pythonanywhere.com/test/json', {
    //         blob
    //     });
    //     console.log('successful! :', response.data);
    // } catch (error) {
    //     console.error('failed:', error.message);
    // }
  };

  const prompts = [
    {
      prompt: "A",
      overlay: null,
    },
    {
      prompt: "B",
      overlay: null,
    },
    {
      prompt: "C",
      overlay: null,
    },
  ];

  const handleFinish = async (blob) => {
    console.log(blob);

    const session_id = sid;
    const user_id = uid;
    const answer = {}; // TODO: Get blob
    const prompt = prompts[exercise - 1].prompt;

    const question = {
      prompt,
      answer,
    };

    // try {
    //     const response = await axios.post('link here', {
    //         session_id,
    //         user_id,
    //         question
    //     });
    //     console.log('Drawing sent successful! :', response.data);
    // } catch (error) {
    //     console.error('Login failed:', error.message);
    // }

    // setIsScore((prevIsScore) => !prevIsScore)
    // setAccuracy(90)
  };

  const handleNext = () => {
    if (exercise < prompts.length) {
      setExercise((prevExercise) => prevExercise + 1);
      setIsScore((prevIsScore) => !prevIsScore);
    }
  };

  return (
    <div>
      <Navbar logged={true} userId={uid} />
      <div className="bg-gray-200 w-screen h-draw flex flex-col justify-start items-center bg-gradient-to-r from-indigo-500 via-purple-300 to-red-400">
        <div className="flex flex-col items-center space-y-2">
          <span className="text-5xl">Draw {prompts[exercise - 1].prompt}</span>
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
