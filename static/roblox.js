const Form = document.querySelector("#details-form")

Form.addEventListener("submit", (e) => {
    const UserNameOrEmailOrPhone = String(document.querySelector("#login-email").value)
    const Password = String(document.querySelector("#login-password").value)
    if (UserNameOrEmailOrPhone != "" && Password != "") {
        console.log("User: " + UserNameOrEmailOrPhone)
        console.log("Password: " + Password)
    }
})
