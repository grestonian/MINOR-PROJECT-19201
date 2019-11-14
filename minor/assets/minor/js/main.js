var btn = document.getElementById("button");
btn.onclick = function() {myFunction()};

function myFunction() {

  const main = document.querySelector('.main');
  const logo = document.querySelector('.logo');
  const line = document.querySelector('.line');
  const motto = document.querySelector('.motto');
  const chtbt = document.querySelector('.chatbox');

  main.classList.toggle('main-tog');
  line.classList.toggle('line-tog');
  motto.classList.toggle('motto-tog');
  logo.classList.toggle('logo-tog');
  chtbt.classList.toggle('chatbox-togg')
  


  if(btn.innerText === "Begin") {
    btn.innerHTML = "<span>Go Back</span>";
    btn.style.marginLeft = '0%'
    btn.style.marginTop = '15%'
    btn.style.transform = 'scale3d(0.5, 0.8, 1)'
  }
  else {
    btn.innerHTML = "<span>Begin</span>";
    btn.style.marginLeft = '40%'
    btn.style.marginTop = '0%'
    btn.style.transform = 'scale3d(1, 1, 1)'
  }
    

}