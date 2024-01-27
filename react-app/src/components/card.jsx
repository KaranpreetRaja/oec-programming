import React from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

const Card = ({ level, icon, user_id }) => {
    const navigate = useNavigate();
    
    const handleSelection = async () => {
        const amount = 10;

        try {
            const response = await axios.post('http://127.0.0.1:5000/api/session/create', {
                user_id,
                level,
                amount
            });
          
            const session_id = response.data.session_id;
            const data = response.data
            console.log('Selection successful! UID:', session_id);
            navigate(`/dashboard/${user_id}/assessment/${session_id}`, { state: {data} })
        } catch (error) {
            console.error('Selection failed:', error.message);
        }
    }

    return (
        <div onClick={handleSelection} className="w-60 h-72 bg-white rounded-lg border border-slate-800 transition-transform hover:scale-105 duration-500 ease-in-out bg-gradient-to-r from-purple-300 to-blue-500 hover:from-pink-400 hover:to-pink-300">
            <div className='w-full h-5/6 flex justify-center items-center'>
                {icon}
            </div>
            <div className='h-1/6 bg-slate-100 rounded-b-lg flex justify-center items-center bg-gradient-to-r from-purple-500 to-blue-500'>
                <span>Level {level}</span>
            </div>
        </div>
    );
};

export default Card;