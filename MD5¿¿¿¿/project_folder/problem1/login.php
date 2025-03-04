<?php
error_reporting(E_ALL);
ini_set('display_errors',1);
ini_set('display_startup_errors',1);
include './config/config.php';

$conn= new mysqli('mysql', $db_username,$db_password, $db_name, $port);

if($conn->connect_error){
 die("connection failed: ".$conn->connect_error);
}
if($_SERVER["REQUEST_METHOD"]=="POST"){
 $user= mysqli_real_escape_string($conn,$_POST['username']);
 $pass= mysqli_real_escape_string($conn,$_POST['password']);
 
 $sql=@mysqli_fetch_array(mysqli_query($conn, "SELECT * FROM users WHERE username='admin' AND password='".md5($pass,true)."'"));
 if(isset($sql[0])){
  echo "hello admin"."<br />"; 
  define('ALLOW_FLAG_ACCESS',true);
  include 'flag.php';
  echo "<br><b>FLAG:</b> ".$flag;
 }else{
  echo "login failed";
 }
}
?>
<form method="POST" action="">
 <label for="username">ID:</label>
 <input type="text" name="username" required>
 <label for="password">password:</label>
 <input type="password" name="password" required pattern="[A-Za-z]+">
 <input type="submit" value="login">
</form>


