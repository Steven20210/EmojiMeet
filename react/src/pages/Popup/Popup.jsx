import React, { useState, useEffect } from 'react';
import Emoji from './Emoji.jsx';
import './Popup.css';

const Popup = () => {
  const [emotion, setEmotion] = useState('');

  const fetchEmotion = () => {
    fetch('http://127.0.0.1:5000/')
      .then((response) => response.json())
      .then((data) => setEmotion(data.mood));
  };

  useEffect(() => {
    setInterval(() => fetchEmotion(), 500);
  }, []);

  const emojiSelect = (emotion) => {
    switch (emotion) {
      case 'joy':
        return '😄';
      case 'sorrow':
        return '😢';
      case 'surprise':
        return '😲';
      case 'angry':
        return '😡';
      case 'unknown':
        return '😐';
      case 'underexposed':
        return '🙈';
      case 'hat':
        return '🤠';
      default:
        return '⏳';
    }
  };

  return (
    <div className="App">
      <Emoji emoji={emojiSelect(emotion)} />
    </div>
  );
};

export default Popup;
