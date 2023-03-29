<?php
 session_start(); 
?>
<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>Enter Your OTP</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  
      <link rel="stylesheet" href="./style.css">

  
</head>

<body>

  <div class="keypadwrapper">
  <div class="inputwrapper">
    <span class="numberinput"></span>
    <span class="numberinput"></span>
    <span class="numberinput"></span>
    <span class="numberinput"></span>
    <span class="numberinput"></span>
    <span class="numberinput"></span>
    
  </div>
  <div class="keypad">
    <div id="lineone" class="numberline">
      <div class="content">
        <div>
          <span class="number">1</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">2</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">3</span>
        </div>
      </div>
    </div>
    <div id="linetwo" class="numberline">
      <div class="content">
        <div>
          <span class="number">4</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">5</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">6</span>
        </div>
      </div>
    </div>
    <div id="linethree" class="numberline">
      <div class="content">
        <div>
          <span class="number">7</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">8</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">9</span>
        </div>
      </div>
    </div>
    <div id="linefour" class="numberline">
      <div class="content">
        <div>
          <span class="number"><</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">0</span>
        </div>
      </div>
      <div class="content">
        <div>
          <span class="number">GO</span>
        </div>
      </div>
    </div>
  </div>
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.1/jquery.min.js'></script>

  

    <script>
      var j = 0;
      console.log(j);
      $(function () {
  $(".content").click(function () {

    var value = $(this).find(".number").text();
    //alert(value)
    if (value !== "<" && value !=="GO") {
      $(".numberinput").each(function () {
        var a = $(this).text();
        
        if (!a) {
          $(this).text(value);
          $(this).addClass("nocircle");
          return false;
        }
      });
    }
     if (value == "<") {
      $($(".numberinput").get().reverse()).each(function () {
        var a = $(this).text();
        if (a) {
          $(this).text("");
          $(this).removeClass("nocircle");
          return false;
        }
      });
    }

    if(value=="GO"){
    var otp=($(".numberinput").text());
    // console.log(otp);
        
    if(otp==<?php echo $_SESSION['otp'] ?>){
    //exec("C:\\Users\\jfern\\Anaconda3\\envs\\test\\python.exe servo.py", $output);    
    window.location.replace("servo.php");    
    }
    
    else
      { if (j < 3 ){
        alert("ERROR");
        }
        j = j + 1;
        if (j == 3){
          alert("OTP entered incorrectly thrice. Redirecting to home page.");
          window.location.replace("index.html");  
        }
        
      }
    }



    
    // <?php
     
    // $age=$_POST['age']; 
    // echo "<strong>".$nm." is $age years old.</strong>"; 
    // ?> 


  });

});
    </script>




</body>

</html>
