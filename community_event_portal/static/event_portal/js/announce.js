document.addEventListener("DOMContentLoaded", function(){

    const bar = document.getElementById("announcement-bar");
    const closeBtn = document.getElementById("close-announcement");

    // Slide down when page loads
    setTimeout(function(){
        bar.classList.add("show");
    }, 2000);

    // Close the bar
    closeBtn.addEventListener("click", function(){
        bar.classList.remove("show");
    });

});