<?php
  
  // If uploadl button is clicked ...
  if (isset($_POST['upload'])) {
    exec("C:\\Users\\jfern\\Anaconda3\\envs\\test\\python.exe serv.py");

}
?>
<!DOCTYPE html>
<html lang="en" style="background-color: black;">
    <head >
        <!--
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
-->
        <title>Success</title>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" >
        <link rel="stylesheet" type="text/css" href="success.css">
        <!-- Optional theme
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" >
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <link rel="stylesheet" href="form.css" >
        <script src="form.js"></script>
     -->
    
    <body >
        <div class="container">
            <div class="row">
                <div class="col-md-6 col-md-offset-3">
                    <!-- <h2>Success</h2> -->
                   <center><IMG SRC="door.gif"></center>
                    <form role="form" method="post" id="reused_form" enctype="multipart/form-data">
                        
                            <div class="col-sm-12 form-group">
                                <button type="submit" class="btn btn-lg btn-danger btn-block" id="upload" name = "upload" style="margin: 10px">LOCK </button>
                            </div>
                        </div>
                    </form>
                    <div id="success_message" style="width:100%; height:100%; display:none; "> <h3>Sent your message successfully!</h3> </div>
                    <div id="error_message" style="width:100%; height:100%; display:none; "> <h3>Error</h3> Sorry there was an error sending your form. </div>
                </div>
            </div>
        </div>
        <script>
    setTimeout(function(){
       window.location.href = 'index.html';
    }, 7000);
</script>
    <!-- <script src="otp.js" > </script>   -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>

