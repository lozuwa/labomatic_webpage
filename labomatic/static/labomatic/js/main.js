jQuery(document).ready(function($){
    $("moreExamplesButton").click(function(){
      $post("https:localhost:8000/", {"hello": 1}, function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
      });
    });
});