$(document).ready(function() {
  // SideNav Button Initialization
  $(".button-collapse").sideNav2();
  // SideNav Scrollbar Initialization
  var sideNavScrollbar = document.querySelector('.custom-scrollbar');
  var ps = new PerfectScrollbar(sideNavScrollbar);
  });

//Display and hide certain div classes
$(document).ready(function(){
  $(".userProfile").click(function(){
    $(".job-listing").hide();
    $(".user-details").show();
    

  });

});

function userProfile() {
  document.getElementById("job-listing").style.display = "none"; //hides
  document.getElementById("user-details").style.display = "block"; //shows




}

