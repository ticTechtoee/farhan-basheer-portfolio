
    $(document).ready(function () {
        $("#contact-form").submit(function (e) {
            e.preventDefault(); // Prevent the default form submission

            var formData = $(this).serialize(); // Serialize form data

            $.ajax({
                type: "POST",
                url: "{% url 'home:ViewHome' %}",  // Replace 'home' with the actual URL of your Django view
                data: formData,
                success: function (response) {
                    $("#message-container").html('<div class="alert alert-success">Form submitted successfully.</div>');
                },
                error: function (xhr, textStatus, errorThrown) {
                    $("#message-container").html('<div class="alert alert-danger">An error occurred. Please try again later.</div>');
                }
            });
        });
    });

