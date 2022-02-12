// Declared constant variables
const contactForm = document.getElementById("contact-form");
const response = document.getElementById("response-text");
const responseHeader = document.getElementById("response-header");

// Submit event listener for contact form
contactForm.addEventListener("submit", sendForm);

// Function to send form
function sendForm(event) {
    event.preventDefault();
    let name = contactForm.name.value;
    let email = contactForm.email.value;
    let message = contactForm.message.value;

// Personalised response message displayed

    // response.innerHTML = `Thank-you ${name}!`;
    // responseHeader.innerHTML = `
    //     The message you sent is:
    //     "${message}" <br>
    //     We will get back to you as soon as possible
    //     via your email ${email}. <br>
    //     In the mean time, enjoy getting inspired and 
    //     getting cooking!</p>`;

// Display personalised modal
    $('#submit-modal').modal('open');

// Send contact information via emailJS
    return sendMail(this);

    function sendMail(contactForm) {
        emailjs.init("user_Qg0VvXz59G6JoT6Bdm3rf");
        emailjs.send("service_a66lyia","cookbook", {
            "from_name" : name,
            "from_email" : email,
            "message" : message
        })
        .then(
            function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("ERROR", error);
            }
        );

    }
}

