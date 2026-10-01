function buyLaptop(name=`Guest ${Math.floor(Math.random() * 1001)}`){
    return `${name} გილოცავთ ახალ შენაძენს.`
}
console.log(buyLaptop())

prompt(name, age)
function nameAndAge(name, age=0){
    age = (age < 18) ? "Bye": "Welcome";
}

prompt(name1, score)
function nameAndGrade(name1, score=0){
    if (score < 50){
        return 'Fail'
    } else{
        return "Pass"
    }
}
