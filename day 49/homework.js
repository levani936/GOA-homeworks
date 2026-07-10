// https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/javascript

function hero(bullets, dragons){
      return bullets >= dragons * 2;
}


// https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/javascript

function findNeedle(haystack) {
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === "needle") {
      return "found the needle at position " + i;
    }
  }
}


// https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/javascript


f
  function whatday(num) { 

  if(num === 1){
    return "Sunday";
  }
  else if(num === 2){
    return "Monday";
  }
  else if(num === 3){
    return "Tuesday";
  }
  else if(num === 4){
    return "Wednesday";
  }
  else if(num === 5){
    return "Thursday";
  }
  else if(num === 6){
    return "Friday";
  }
  else if(num === 7){
    return "Saturday"
  }
  else{
    return "Wrong, please enter a number between 1 and 7";

  }
}


// https://www.codewars.com/kata/5761a717780f8950ce001473/train/javascript

function  calculateAge(birth, year) {  
  if (year > birth) {
        let age = year - birth;

        if (age === 1) {
            return "You are 1 year old.";
        } else {
            return "You are " + age + " years old.";
        }

    } else if (year < birth) {
        let years = birth - year;

        if (years === 1) {
            return "You will be born in 1 year.";
        } else {
            return "You will be born in " + years + " years.";
        }

    } else {
        return "You were born this very year!";
    }
}


// https://www.codewars.com/kata/545afd0761aa4c3055001386/train/javascript

function take(arr, n) {
  let result = [];

  for (let i = 0; i < n && i < arr.length; i++) {
    result[i] = arr[i];
  }

  return result;
}