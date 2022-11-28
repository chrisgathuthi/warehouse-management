const loginForm = document.getElementById("login-form")
const baseEndpoint = "http://127.0.0.1:8000/api"
if (loginForm){
    // handle login form 
    loginForm.addEventListener("submit",handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const LoginEndpont = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    
    let loginObjecData = Object.fromEntries(loginFormData)
    let bodystr = JSON.stringify(loginObjecData)
    console.log(bodystr)
    const optons = {
        method : "POST",
        headers: {
            "content-type": "application/json"
        },
        body: bodystr
    }
    fetch(LoginEndpont,optons)
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(x =>{
        console.log(x)
    })
    .catch(err=>{
        console.log(err)
    })
    
}