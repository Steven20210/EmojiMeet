import html2canvas from 'html2canvas';

const everything = () => {
  const video = document.querySelector(`.p2hjYe`);
  console.log('sup');
  html2canvas(video, {
    allowTaint: true,
    useCORS: true,
  })
    .then(function (canvas) {
      // It will return a canvas element
      let image = canvas.toDataURL('image/png', 0.5);
      console.log(image);
      fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: image }),
      })
        .then((res) => res.json())
        .then((json) => {
          mood = json.mood;
          console.log(mood);
        });
    })
    .catch((e) => {
      // Handle errors
      console.log(e);
    });
};

setTimeout(() => {
  setInterval(() => everything(), 1000);
}, 5000);
