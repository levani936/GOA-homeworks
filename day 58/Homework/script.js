// https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/javascript

function hoopCount (n){
  if(n > 9){
return "Great, now move on to tricks";
  }else{
    return "Keep at it until you get it"
  }
  }


//  https://www.codewars.com/kata/56dec885c54a926dcd001095/train/javascript

function opposite(number) {
  return -number
}


// https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/javascript

function evenOrOdd(number) {
  if (number % 2 === 0) {
    return "Even";
  } else {
    return "Odd";
  }
}


// https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/javascript

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


// https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145/train/javascript

function hoopCount (n){
  if(n > 9){
return "Great, now move on to tricks";
  }else{
    return "Keep at it until you get it"
  }
}


// https://www.codewars.com/kata/56dec885c54a926dcd001095/train/javascript

function opposite(number) {
  return -number
}


// https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/javascript 

function evenOrOdd(number) {
  if (number % 2 === 0) {
    return "Even";
  } else {
    return "Odd";
  }
}


// https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/javascript

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