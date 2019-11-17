$(document).ready(function() {
    var $myForm = $('.my-ajax-form');
    $myForm.submit(function(event) {
        event.preventDefault();
        var $formData = $myForm.serialize();
        var $thisURL = $myForm.attr('data-url') || window.location.href;
        $.ajax({
            method: 'POST',
            url: $thisURL,
            data: $formData,
            success: handleSuccess,
            error: handleError,
        });

        function handleSuccess(data) {
            var p1 = document.createElement("p");
            var p2 = document.createElement("p");
            var uq = document.createTextNode(data["message"]);
            var res = document.createTextNode(data["res"]);
            console.log(data.res)
            p1.appendChild(uq);
            p2.appendChild(res);
            var div = document.getElementById('messages');
            div.appendChild(p1);
            div.appendChild(p2);
            $myForm[0].reset()
        }

        function handleError(ThrowError) {
            console.log(ThrowError);
        }
    });
});



// function querySubmit() {
//     var inputValue = document.getElementById("userQuery").value;
//     if(inputValue != "") {
//         var divEl = document.createElement("div");
//         var messages = document.createTextNode(inputValue);
    
//         divEl.classList.add('mess');
//         divEl.appendChild(messages);

//         document.getElementById('messages').appendChild(divEl);
//         document.getElementById("userQuery").value = ""
//     }
    
//     // alert(inputValue)
// }