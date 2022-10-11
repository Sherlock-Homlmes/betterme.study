const navBar = document.querySelector(".nav");
const navButton = document.querySelector(".nav-toggle");
let mousedown = false;

// Hamburger Navigation
function toggleNavigation() {
  if (navBar.classList.contains("is-open")) {
    this.setAttribute("aria-expanded", false);
    navBar.classList.remove("is-open");
  } else {
    navBar.classList.add("is-open");
    this.setAttribute("aria-expanded", true);
  }
}

// Counters

function counter(target, start, stop) {
  target.innerText = 0.1;
  const counterInterval = setInterval(() => {
    start += 0.1;
    const valueConverted = (Math.round(start * 100) / 100).toFixed(1);
    target.innerText = valueConverted;
    if (Number(valueConverted) >= Number(stop)) {
      clearInterval(counterInterval);
    }
  }, 30);
}

function obCallBack(entries) {
  entries.forEach((entry) => {
    const { target } = entry;
    const stopValue = target.innerText;
    const startValue = 0;
    if (!entry.isIntersecting) return;
    console.log(startValue, stopValue);
    counter(target, startValue, stopValue);
    counterObserver.unobserve(target);
  });
}

const counterObserver = new IntersectionObserver(obCallBack, { threshold: 1 });

// Event Listeners
navButton.addEventListener("click", toggleNavigation);