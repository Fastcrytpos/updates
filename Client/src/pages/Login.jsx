import React from 'react';
import { useState } from 'react'
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom'

import backgroundImageee from "../assets/antonio-alcantara-DWIbVgYzu6U-unsplash.jpg"

function Login() {
  const [Username,setUsername]=useState()
  const [Password,setPassword]=useState()
 
  const navigate = useNavigate()
  
  function handlesubmit(e){
    e.preventDefault()
    console.log(Password)
    const formData={
      username:Username,
      
      password:Password,
    }
    console.log(JSON.stringify(formData))

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: JSON.stringify(formData),
      redirect: "follow"
    };

    fetch("http://localhost:5000/register", requestOptions)
      .then((response) => response.text())
      .then((result)=> console.log(result),navigate('/game'))
      .catch((error) => console.error(error));

      // onChange={(e)=>setUsername(e.target.value)
  }



  return (
    <div 
    style={{
      backgroundImage: `url(${backgroundImageee})`,
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
        <form  onSubmit={handlesubmit} className="px-8 pb-8 w-full flex flex-col">
          <label htmlFor="username" className="block text-sm mb-2">username</label>
          <input type="text" onChange={(e)=>setUsername(e.target.value)} id="username" name="username" className="w-full mb-4 p-2 border rounded-md" />
          
          <label htmlFor="password" className="block text-sm mb-2">password</label>
          <input type="password"  onChange={(e)=>setPassword(e.target.value)} id="password" name="password" className="w-full mb-4 p-2 border rounded-md" />
          
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
