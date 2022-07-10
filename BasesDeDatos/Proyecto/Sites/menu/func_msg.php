<?php

session_start();

$message = $_POST['message'];
$receptant = $_POST['receptant'];
$id = $_SESSION['id'];


$url = "https://e5grupo96.herokuapp.com/users";
$json = file_get_contents("http://e5grupo96.herokuapp.com/users");

#echo $json;
$json = str_replace("[","",$json);
$json = str_replace("]","",$json);
$json = str_replace("},{","|",$json);
$json = str_replace("{","",$json);
$json = str_replace("}","",$json);

$lista = explode('|',$json);

$exists = false;
foreach($lista as $element){
    #echo($element);
    if (strpos($element, $receptant) !== false){
        #echo $receptant;
        $pos = strpos($element,'uid');
        $elementos = explode(':',$element);
        $uid = end($elementos);
        #echo $uid;
        $exists = true;
    }
}
  
$lat = random_int ( 0 , 100);
$long = random_int ( 0 , 100);

if ($exists == true){
    $url = "https://e5grupo96.herokuapp.com/messages";
    $data = array("date"=>"2020-10-10",
    "lat"=>$lat,
    "long"=>$long,
    "message"=>$message,
    "receptant"=>$uid,
    "sender"=>$id);

    $postdata = json_encode($data);
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postdata);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    $result = curl_exec($ch);
    curl_close($ch);
    print_r ($result);

    if($result === FALSE){
        die(curl_error($ch));
    }
}
else {echo("Usuario no existe");}

?>
<form align="center" action="menu.php" method="post">
  <input type="submit" name="Volver" class="btn btn-primary btn-block" value="Volver" />
</form>
