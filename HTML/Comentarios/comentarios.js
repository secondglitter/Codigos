document.addEventListener("DOMContentLoaded", function() {
    const comments = document.querySelectorAll(".carousel-comment");
    const prevButton = document.querySelector(".carousel-arrow.left");
    const nextButton = document.querySelector(".carousel-arrow.right");
    let currentIndex = 0;
  
    function showComment(index) {
      comments.forEach((comment, i) => {
        comment.classList.toggle("active", i === index);
      });
    }
  
    prevButton.addEventListener("click", () => {
      currentIndex = (currentIndex - 1 + comments.length) % comments.length;
      showComment(currentIndex);
    });
  
    nextButton.addEventListener("click", () => {
      currentIndex = (currentIndex + 1) % comments.length;
      showComment(currentIndex);
    });
  
    showComment(currentIndex); // Show the first comment initially
  });
  