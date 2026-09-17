function sayHello() {
    console.log("გამარჯობა, კეთილი იყოს შენი მობრძანება JS ში")
}

function addNumbers(number1, number2) {
    return number1 + number2
}
console.log(addNumbers(6, 7))

function isEven(number) {
    if (number % 2 === 0) {
        return true;
    } else {
        return false;
    }
}
function square(number) {
    number * number
}

function getFullName(firstName, lastName) {
    return firstName + " " + lastName
}
console.log(getFullName("გიორგი", "ბერიძე"))
