import React, { useEffect, useState } from 'react';
import Col from "./Col";
import backgroundImageee from "../assets/beach.jpg"

function Game() {
  const [board, setBoard] = useState([]);


  function getBoard() {
    const myHeaders = new Headers();
    myHeaders.append("Cookie", "session=.eJyrVkrKTyxKUbKKjlZSUNJRSgZi7HSsTjQeWRANUkHYDAUoDzsmTkUBlIedhpmBWxURZsTWAgCYyzSv.ZpUa3A.yhZBXOKFHxBW89EAioOJsew-Aag");
  
    const requestOptions = {
      method: "GET",
      headers: myHeaders,
      redirect: "follow"
    };
    
    fetch("http://127.0.0.1:5000/game", requestOptions)
      .then((response) => response.json())
      .then((result) => setBoard(result))
      .catch((error) => console.error('Error:', error));
  }

  return (
    <div style={{
        backgroundImage: `url(${backgroundImageee})`,
        backgroundSize: '100%',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        height: '100vh',
        width: '100vw',
      }}>
      <div >
        <div
          style={{
            width: "100%",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div>
            <p>Welcome Player:</p>
          </div>
          <div>
            <button className="w3-btn w3-round w3-red">Logout</button>
            <button className="w3-btn w3-round w3-teal w3-margin-left">New Game</button>
            <button onClick={getBoard} className="w3-btn w3-round w3-teal ">START</button>
          </div>
        </div>
      </div  >
      <div className="flex items-center justify-center h-screen" >
      <div>
        {board.map((row, index) => 
        
        <Col key={index}
              rowindex={index} 
              row={row} 
              board={board} 
              setBoard={setBoard}
        
        />
        
        )}


      </div>
      </div>
    </div>
  );
}

export default Game;
