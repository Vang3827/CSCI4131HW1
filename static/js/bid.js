document.addEventListener("DOMContentLoaded", () => {
  console.log("In bid.js script");

  const btn = document.getElementById("btnButton");
  const formInput = document.getElementById("bidInput");
  const submitBtn = document.getElementById("submit");
  const name_input = document.getElementById("nameinput").value;
  const amount_input = document.getElementById("amount").value;
  const comments_input = document.getElementById("comments").value;

  const formData = {
    name: name_input,
    amount: amount_input,
    comments: comments_input
  }

    async function postapi(event) {
      console.log("Before fetch ", JSON.stringify(formData));
      url = '/api/place_bid';
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      console.log("After fetch ", body)
      const data = await response.json();
      console.log('Success:', data);
    }
    

//   async function handleSubmit(event) {
//     // event.preventDefault(); // Prevent the default form submission

//     // Gather form data
//     // const name = document.getElementById("name").value;
//     // const email = document.getElementById("email").value;

//     // Create an object with the form data
//     const formData = {
//         name: name_input,
//         email: amount_input
//     };

//     try {
//         // Send the data with a fetch POST request using async/await
//         const response = await fetch('/api/place_bid', { // Replace with your API endpoint
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify(formData) // Convert the object to a JSON string
//         });

//         // Check if the response is successful (status code 200-299)
//         if (!response.ok) {
//             throw new Error(`HTTP error! Status: ${response.status}`);
//         }

//         // Parse the JSON response
//         const data = await response.json();

//         // Handle the response data (e.g., show a success message)
//         console.log('Success:', data); // Log the response from the server
//     } catch (error) {
//         // Handle any errors (e.g., network issues)
//         console.error('Error:', error);
//     }
// }


  formInput.style.display = "none";

  btn.addEventListener("click", () => {
    if (formInput.style.display === "block") {
      formInput.style.display = "none";
    } else {
      formInput.style.display = "block";
    }
  })

  submitBtn.addEventListener("click", (event) => {
    event.preventDefault();
    postapi()
    // handleSubmit();
    
    // const inputData = new FormData(formInput);
    // const data = JSON.loads(inputData);

    // console.log(data);

  })

});