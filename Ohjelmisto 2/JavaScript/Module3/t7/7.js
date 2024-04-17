//Open t7 folder in your IDE/editor. Make a hover effect with JavaScript. (2p)
// when user mouses over <p id="trigger"> change the picture of
// <img id="target"> form picA.jpg to picB.jpg
// when user mouses off, change the picture back to original

'use script';

function changePictureB() {
  document.getElementById('target').src = 'img/picB.jpg';
}
function changePictureA() {
  document.getElementById('target').src = 'img/picA.jpg';
}

document.getElementById('trigger').addEventListener('mouseover', changePictureB);
document.getElementById('trigger').addEventListener('mouseout', changePictureA);
