<?php
session_start();
?>
<html>
<?php
$data = array();
$data["userId"] = $_SESSION['id'];
// json encode data
$vacio = true;
$authToken = "d74c91f7-ba42-4903-aea3-d37a192d0d6d";
$data_string = json_encode($data);
// set up the curl resource
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://e5grupo96.herokuapp.com/text-search");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
       'Content-Type:application/json',
       'Content-Length: ' . strlen($data_string) ,
       'API-TOKEN-KEY:'.$authToken ));   // API-TOKEN-KEY is keyword so change according to ur key word. like authorization
// execute the request
$output = curl_exec($ch);
//echo $output;
// Check for errors
if($output === FALSE){
       die(curl_error($ch));
}
#echo($output) . PHP_EOL;
// close curl resource to free up system resources
curl_close($ch);

$str = substr($output, 180);

#$mid = $str['mid'];
$str = str_replace("{","",$str);
$lista = explode(", '",$str);

#$str = $output;
$mensajes = array();
$mensaje = array();

$n = 0;
foreach ($lista as $elemento)
  {
    $elemento = str_replace("}","",$elemento);
    $elemento = str_replace("{","",$elemento);
    $elemento = str_replace("[","",$elemento);
    $elemento = str_replace("]","",$elemento);
    $elemento = str_replace("'","",$elemento);
    $elemento = str_replace(":","",$elemento);
    #$elemento = str_replace("_id ","",$elemento);
    #$elemento = str_replace("mid ","",$elemento);
    #$elemento = str_replace("message ","",$elemento);
    #$elemento = str_replace("sender ","",$elemento);
    #$elemento = str_replace("receptant ","",$elemento);
    #$elemento = str_replace("lat ","",$elemento);
    #$elemento = str_replace("long ","",$elemento);
    #$elemento = str_replace("date ","",$elemento);
    #array_push($mensaje, $elemento);
    $n = $n + 1;
    if (strpos($elemento, '_id') !== false){
      $elemento = str_replace("_id ","",$elemento);
      $mensaje[0] = $elemento;
    }
    if (strpos($elemento, 'mid') !== false){
      $elemento = str_replace("mid ","",$elemento);
      $mensaje[1] = $elemento;
    }
    if (strpos($elemento, 'message') !== false){
      $elemento = str_replace("message ","",$elemento);
      $mensaje[2] = $elemento;
    }
    if (strpos($elemento, 'sender') !== false){
      $elemento = str_replace("sender ","",$elemento);
      $mensaje[3] = $elemento;
    }
    if (strpos($elemento, 'receptant') !== false){
      $elemento = str_replace("receptant ","",$elemento);
      $mensaje[4] = $elemento;
    }
    if (strpos($elemento, 'lat') !== false){
      $elemento = str_replace("lat ","",$elemento);
      $mensaje[5] = $elemento;
    }
    if (strpos($elemento, 'long') !== false){
      $elemento = str_replace("long ","",$elemento);
      $mensaje[6] = $elemento;
    }
    if (strpos($elemento, 'date') !== false){
      $elemento = str_replace("date ","",$elemento);
      $mensaje[7] = $elemento;
    }
    if ($n == 8){
      $n = 0;
      $mensajes[] = $mensaje;
      $mensaje = array();
    }
  }



 ?>
 <table>
     <tr>
       <th>ObjectId</th>
       <th>mid </th>
       <th>message</th>
       <th>sender</th>
       <th>receptant</th>
       <th>lat</th>
       <th>long</th>
       <th>date</th>
     </tr>


   <?php

   foreach ($mensajes as $mensaje) {
       echo "<tr><td>$mensaje[0]</td><td>$mensaje[1]</td><td>$mensaje[2]</td><td>$mensaje[3]</td><td>$mensaje[4]</td><td>$mensaje[5]</td><td>$mensaje[6]</td><td>$mensaje[7]</td></tr>";
 }
 ?>
</table>

<form align="center" action="Antes-enviados.php" method="post">
  <input type="submit" name="Volver" class="btn btn-primary btn-block" value="Volver" />
</form>
