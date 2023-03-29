<?php
 ini_set('max_execution_time',180);
exec("C:\\Users\\jfern\\Anaconda3\\envs\\test\\python.exe face_recognition_fast.py", $output);
print_r($output);
// print($output[1])
session_start();
$_SESSION['otp'] = $output[0];



function redirect($url) {
    ob_start();
    header('Location: '.$url);
    ob_end_flush();
    die();
}

if($output[0]== "Unlocked"){  
	exec("C:\\Users\\jfern\\Anaconda3\\envs\\test\\python.exe servo.py", $outputserv);
	if($outputserv[0]== "Unlocked"){
 		redirect("success.php");
 	}	   
}

else{
	echo "Locked Contact Home owner ";
 	redirect("OTPindex.php"); 

}




?>