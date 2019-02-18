$(document).ready(function() {
    $("#regform").validate({
        rules: {
        	first_name: "required",
        	last_name: "required",
            email: {
                required: true,
                email: true
            },
            phone: {
                required: true,
                number: true
            },
            agree: "required"
        },
        messages: {
            first_name: "Please enter your first name",
            last_name: "Please enter your last name",
            email: "Please enter a valid email address",
            phone: {
                required: "Please enter your phone number",
                number: "Please enter only numeric value"
            },
            agree: "Please accept our policy"
        }
    });
});
