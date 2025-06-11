

const myObserver = new IntersectionObserver((info) => {
    info.forEach((infoo) => {
        if(infoo.isIntersecting){
            infoo.target.classList.add('show')
        }else{
            infoo.target.classList.remove('show')
        }
    })
})

const elemento = document.querySelectorAll('.caixa')

elemento.forEach((elemento) => myObserver.observe(elemento))

const elemento2 = document.querySelectorAll('.caixa2')

elemento2.forEach((element) => myObserver.observe(element))

const elemento3 = document.querySelectorAll('.caixa3')

elemento3.forEach((element) => myObserver.observe(element))


window.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('.fade-in');
  items.forEach((el, i) => {
    setTimeout(() => {
      el.classList.add('show');
    }, i * 150); // atraso em cascata
  });
});

//Código para mostrar senha
const pwShow = document.querySelector(".show");
createPw = document.querySelector("#createPw");
confirmPw = document.querySelector("#confirmPw");
alertIcon = document.querySelector(".errorIcon");
alerttext = document.querySelector(".text");
submitBtn = document.querySelector("#button");

pwShow.addEventListener("click", () => {
    if((createPw.type === "password") && (confirmPw.type === "password")){
        createPw.type = "text";
        confirmPw.type = "text";
        pwShow.classList.replace("bxs-eye-slash", "bxs-eye");
    }else{
        createPw.type = "password";
        confirmPw.type = "password";
        pwShow.classList.replace("bxs-eye", "bxs-eye-slash");
    }
});

//Codigo para confirmar senha

createPw.addEventListener("input", ()=> {
   let inputValue = createPw.value.trim();

    if(inputValue.length >= 8){
        confirmPw.removeAttribute("disabled");
        submitBtn.removeAttribute("disabled");
        submitBtn.classList.add("active");

    }else{
        confirmPw.setAttibute("disabled", true);
        submitBtn.setAttibute("disabled", true);
        submitBtn.classList.remove("active");
        confirmPw.value = "";
        alerttext.innerText = "Digite pelo menos 8 caracteres";
        alerttext.style.color = "#a6a6a6";
        alertIcon.style.display = "none";
    }
});

submitBtn.addEventListener("click", () => {
    if(createPw.value === confirmPw.value){
     alerttext.innerText = "Senha aceita";
     alertIcon.style.display = "none";
     alerttext.style.color = "#4070F4"

    } else{
        alerttext.innerText = "Senha não aceita";
        alerttext.style.color = "#D93025"
        alertIcon.style.display = "block";
        
     }
});




