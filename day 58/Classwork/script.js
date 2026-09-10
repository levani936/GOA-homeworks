const guestNumbers = [1, 7, 4, 5]
let firstName = prompt('Enter your name:') || "Guest"
let number = Math.floor(Math.random() * 10) + 1;
if(firstName) {
    console.log(`Hello ${firstName}`)
} else {
    if(number.includes(guestNumbers)) {
        console.log(firstName + guestNumbers)
    }
}
console.log(`Hello ${firstName}`)