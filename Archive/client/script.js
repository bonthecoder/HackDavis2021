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

    fetch('http://localhost:5000/app?input1=1\ Week').then(response => response.json()).then(parsedResponse => {
        // console.log(parsedResponse);
        // var length = parsedResponse["metadata"]["size"];
        assList = makeList(parsedResponse);
        populateTable(assList);
    })
}

// Make list of jsons
function makeList(json) {
    var arr = [];
    for (ass in json) {
        arr.push(json[ass]);
        console.log(json[ass]);
    }
    return arr;
}

// Make a table of assignments
function populateTable(json) {
    var obj = json;
    var table = $("<table />");
    table[0].border = "1";
    var columns = Object.keys(obj[0]);
    var columnCount = columns.length;
    var row = $(table[0].insertRow(-1));

    for (var i = 0; i < columnCount; i++) {
        var headerCell = $("<th />");
        headerCell.html([columns[i]]);
        row.append(headerCell);
    }

    for (var i = 0; i < obj.length; i++) {
        row = $(table[0].insertRow(-1));
        for (var j = 0; j < columnCount; j++) {
            var cell = $("<td />");
            cell.html(obj[i][columns[j]]);
            row.append(cell);
        }
    }
    
    var dvTable = $("#dvCSV");
    dvTable.html("");
    dvTable.append(table);
}