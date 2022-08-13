let fetch = document.getElementById("fetchButton");
fetch.addEventListener("click" , buttonClickHandler);

function buttonClickHandler() {
    console.log("Welcomd Here");

    const xhr = new XMLHttpRequest();

    xhr.open("POST" , "	https://dummy.restapiexample.com/api/v1/create" , true);
    xhr.getResponseHeader("Content-type" , "application/json")

    xhr.onprogress = function () {
        console.log("On Progress")
    }

    // xhr.onreadystatechange = function () {
    //     console.log("State Change Code: " + (xhr.readyState))
    // }

    xhr.onload = function () {
        if(this.status === 200){
            console.log(this.responseText);
        } else {
            console.error("Some Error");
        }
    }

    parameters_json = {"name":"testSample","salary":"123","age":"23"};
    xhr.send(parameters_json);
}

let data = document.getElementById("dataButton");
data.addEventListener("click" , addEmployees);

function addEmployees() {
    console.log("Welcomd Here");

    const xhr = new XMLHttpRequest();

    xhr.open("GET" , "https://dummy.restapiexample.com/api/v1/employees" , true);
    xhr.getResponseHeader("Content-type" , "application/json")

    xhr.onload = function () {
        if(this.status === 200){
            let object = JSON.parse(this.responseText);
            // console.log(object);

            let list = document.getElementById("list");

            for(key in object.data){
                console.log(object.data[key].employee_name);
                list.innerHTML += `<li>${object.data[key].employee_name}</l1>`;
            }
        } else {
            console.error("Some Error");
        }
    }

    xhr.send();
}
