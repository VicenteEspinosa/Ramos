<?php

session_start();


$id = $_SESSION['id'];

$url = "https://e5grupo96.herokuapp.com/users";
$json = file_get_contents("http://e5grupo96.herokuapp.com/messages");

#echo $json;
$json = str_replace("[","",$json);
$json = str_replace("]","",$json);
$json = str_replace("},{","|",$json);
$json = str_replace("{","",$json);
$json = str_replace("}","",$json);

$lista = explode('|',$json);


$mensajes = array();

foreach($lista as $element){
    #echo($element);
    if (strpos($element,"receptant\":{$id},") !== false){
        #echo($element);
        array_push($mensajes, $element);

    }
}

?>

 <table>
     <tr>
       <th>Mensaje</th>

     </tr>


   <?php

   foreach ($mensajes as $mensaje) {
       echo "<tr><td>$mensaje</td></tr>";
 }
 ?>
</table>
<form align="center" action="Antes-recibidos.php" method="post">
  <input type="submit" name="Volver" class="btn btn-primary btn-block" value="Volver" />
</form>
