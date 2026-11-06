let text = prompt("შეიყვანეთ თქვენი საყვარელი ბიბლიოთეკის ან ავტორის სახელი:");

text = text.trim().replace(/\s+/g, " ");

let length = text.length;

let hasLetters = /[a-zA-Zა-ჰ]/.test(text);

let endsCorrectly = /[.!]$/.test(text);

text = text[0].toUpperCase() + text.substring(1).toLowerCase();

let remainder = (length + 10) % 3;

let cube = length ** 3;

let decimal = length / 3;

let rounded = Math.round(decimal);
let roundedUp = Math.ceil(decimal);
let roundedDown = Math.floor(decimal);

let pages = [145, 89, 320, 210, 450];

let min = Math.min(...pages);
let max = Math.max(...pages);

console.log("დამუშავებული ტექსტი:", text);
console.log("სიმბოლოების რაოდენობა:", length);
console.log("შეიცავს ასოებს:", hasLetters);
console.log("მთავრდება წერტილით ან ძახილის ნიშნით:", endsCorrectly);
console.log("ნაშთი:", remainder);
console.log("მე-3 ხარისხი:", cube);
console.log("ათწილადი:", decimal);
console.log("Math.round:", rounded);
console.log("Math.ceil:", roundedUp);
console.log("Math.floor:", roundedDown);
console.log("მინიმალური გვერდები:", min);
console.log("მაქსიმალური გვერდები:", max);