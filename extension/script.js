document.getElementById("myButton").addEventListener("click", clicked);

function clicked(){
  let userInput = document.getElementById("myInput").value;
  // console.log('TYPED USER VALUE IS', userInput);
  // https://3e16c14010e1.ngrok.io
  fetch('http://localhost:5000/app?input1=' + userInput/* + 'input2=' + APIkey*/).then(response => response.json()).then(parsedResponse => {
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