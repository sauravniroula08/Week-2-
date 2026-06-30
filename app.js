const hamburger = document.querySelector("#hamburger")
const menu = document.querySelector("#menu")
const body = document.querySelector("body")
const hLinks = document.querySelectorAll("#hLink")

const bar1 = document.querySelector("#bar1")
const bar2 = document.querySelector("#bar2")
const bar3 = document.querySelector("#bar3")

function toggleMenu() {
  menu.classList.toggle("hidden")
  
  if (bar1 && bar2 && bar3) {
    bar1.classList.toggle("rotate-45")
    bar1.classList.toggle("translate-y-[6px]")
    bar2.classList.toggle("opacity-0")
    bar2.classList.toggle("scale-0")
    bar3.classList.toggle("-rotate-45")
    bar3.classList.toggle("-translate-y-[6px]")
  }
}

if (hamburger) {
  hamburger.addEventListener("click", toggleMenu)
}

hLinks.forEach(link=>{
  link.addEventListener("click", toggleMenu)
})