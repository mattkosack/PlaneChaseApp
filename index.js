let fileContents;
let oracleText = "";

function loadFile() {
    fetch('important_info.json')
        .then(response => response.text())
        .then(data => {
            fileContents = JSON.parse(data);
            console.log("File loaded successfully");
        })
        .catch(error => {
            console.error(error);
        });
}

function getRandomCard() {
    let keys = Object.keys(fileContents);
    let totalImages = keys.length;
    let randomIndex = Math.floor(Math.random() * totalImages);
    let path = fileContents[keys[randomIndex]].path;
    oracleText = fileContents[keys[randomIndex]].oracle_text;
    setOracleText(oracleText);
    return path;
}

function showImage() {
    let image = getRandomCard();
    document.getElementById('img').src = image;
}

function setOracleText(text) {
    document.getElementById('oracle-text').innerHTML = text;
}

function showOracleText() {
    var div = document.getElementById("oracle-text");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function rollDice() {
    var dice = document.getElementById("dice");
    var numbers = dice.getElementsByClassName("number");
    
    for (var i = 0; i < numbers.length; i++) {
        numbers[i].style.display = "none";
    }

    dice.classList.add("roll");

    setTimeout(() => {
        var randomIndex = Math.floor(Math.random() * numbers.length);
        numbers[randomIndex].style.display = "block";
    }, 1000);

    // setTimeout(() => {
    //     dice.classList.remove("roll");
    // }, 1500);
}
