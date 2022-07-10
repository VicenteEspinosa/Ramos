<?php 
    $json_string = file_get_contents("http://e5grupo96.herokuapp.com/messages");
    session_start();
    $id = $_SESSION['id'];
    $fi = $_POST["fecha_i"];
    $ff = $_POST["fecha_f"];
    $data = json_decode($json_string, TRUE);
    $enviados = array();
    foreach($data as $item) {
        if ($item["sender"] == $id) {
            $enviados[] = $item;
        };
    };
    $marker_list = array();
    foreach($enviados as $msj){
        if (( $msj["date"] >= $fi ) && ( $msj["date"] <= $ff )) {
            $marker_list[] = ["lat" =>$msj["lat"] , "long"=> $msj["long"]];
        };
    };
?> 

<html>
 <head>
  <title>Coordenadas del mensaje</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
	integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
	crossorigin=""/>
 </head>
 <body>
 <?php echo '<p>Hello World</p>'; ?> 
 <?php 
    $lat = -22.5;
    $long = -68.9;
?>

 <div id="mapid" style="height: 500px"></div>
 </body>

 <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
   integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
   crossorigin=""></script>
<script>
    var map = L.map('mapid').setView([<?php echo $lat ?>, <?php echo $long ?>], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    <?php foreach($marker_list as $marker) {
        echo 
        'L.marker([' . $marker["lat"] . ',' . $marker["long"] . ']).addTo(map);';
    } ?>
</script>
</html>