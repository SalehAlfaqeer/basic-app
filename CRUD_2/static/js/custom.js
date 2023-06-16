$(document).ready(function() {
    // Show the alert
    $("#myAlert").fadeIn(500);
  
    // Hide the alert after 3 seconds
    setTimeout(function() {
      $("#myAlert").fadeOut(500);
    }, 3000);
  });