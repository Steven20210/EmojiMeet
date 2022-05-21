import React, { useState, useEffect } from 'react';
import Emoji from './Emoji.jsx';
import './Popup.css';

const Popup = () => {
  const [emotion, setEmotion] = useState('');

  const fetchEmotion = () => {
    fetch('http://127.0.0.1:5000/')
      .then((response) => response.json())
      .then((data) => setEmotion(data));
  };

  const emojiSelect = (emotion) => {
    switch (emotion) {
      case 'happy':
        return '😄';
      case 'sad':
        return '😢';
      case 'surprise':
        return '😲';
      case 'angry':
        return '😡';
      case 'underexposed':
        return '🙈';
      case 'hat':
        return '🤠';
      default:
        return '⏳';
    }
  };
  const rr = () => {
    setEmotion('angry');
  };
  // useEffect(() => {
  //   fetchEmotion();
  // }, [emotion]);

  return (
    <div className="App" onClick={rr}>
      <Emoji emoji={emojiSelect(emotion)} />
    </div>
  );
};

export default Popup;
