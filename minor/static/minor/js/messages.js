$(document).ready(function() {
    var $myForm = $('.my-ajax-form');
    $myForm.submit(function(event) {
        event.preventDefault();

        var $formData = $myForm.serialize();
        var $thisURL = $myForm.attr('data-url') || window.location.href;

        var p1 = document.createElement("p");
        var user_query = document.createTextNode(jQuery('#id_name').val());
        p1.appendChild(user_query);
        var div = document.getElementById('messages');
        p1.classList.add('userQueryChat');
        div.appendChild(p1);
        $myForm[0].reset()

        $.ajax({
            method: 'POST',
            url: $thisURL,
            data: $formData,
            success: handleSuccess,
            error: handleError,
        });

        function handleSuccess(data) {
            var p2 = document.createElement("p");
            var chatbot_response = document.createTextNode(data["res"]);
            // console.log(data.res)
            
            p2.appendChild(chatbot_response);
            var div = document.getElementById('messages');
            p2.classList.add('ResponseChat');
            div.appendChild(p2);
            
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