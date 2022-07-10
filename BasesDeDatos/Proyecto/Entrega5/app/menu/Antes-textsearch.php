<h3>Text-Search</h3>
                 <form align="center" action="E5-textsearch.php" method="post">

                    <label>UserId</label>
                    <input type="text" name="id"/>
                    <br />
                    <label>Forbidden</label>
                    <input type="text" name="forbidden" class="form-control" />
                    <br />
                    <label>Desired</label>
                    <input type="text" name="desired" class="form-control" />
                    <br />
                    <label>Required</label>
                    <input type="text" name="required" class="form-control" />
                    <br />
                    <input type="submit" name="Buscar" class="btn btn-primary btn-block" value="Buscar" />
                    <br> Separa frases por ";"
                </form>

                <form align="center" action="menu.php" method="post">
                  <input type="submit" name="Volver" class="btn btn-primary btn-block" value="Volver" />
                </form>
