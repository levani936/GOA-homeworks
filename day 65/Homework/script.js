// მოცემულია prices მასივი, რომელშიც შენახულია პროდუქტების ფასები.
const prices = [15,72,45,73,85,16,82,54,100,250]

// ეს ფუნქცია ფასებს 15%-ით აკლებს.
function discount(pricesArr){
    // ვქმნით ცარიელ მასივს, რომელშიც ფასდაკლებული ფასები ჩაიწერება.
    const discountedPrices = []

    // for ციკლი მასივის ყველა ელემენტს სათითაოდ გადაუვლის.
    for(let i = 0; i < pricesArr.length; i++){
        // ფასს ვამრავლებთ 0.85-ზე, რათა 15%-იანი ფასდაკლება მივიღოთ.
        // Math.trunc() ათწილადის ნაწილს შლის, ხოლო push() შედეგს მასივში ამატებს.
        discountedPrices.push(Math.trunc(pricesArr[i] * 0.85))
    }

    // ვაბრუნებთ ფასდაკლებული ფასების მასივს.
    return discountedPrices;
}

// ეს ფუნქცია ფასებს 30%-ით ზრდის.
function increasePrice(pricesArr){
    // ვქმნით ცარიელ მასივს გაზრდილი ფასების შესანახად.
    const increasedPrices = []

    // ციკლი ყველა ფასს სათითაოდ ამოწმებს.
    for(let i = 0; i < pricesArr.length; i++){
        // ფასს ვამრავლებთ 1.3-ზე, რაც მის 30%-ით გაზრდას ნიშნავს.
        // Math.trunc() ათწილადის ნაწილს შლის, push() კი შედეგს მასივში ამატებს.
        increasedPrices.push(Math.trunc(pricesArr[i] * 1.3))
    }

    // ვაბრუნებთ გაზრდილი ფასების მასივს.
    return increasedPrices;
}

// ეს ფუნქცია ყველა ფასს აორმაგებს.
function doublePrices(pricesArr){
    // ვქმნით ცარიელ მასივს გაორმაგებული ფასების შესანახად.
    const doubledPrices = []

    // ციკლი მასივის ყველა ელემენტს გადაუვლის.
    for(let i = 0; i < pricesArr.length; i++){
        // თითოეულ ფასს ვამრავლებთ 2-ზე და შედეგს ახალ მასივში ვამატებთ.
        doubledPrices.push(pricesArr[i] * 2)
    }

    // ვაბრუნებთ გაორმაგებული ფასების მასივს.
    return doubledPrices;
}

// ეს ფუნქცია არჩევს იმ ელემენტებს, რომელთა ინდექსებიც ლუწია.
function evenProducts(pricesArr){
    // ვქმნით ცარიელ მასივს ლუწი ინდექსების მქონე ელემენტების შესანახად.
    const evenElements = []

    // ციკლი მასივის ყველა ინდექსს სათითაოდ ამოწმებს.
    for(let i = 0; i < pricesArr.length; i++){
        // % არის ნაშთის ოპერატორი.
        // თუ ინდექსი 2-ზე გაყოფისას ნაშთს არ ტოვებს, ის ლუწია.
        if(i % 2 == 0){
            // ლუწი ინდექსის მქონე ელემენტი ახალ მასივში ემატება.
            evenElements.push(pricesArr[i])
        }
    }

    // ვაბრუნებთ ლუწი ინდექსების მქონე ელემენტების მასივს.
    return evenElements;
}

// მთავარი ფუნქცია, რომელიც ყველა ფუნქციის შედეგს ერთ ტექსტში აერთიანებს.
function renderPrices(pricesArr) {
    // backtick-ები (`) საშუალებას გვაძლევს, ტექსტში ცვლადები და ფუნქციების შედეგები ჩავსვათ.
    // ${} გამოიყენება ცვლადის მნიშვნელობის ან ფუნქციის შედეგის ტექსტში გამოსატანად.
    return `
    Original Prices: ${pricesArr}
    15% Discount: ${discount(pricesArr)}
    30% Increase: ${increasePrice(pricesArr)}
    2X Prices: ${doublePrices(pricesArr)}
    Even Elements: ${evenProducts(pricesArr)}
    `
}

// ვიძახებთ მთავარ ფუნქციას და console.log()-ის საშუალებით მის შედეგს კონსოლში გამოვიტანთ.
console.log(renderPrices(prices))