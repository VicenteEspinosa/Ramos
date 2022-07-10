<?php session_start();
include('../templates/header.html');
   ?>


<?php
    if (array_key_exists("id_elegido",$_POST) == true){
      $id = $_POST["id_elegido"];
      $_SESSION['id'] = $id;
    }

  ?>

<h1> Hello World </h1>
<p> <?php print "Usuario iniciado: ".$_SESSION['id'] ?> </p>

<body>
  <h3 align="center"> Buscar mensajes enviados</h3>

  <form align="center" action="Antes-enviados.php" method="post">
    <input type="submit" value="Buscar">
  </form>

  <br>
  <br>
  <br>
  <h3 align="center"> Buscar mensajes recibidos</h3>

<form align="center" action="Antes-recibidos.php" method="post">
  <input type="submit" value="Buscar">
</form>

<br>
<br>
<br>

</body>

  <h3 align="center"> Enviar mensajes</h3>
  <form align="center" action="send_msg.php" method="post">
    <input type="submit" value="Enviar">
  </form>
<br>
<br>
<br>

</body>
<h3 align="center"> Buscar mensaje</h3>

<form align="center" action="Antes-textsearch.php" method="post">
  <input type="submit" value="Buscar">
</form>

<br>
<br>
<br>

</body>
<h3 align="center"> Ver mapa de mensajes "YYYY-MM-DD"</h3>

<form align="center" action="map.php" method="post">
    Fecha Inicial:
    <input type="date" name="fecha_i">
        <br/><br/>
    Fecha Final:
    <input type="date" name="fecha_f">
        <br/><br/>
    <input type="submit" value="Buscar">
</form>

<br>
<br>
<br>

</body>


</body>



<?php include('../templates/footer.html'); ?>
