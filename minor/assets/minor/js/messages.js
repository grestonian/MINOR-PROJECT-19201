function querySubmit() {
    var inputValue = document.getElementById("userQuery").value;
    if(inputValue != "") {
        var divEl = document.createElement("div");
        var messages = document.createTextNode(inputValue);
    
        divEl.classList.add('mess');
        divEl.appendChild(messages);

        document.getElementById('messages').appendChild(divEl);
        document.getElementById("userQuery").value = ""
    }
    
    // alert(inputValue)
}