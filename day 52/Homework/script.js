// 1) https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/javascript\

function findNextSquare(sq) {
  let root = Math.sqrt(sq);

  if (root % 1 !== 0) {
    return -1;
  }

  return (root + 1) ** 2;
}


// 2) https://www.codewars.com/kata/5641a03210e973055a00000d/train/javascript

function twoDecimalPlaces(n) {
   return Math.round(n * 100) / 100;
}


// 3) https://www.codewars.com/kata/554b4ac871d6813a03000035/train/javascript

function highAndLow(numbers){
  let arr = numbers.split(" ");

  let max = Number(arr[0]);
  let min = Number(arr[0]);

  for (let i = 1; i < arr.length; i++) {
    let num = Number(arr[i]);

    if (num > max) {
      max = num;
    }

    if (num < min) {
      min = num;
    }
  }

  return max + " " + min;
}


// 4) https://www.codewars.com/kata/582cb0224e56e068d800003c/train/javascript

function litres(time) {
  return Math.floor(time * 0.5)
}


// 5) https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/javascript

function century(year) {
  if (year % 100 === 0) {
    return year / 100;
  }

  return Math.floor(year / 100) + 1;
}