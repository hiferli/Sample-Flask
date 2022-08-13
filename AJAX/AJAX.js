let fetch = document.getElementById("fetchButton");

fetch.addEventListener("click" , buttonClickHandler);

function buttonClickHandler() {
    console.log("Welcomd Here");

    const xhr = new XMLHttpRequest();

    xhr.open("GET" , "Ishaan.txt" , true);

    xhr.onprogress = function () {
        console.log("On Progress")
    }

    xhr.onreadystatechange = function () {
        console.log("State Change Code: " + (xhr.readyState))
    }

    xhr.onload = function () {
        if(this.status === 200){
            console.log(this.responseText);
        } else {
            console.error("Some Error");
        }
    }

    xhr.send();
}