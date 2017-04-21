// The following prototype is defined to store drawing information.
function Drawing(tag, count)
{
    this.tag=tag;
    this.count=count;
}
drawings=[]

function createCloud()
{
    $('#tc').empty();
    document.getElementById("loader1").style.display = "block";

    var searchInput = document.getElementById("StockTicker").value;
    if (searchInput != ""){
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function()
        {
            if (xhttp.readyState == 4 && xhttp.status == 200)
            {
                var data = xhttp.responseText;
                var drawingStrings = data.split(";");
                drawings=[]
                for(var i=0;i<drawingStrings.length;i++)
                {

                    var drawingString = drawingStrings[i];
                    if (drawingString == "") {
                        continue;
                    }
                    var attributeStrings = drawingString.split(",");
                    var newDrawing = new Drawing(attributeStrings[0], attributeStrings[1]);
                    drawings.push(newDrawing);

                }
                appendToList()
                
            }
        }
        xhttp.open("GET", "/getIndex/"+"?index="+searchInput, false);
        xhttp.send();
        document.getElementById("loader1").style.display = "none";
    }

}

function appendToList()
{  


    for(var i=0; i<drawings.length; i++){
        var li = document.createElement('li');
        li.className= 'tag1'
        var aTag = document.createElement('a');
        aTag.innerHTML = drawings[i].tag;
        li.appendChild(aTag);
        li.style.fontSize = drawings[i].count+"px";
        var tc = document.getElementById("tc")
        tc.appendChild(li)

    }
}

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}





