let speed = 293
speed = 100

let age = 13
console.log(Math.cbrt(age))

let age2 = 13
if (age2 < 18){
    return "თქვენ არ ხართ სრულწლოვანი"
} else if (age2 >= 18){
    return "თქვენ სრულწლოვანი ხართ"
}

// https://www.codewars.com/kata/582cb0224e56e068d800003c/train/javascript

function litres(time) {
  return Math.floor(time * 0.5)
}


//  https://www.codewars.com/kata/5861d28f124b35723e00005e/train/javascript

const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  return fuelLeft * mpg >= distanceToPump
};