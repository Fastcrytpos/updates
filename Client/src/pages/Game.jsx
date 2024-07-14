import React from 'react'
import backgroundImageee from "../assets/game.png";

function Game() {
  return (
    <div
    style={{
      backgroundImage: `url(${backgroundImageee})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat',
      height: '100vh',
      width: '100vw',
    }}
    ><button type="submit" className="buttonsubmit"><b>CLICK TO PLAY</b></button>
    </div>
    
  )
}

export default Game