
function book(name){
    console.log(name.trimStart())
    console.log(name.trimEnd())
    console.log(name.trim())
}

let myfav = prompt()

book(myfav)

function startAndEnd(name2){
    if(name2.startsWith("ტ")){
        console.log( "idk")
    } else if(name2.endsWith("ე")){
        console.log("i said idk")
    } else{
        console.log("")
    }
    console.log(name2.toUpperCase())
    console.log(name2.toLowerCase())
}

function mathematics(name3){
    let bruh = Math.abs(name3.length - 20)
    console.log(bruh)
    console.log(Math.sqrt(bruh))
    console.log(Math.cbrt(bruh))
    console.log(Math.pow(bruh, 2))
    console.log(Math.round(bruh))
    console.log(Math.ceil(bruh))
    console.log(Math.floor(bruh))
    console.log(Math.min(bruh))
    console.log(Math.max(bruh))
}

