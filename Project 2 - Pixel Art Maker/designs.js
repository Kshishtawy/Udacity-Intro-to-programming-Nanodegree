// Select color input
// Select size input
document.getElementById('sizePickerr').addEventListener('click', function(e) {  // to prevent the page from being refreshed when submit button is pressed
    e.preventDefault();
})
var table = document.getElementById('pixelCanvas'); 
var height = document.getElementById('inputHeight'); 
var width = document.getElementById('inputWidth');


// When size is submitted by the user, call makeGrid()

document.getElementById('sizePickerr').addEventListener('click', function makeGrid() { // when submit is pressed call makeGrid()
    if (typeof table.childElementCount !== "undefined") { // to check if there is already made grid (if table has children). 
        for (var e = 0; e = table.childElementCount;) {// if table has children, a for loop will be active to remove all the children
            table.children[0].remove()
        }
    };
    for (let i = 0; i < Number(height.value); i++) {// the value written for height determines how many rows will be generated in the table
        var newRow = document.createElement('tr') // creates rows 
        table.appendChild(newRow) // appends the rows to the table
    };
    for (let k = 0; k < table.childElementCount; k++) { // a loop for every time the table got a row (children till now)
        for (let j = 0; j < Number(width.value); j++) { // an increasing loop to determain the width or (how many boxs,squares, or table data) will be in each row
            var newBox = document.createElement('td') // creates a new square (box or table data)
            var c = table.children // the variable (c) contains the rows. as rows are the only children in the table till now
            c[k].append(newBox) // the variable (j) will append a new square for a row , as variable k walk along the children of table which are rows, and variable (j) loops inside each row to append a number of squares depends on the (width.value)
        } // the code above looks in the array of the table children which are rows until creating the table data, and each row get the number of squares depending on the loop with the variable (j), as (j) loops for the value of the width
    };
    var w = table.getElementsByTagName('td'); // putting all the squares (td) inside a variable called w 
    var colorPicker = document.getElementById('colorPicker'); // putting the color picker in a variable
    for (let x = 0; x < w.length; x++) { // a loop the runs through all squares that has been made 
        w[x].addEventListener('click', function() {  
            w[x].style.backgroundColor = colorPicker.value // an event listener will be added for every sqaure so that any click on any square will turn the background of this square into the value (color) of the color picker 
        })
    }




    // Your code goes here!

})