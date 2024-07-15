import React, { useEffect, useState } from 'react';
import Col from "./Col";
import backgroundImageee from "../assets/game.png";

function Game() {
  const [board, setBoard] = useState([]);

  useEffect(() => {
    getBoard();
  }, []);

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
    <div className='gamepage'>
      <div>
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
          </div>
        </div>
      </div>
      <div >
        {board.map((row, index) => <Col key={index} rowindex={index} row={row} />)}
      </div>
    </div>
  );
}

export default Game;
