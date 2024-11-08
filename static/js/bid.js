document.addEventListener("DOMContentLoaded", () => {
  console.log("In bid.js script");

  const btn = document.getElementById("btnButton");
  const formInput = document.getElementById("bidInput");
  const submitBtn = document.getElementById("submit");
  const bidContainerID = document.getElementById("bidContainer")


    async function postapi() {
      const name_input = document.getElementById("nameinput").value;
      const amount_input = document.getElementById("amount").value;
      const comments_input = document.getElementById("comments").value;
      const listingId = document.getElementById("bidInput").getAttribute("data-id")
    
      const formData = {
        bidder_name: name_input,
        bid_amount: amount_input,
        comment: comments_input,
        listing_id: listingId
      }
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
        throw console.log(response.json()), new Error(`HTTP error! Status: ${response.status}`);
      }
    
      const data = await response.json();
      console.log('Success:', data);

      const newName = document.createTextNode(name_input);
      const newBid = document.createTextNode("$"+amount_input);
      const newComment = document.createTextNode(comments_input);

      const newDiv = document.createElement("div");
      const newPname = document.createElement("p");
      const newPamount = document.createElement("p");
      const newPcomment = document.createElement("p");

      newDiv.classList.add("bidDiv")

      newPname.appendChild(newName);
      newPamount.appendChild(newBid);
      newPcomment.appendChild(newComment);

      newDiv.appendChild(newPname).classList.add("top");
      newDiv.appendChild(newPamount).classList.add("top");
      newDiv.appendChild(newPcomment).classList.add("bot");

      bidContainerID.prepend(newDiv);

      if (formInput.style.display === "block") {
        formInput.style.display = "none";
      } else {
        formInput.style.display = "block";
      }

    }

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
  })

});