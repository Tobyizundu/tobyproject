

//When button pressed calls the function get revies
document.getElementById('button').addEventListener
('click', button);

function button(){
  //Fetches data from API
  fetch('https://student.computing.edgehill.ac.uk/~walshd/cis1110api/product-reviews/bikeoil')
  .then((res) => res.json())
  .then((data) => {
    //output
    let output = '<h3>ALL REVIEWS</h3> <hr/>';
    
    data.forEach(function(review){
      //star rating variable
     
      //Sets starrating to nothing
       var starrating = ``;
      //Sets how many stars are red or black
      var star0 =`<em>★★★★★</em>`;
      var star1 =`★<em>★★★★</em>`;
      var star2 =`★★<em>★★★</em>`;
      var star3 =`★★★<em>★★</em>`;
      var star4 =`★★★★<em>★</em>`;
      var star5 =`★★★★★`;
    
    
      //converts the number rating into stars
      if (review.rating ==0){
        starrating = star0;
      }
      if (review.rating ==1){
        starrating = star1;
      }
      if (review.rating ==2){
        starrating = star2;
      }
      if (review.rating ==3){
        starrating = star3;
      }
      if (review.rating ==4){
        starrating = star4;
      }
      if (review.rating ==5){
        starrating = star5;
      }
     
     
      //output to the page
      output += `
      <div class="itemproduct4">
        <img class="reviewimage" src="robot-juice-images/reviewicon1.jpg" alt="">
        <P class="p6">
          ${review.nickname}
        </P>
        <P class="p7">
          ${starrating}
        </P>
      </div>
      <div class="itemproduct5">
        <P>
          ${review.review}
        </p>
      </div>
      <div class="itemproduct6">
        <br>
        <hr />
        <br>
      </div>
      `;

    });

    
    //hides the button
    document.getElementById('output').innerHTML = output;
    document.getElementById('button').style.display = 'none'
  })
}