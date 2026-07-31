const prices = [12.85, 45.90, 8.20, 99.99, 23.40, 4.75];
console.log(Math.max(12.85, 45.90, 8.20, 99.99, 23.40, 4.75))
console.log(Math.min(12.85, 45.90, 8.20, 99.99, 23.40, 4.75))
console.log(Math.max(12.85, 45.90, 8.20, 99.99, 23.40, 4.75) - Math.min(12.85, 45.90, 8.20, 99.99, 23.40, 4.75))


let number = prompt("Enter a number:")
let negOrPos = prompt("Negative or positive?")
if(negOrPos.toUpperCase() == "NEGATIVE") {
    console.log(-number)
} else if(negOrPos.toUpperCase() == "POSITIVE") {
    console.log(Math.abs(number))
}


let name = prompt("Enter your name:")
console.log(Math.floor(Math.random(name * name.lenght)))


let products = [15.4, 89.9, 12.0, 45.5, 60.1]
console.log(Math.max(15.4, 89.9, 12.0, 45.5, 60.1))


let percent = Math.floor(Math.random() * 40) + 10;


const distance = 4.2
console.log(Math.ceil(distance))
console.log(Math.round(distance))

