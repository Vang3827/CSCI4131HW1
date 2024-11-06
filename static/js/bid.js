document.addEventListener("DOMContentLoaded", () => {
    console.log("In bid.js script");

    const btn = document.getElementById("btnButton");
    const formInput = document.getElementById("bidInput")
    const name_input = document.getElementById("#nameinput")
    const amount_input = document.getElementById("#amount")
    const comments_input = document.getElementById("#comments")


    async function postapi(){
      
      let result = await fetch("/api/place_bid",{
        method: "POST",
        headers:{
          "Content-Type": "application/json"
        },
        body: JSON.stringify({name:name_input, amount:amount_input,comments:comments_input})
      });
      console.log(result)
    }

    formInput.style.display = "none";

    btn.addEventListener("click", () =>{
      if(formInput.style.display === "block"){
        formInput.style.display = "none";
      }else{
        formInput.style.display = "block";
      }
    })

    formInput.addEventListener("submit",(event)=>{
      event.preventDefault();
      postapi()
      // const inputData = new FormData(formInput);
      // const data = JSON.loads(inputData);

      // console.log(data);

    })
    
  });