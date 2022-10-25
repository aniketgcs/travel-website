// import * as mdb from 'mdb-ui-kit'; // lib
// import { Input } from 'mdb-ui-kit'; // module


let menu = document.querySelector("#menu-btn");
let navbarc = document.querySelector(".header .navbarc");

menu.onclick = () => {
  menu.classList.toggle("fa-times");
  navbarc.classList.toggle("active");
};

window.onscroll = () => {
  menu.classList.remove("fa-times");
  navbarc.classList.remove("active");
};

var swiper = new Swiper(".home-slider", {
  autoplay: {
    delay: 3000,
    disableOnInteracton: false,
  },
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

var swiper = new Swiper(".reviews-slider", {
  autoplay: {
    delay: 3000,
    disableOnInteracton: false,
  },
  grabCursor: true,
  loop: true,
  autoHeight: true,
  spaceBetween: 20,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    700: {
      slidesPerView: 2,
    },
    1000: {
      slidesPerView: 3,
    },
  },
});

// let loadMoreBtn = document.querySelector('.packages .load-more .btn');
// let currentItem = 3;

// loadMoreBtn.onclick = () =>{
//    let boxes = [...document.querySelectorAll('.packages .box-container .box')];
//    for (var i = currentItem; i < currentItem + 3; i++){
//       boxes[i].style.display = 'inline-block';
//    };

//    currentItem +=3;
//    if(currentItem >= boxes.length){
//       loadMoreBtn.style.display = 'none';
//    }
// }

// pagination of packages code starts

const cardItems = document.querySelector(".box-container").children;

// console.log(cardItems);
let next = document.querySelector(".next");
let page = document.querySelector(".page-num"); 
let prev = document.querySelector(".prev");



const maxItem = 6;
let index = 1;

const pagination = Math.ceil(cardItems.length / maxItem);
if(prev){
prev.addEventListener("click", function () {
  index--;
  check();
  showItems();
});
}

if(next){
next.addEventListener("click", function () {
  index++;
  check();
  showItems();
});
}

function check() {
  if (index == pagination) {
    next.classList.add("disabled");
  } else {
    next.classList.remove("disabled");
  }

  if (index == 1) {
    prev.classList.add("disabled");
  } else {
    prev.classList.remove("disabled");
  }
}

showItems = () => {
  for (let i = 0; i < cardItems.length; i++) {
    cardItems[i].classList.remove("show");
    cardItems[i].classList.add("hide");

    if (i >= index * maxItem - maxItem && i < index * maxItem) {
      cardItems[i].classList.remove("hide");
      cardItems[i].classList.add("show");
    }
    page.innerHTML=index;
  }
};

window.onload = function () {
  showItems();
  check();
};
