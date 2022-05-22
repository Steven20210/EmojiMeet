import html2canvas from 'html2canvas';

const everything = () => {
  const video = document.querySelectorAll(`Gv1mTb-aTv5jf`)[1];
  html2canvas(video, {
    allowTaint: true,
    useCORS: true,
  })
    .then(function (canvas) {
      // It will return a canvas element
      let image = canvas.toDataURL('image/jpg', 0.5);
      fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: image }),
      }).then((res) => res.json());
    })
    .catch((e) => {
      // Handle errors
      console.log(e);
    });
};

setTimeout(() => {
  setInterval(() => everything(), 5000);
}, 5000);
