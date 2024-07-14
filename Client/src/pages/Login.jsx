import React from 'react';
import { Link } from 'react-router-dom';
import backgroundImage from "../assets/antonio-alcantara-DWIbVgYzu6U-unsplash (1).jpg"

function Login() {
  return (
    <div 
    style={{
      backgroundImage: `url(${backgroundImage})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat',
      height: '100vh', // Add a height to the div to make it visible
      width: '100vw', // Add a width to the div to make it visible
    }}
    className=" flex items-center justify-center h-screen">
      <div className="bg-white rounded-lg shadow-lg w-80 flex flex-col items-center">
        <div className="relative w-full">
          <div className="triangle absolute top-0 left-0"></div>
          <h2 className="text-center text-xl font-bold py-8">Login</h2>
        </div>
        <form className="px-8 pb-8 w-full flex flex-col">
          <label htmlFor="username" className="block text-sm mb-2">username</label>
          <input type="text" id="username" name="username" className="w-full mb-4 p-2 border rounded-md" />
          
          <label htmlFor="password" className="block text-sm mb-2">password</label>
          <input type="password" id="password" name="password" className="w-full mb-4 p-2 border rounded-md" />
          
          <button type="submit"className="buttonsubmit" >Login</button>

          <div className="flex justify-between text-sm mb-1 mt-6">
            <a href="#" className="text-gray-600">forgot password?</a>
            <Link to="/signup" className="text-gray-600">sign up</Link>
          </div>
          
        </form>
      </div>
    </div>
  );
}

export default Login;
