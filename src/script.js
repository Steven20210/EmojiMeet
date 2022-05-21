const ff = (video) => {
  if (typeof video != "undefined") {
    console.log("yes");
  }
  console.log("hmmm");
};
setTimeout(() => {
  const video = document.querySelector(`.p2hjYe`);
  video.addEventListener("mouseover", () => console.log("hi"));
  ff(video);
}, 7000);
