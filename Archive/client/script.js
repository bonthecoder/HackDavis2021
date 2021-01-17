function clicked(){
    console.log("hello");
    let userInput = document.getElementById('user-input').value;
    console.log('TYPED USER VALUE IS', userInput);
    // https://3e16c14010e1.ngrok.io
    // fetch('http://localhost:5000/app?input1=' + userInput).then(response => response.text()).then(parsedResponse => {
    //     console.log(parsedResponse);
    //     document.getElementById('display').innerText = parsedResponse;
    // })

    // fetch('http://localhost:5000').then(response => response.json()).then(parsedResponse => {
    //     console.log(parsedResponse);
    //     document.getElementById('display').innerText = parsedResponse[0].coolthing;
    // })

    fetch('http://localhost:5000/app?input1=1\ Week').then(response => response.text()).then(parsedResponse => {
        console.log(parsedResponse);
        document.getElementById('display').innerText = parsedResponse;
    })
}