$(document).ready(function () {
  $(document).on("click", ".add-new-job", function (e) {
    e.preventDefault();
    $("#add_new_job").modal("show");
  });

  $(document).on("click", ".view-job-details", function(e){
    e.preventDefault()
    

    var commitment = $(this).parents(".job-detail").find('.commitment').text(),
    department = $(this).parents(".job-detail").find('.department').text(),
    team =$(this).parents(".job-detail").find('.team').text(),
    location=$(this).parents(".job-detail").find('.location').text(),
    description=$(this).parents(".job-detail").find('.description').text();
    

    var body = '<p>'+commitment+'</p><p>'+department+'</p><p>'+team+'</p><p>'+location+'</p><p>'+description+'</p>'

    $('#job_details .modal-body').empty().append(body)
    
    $("#job_details").modal("show");

  })
});
