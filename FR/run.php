<html>
 
  <head>
   <title>
     run
   </title>
  </head>
<body>
   <form method="post">

    <input type="submit" value="GO" name="GO">
   </form>


<?php
	if(isset($_POST['GO']))
	{
		exec("C:\Users\jfern\Anaconda3\python.exe face_detection.py",$output);
    print_r($output);
	}
?>
</body>
</html>