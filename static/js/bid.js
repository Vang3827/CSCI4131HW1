document.addEventListener("DOMContentLoaded", () => {
    console.log("In JS script");

    let btn = document.getElementById("btnButton");
    let showhideForm = document.getElementById("bidInput")

    showhideForm.style.display = "none";

    btn.addEventListener("click", () =>{
      if(showhideForm.style.display === "block"){
        showhideForm.style.display = "none";
      }else{
        showhideForm.style.display = "block";
      }
    })

  });