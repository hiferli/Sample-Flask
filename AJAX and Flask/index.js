<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>


$(function () {
    window.setInterval(function () {
        newNumber()
    } , 1000)

    function newNumber () {
        $.ajax({
            type: "GET",
            url: "/update",
            dataType: "json",
            success: function (data) {
                $("#randomNumber").replaceWith(data)
            }
        });
    }
});