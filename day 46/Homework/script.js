
let saxeli = "ნიკოლოზი";
console.log(saxeli);

saxeli = "გიორგი";
console.log(saxeli);


// String - ტექსტური მონაცემები ("გამარჯობა", "კარაქი")
// Number - რიცხვითი მონაცემები (10, 25, 3.14)
// Boolean - ლოგიკური მნიშვნელობები (true ან false)

// == ადარებს მხოლოდ მნიშვნელობებს და საჭიროების შემთხვევაში ცვლის ტიპებს
// მაგალითი:
console.log(5 == "5"); // true

// === ადარებს როგორც მნიშვნელობას, ასევე მონაცემთა ტიპს
// მაგალითი:
console.log(5 === "5"); // false


let dachi = "winner";
let levani = "";

if (levani === "winner") {
    console.log("ლევანმა მოიგო წყლის სმის ჩემპიონატში");
} else if (dachi === "winner") {
    console.log("დაჩიმ მოიგო წყლის სმის ჩემპიონატში");
} else {
    console.log("მეგობრობამ გაიმარჯვა");
}