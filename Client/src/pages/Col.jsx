import React, { useState, useEffect } from 'react';

function Col({ rowindex, row }) {
  const [selectedCell, setSelectedCell] = useState([]);
  const [clickcount, setClickCount] = useState(0);

  const handleCellClick = (colindex, rowindex) => {
    setClickCount(prev => prev + 1);
    setSelectedCell(prev => [...prev, rowindex, colindex]);
  };

  useEffect(() => {
    if (clickcount === 2) {
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      const raw = JSON.stringify({
        "start_row": selectedCell[0],
        "start_col": selectedCell[1],
        "end_row": selectedCell[2],
        "end_col": selectedCell[3]
      });

      const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
      };

      fetch("http://127.0.0.1:5000/game", requestOptions)
        .then(response => response.text())
        .then((result)=>{
          setClickCount(0);
          setSelectedCell([])
          console.log(result)})
        .catch(error => console.error(error));

      
    }
  }, [clickcount, selectedCell]);

  return (
    <div style={{ display: 'flex', flexDirection: 'row' }}>
      {row.map((cell, colindex) => (
        <div
          key={colindex}
          className="cell"
          style={{
            width: '50px',
            height: '50px',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            border: '1px solid black',
            background:
              rowindex % 2 === 0
                ? colindex % 2 === 0
                  ? '#f0f0f0'
                  : 'brown'
                : colindex % 2 === 1
                ? '#f0f0f0'
                : 'brown',
            cursor: 'pointer',
            opacity: selectedCell.includes(rowindex) && selectedCell.includes(colindex) ? 0.7 : 1, 
          }}
          onClick={() => handleCellClick(colindex, rowindex)} 
        >
          {cell}
        </div>
      ))}
    </div>
  );
}

export default Col;
