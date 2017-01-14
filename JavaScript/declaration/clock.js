var days = 60;

while (days >= 0){
    if(days >= 30){
    console.log("There's " + days + " days till my birthday. Still so long..");
    }
    else if(days >= 5){
        console.log("There's " + days + " days till my birthday. It's less than a month now!")
    }
    else if(days > 0){
        console.log("There's " + days + " days till my birthday! SOON I SHALL RULE THE WORLD!")
    }
    else if(days === 0){
        console.log("IT'S MY BIRTHDAY!")
    }
    days--;
}
