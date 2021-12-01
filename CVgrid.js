function printMyName(){
    console.log("Gal Biton");
}

function myFunction() {
    const inpObj = document.getElementById("name");
    if (!inpObj.checkValidity()) {
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    }

     const inpObj2 = document.getElementById("lname");
    if (!inpObj2.checkValidity()) {
        document.getElementById("demo2").innerHTML = inpObj2.validationMessage;
    } else {
        document.getElementById("demo2").innerHTML = "Input OK";
    }

    const inpObj3 = document.getElementById("subject");
    if (!inpObj3.checkValidity()) {
        document.getElementById("demo3").innerHTML = inpObj3.validationMessage;
    } else {
        document.getElementById("demo3").innerHTML = "Input OK";
    }

}