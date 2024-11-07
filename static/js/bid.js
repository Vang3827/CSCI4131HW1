document.addEventListener("DOMContentLoaded", () => {
    console.log("In bid.js script");

    const btn = document.getElementById("btnButton");
    const formInput = document.getElementById("bidInput")
    const name_input = document.getElementById("nameinput")
    const amount_input = document.getElementById("amount")
    const comments_input = document.getElementById("comments")


    // async function postapi(){
      
    //   let result = await fetch("/api/place_bid",{
    //     method: "POST",
    //     headers:{
    //       "Content-Type": "application/json"
    //     },
    //     body: JSON.stringify({name:name_input, amount:amount_input,comments:comments_input})
    //   });
    //   console.log(result)
    //   return result.json()
    // }

    async function postapi() {

        nameVal = name_input.value;
        amountVal = amount_input.value;
        commentsVal = comments_input.value;
        console.log("Before fetch ",JSON.stringify({name:nameVal, amount:amountVal,comments:commentsVal}));
        console.log(typeof(nameVal),nameVal)
        url = '/api/place_bid';
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify({name:nameVal,amount:amountVal,comments:commentsVal}),
          headers: {
            'Content-Type': 'application/json'
          } 
        });
        // const data = await response.json();
        // console.log(data);; 
      
      }
    
    // postData('/api/place_bid', { answer: 42 })
    //   .then(data => {
    //     console.log(data); // JSON data parsed by response.json()
    //   })
    //   .catch(error => {
    //     console.error('Error:', error);
    //   });

    formInput.style.display = "none";

    btn.addEventListener("click", () =>{
      if(formInput.style.display === "block"){
        formInput.style.display = "none";
      }else{
        formInput.style.display = "block";
      }
    })

    formInput.addEventListener("submit",(event)=>{
      postapi()
      event.preventDefault();
      // const inputData = new FormData(formInput);
      // const data = JSON.loads(inputData);

      // console.log(data);

    })
    
  });