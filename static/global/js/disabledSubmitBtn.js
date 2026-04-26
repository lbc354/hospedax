// EMPTY FORM (CREATE, SIGN UP, SIGN IN)

// TYPE 1
const form = document.getElementById("submitForm");
const submitBtn = document.getElementById("submitBtn");

function checkForm() {
    submitBtn.disabled = !form.checkValidity();
}

form.addEventListener("input", checkForm);
checkForm();

// TYPE 2
// const form = document.getElementById("submitForm");
// const submitBtn = document.getElementById("submitBtn");
// const requiredFields = form.querySelectorAll("[required]");

// function checkForm() {
//     let allFilled = true;

//     requiredFields.forEach(field => {
//         if (!field.value.trim()) {
//             allFilled = false;
//         }
//     });

//     submitBtn.disabled = !allFilled;
// }

// // Escuta mudanças em todos os campos
// requiredFields.forEach(field => {
//     field.addEventListener("input", checkForm);
// });

// // roda uma vez ao carregar
// checkForm();