import React, { useEffect, useState } from 'react';

function Col({ rowindex, row, board, setBoard }) {
  const [selectedCell, setSelectedCell] = useState({ start: null, end: null });
 
 

   

    if (selectedCell.start && selectedCell.end) {
      console.log("sending moves")

      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      const raw = JSON.stringify({
        start_row: selectedCell.start.row,
        start_col: selectedCell.start.col,
        end_row: selectedCell.end.row,
        end_col: selectedCell.end.col,
        board:board
      });

      const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
      };

      fetch("http://127.0.0.1:5000/postmove", requestOptions)
        .then(response => response.json())
        .then(result => {
          // setBoard(result.board);
          console.log(result);
          setSelectedCell({ start: null, end: null });
        })
        .catch(error => console.error(error));
      }
   
  
 
 
  const handleCellClick = (colindex, rowindex) => {
    console.log('Cell clicked:', colindex, rowindex);

    if (!selectedCell.start) {
      setSelectedCell({ start: { row: rowindex, col: colindex } });
    } 
    
    else {
      setSelectedCell((prevSelectedCell) => ({
        ...prevSelectedCell,
        end: { row: rowindex, col: colindex },
      }));
    }
  };
  

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
            opacity:
              (selectedCell.start &&
                selectedCell.start.row === rowindex &&
                selectedCell.start.col === colindex) ||
              (selectedCell.end &&
                selectedCell.end.row === rowindex &&
                selectedCell.end.col === colindex)
                ? 0.7
                : 1,
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
