import React from 'react';

const Emoji = ({ emoji }) => {
  const loading = emoji == '⏳';
  return (
    <div className="container">
      <p className="text">
        {loading ? 'Loading...' : 'The person you are talking to is feeling'}
      </p>

      <div className={loading ? 'loading' : 'emoji'}>{emoji}</div>
    </div>
  );
};
//do you ever feel like someone is secretly upset even though they sound happy? this emotion detector will tell you how
//the person you're talking to is feeling
export default Emoji;
