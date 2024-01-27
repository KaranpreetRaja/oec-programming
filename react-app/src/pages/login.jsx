import axios from 'axios';
import Navbar from '../components/navbar';
import { Link, useNavigate } from 'react-router-dom';

export default function Login(){
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();

        const email = e.target.elements.email.value;
        const password = e.target.elements.password.value;

        console.log(email);
        console.log(password);

        try {
            const response = await axios.post('http://127.0.0.1:5000/api/user/login', {
                email,
                password
            });

            const uid = response.data.uid;
            console.log('Login successful! UID:', uid);
            navigate(`/dashboard/${uid}`);
        } catch (error) {
            console.error('Login failed:', error.message);
        }

        
    
    }
    
    return(
        <div>
            <Navbar/>
            <div className="login-form-container">
                <form className="login-form" onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="email">Email</label>
                        <input
                            className="input-field"
                            type="email"
                            id="email"
                            name="email"
                            placeholder="Enter your email"
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            className="input-field"
                            type="password"
                            id="password"
                            name="password"
                            placeholder="Enter your password"
                            required
                        />
                    </div>
                    <button className="btn-submit bg-blue-500 hover:bg-blue-700 transition ease-in-out duration-300 mt-3" type="submit">
                        Login
                    </button>
                </form>
            </div>
        </div>
    )
}