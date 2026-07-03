//  https://www.codewars.com/kata/5761a717780f8950ce001473/train/javascript

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


// https://www.codewars.com/kata/55a70521798b14d4750000a4/train/javascript

function greet(name){
  return `Hello, ${name} how are you doing today?`;
}


// https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/javascript

String.prototype.isUpperCase = function() {
  return this == this.toUpperCase();
}


// https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/javascript

class Kata {
  static getVolumeOfCuboid(length, width, height) {
    return length * width * height;
  }
}


// https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/javascript

function finalGrade (exam, projects) {
  if (exam > 90 || projects > 10) {
    return 100;
  } else if (exam > 75 && projects >= 5) {
    return 90;
  } else if (exam > 50 && projects >= 2) {
    return 75;
  } else {
    return 0;
  }
}