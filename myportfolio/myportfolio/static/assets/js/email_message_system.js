$(document).ready(function () {
    $("#contact-form").submit(function (e) {
        e.preventDefault(); // Prevent the default form submission

        var formData = $(this).serialize(); // Serialize form data
        var url = $(this).data('url');  // Retrieve the URL from the data attribute

        $.ajax({
            type: "POST",
            url: url,
            data: formData,
            success: function (response) {
                $("#message-container").html('<div class="alert alert-success">Email has been sent successfully.</div>');
            },
            error: function (xhr, textStatus, errorThrown) {
                $("#message-container").html('<div class="alert alert-danger">An error occurred while sending the Email. Please try again later.</div>');
            }
        });
    });
});
