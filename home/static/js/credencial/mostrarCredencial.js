document.addEventListener("DOMContentLoaded", function () {
  btnRotate = document.getElementById("rotate-card");
  btnRotate.addEventListener("click", function () {
    credFront = document.querySelector(".contenedor_credenciales");
    credBack = document.querySelector(".credencial_reverso");
    if (!credFront.classList.contains("efecto_rotar")) {
        credBack.classList.remove("efecto_rotar")
        credFront.classList.add("efecto_rotar");
    } else {
        credBack.classList.add("efecto_rotar")
        credFront.classList.remove("efecto_rotar");
    }
    
  });
});
