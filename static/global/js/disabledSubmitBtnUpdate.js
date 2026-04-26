// FORM WITH DATA (UPDATE)

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("submitFormUpdate");
    const submitBtn = document.getElementById("submitBtnUpdate");

    const fields = form.querySelectorAll(
        "input:not([name='csrfmiddlewaretoken']), textarea, select"
    );

    const initialState = Array.from(fields).map(field => {
        if (field.type === "checkbox" || field.type === "radio") {
            return field.checked;
        }
        return field.value;
    });

    function isDirty() {
        return Array.from(fields).some((field, index) => {
            const current = field.type === "checkbox" || field.type === "radio"
                ? field.checked
                : field.value;
            return current !== initialState[index];
        });
    }

    function checkForm() {
        const dirty = isDirty();
        const valid = form.checkValidity();

        submitBtn.disabled = !(dirty && valid);
    }

    form.addEventListener("input", checkForm);
    form.addEventListener("change", checkForm);

    checkForm();
});