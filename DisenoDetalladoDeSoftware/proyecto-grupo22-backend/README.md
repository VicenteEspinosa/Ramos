# proyecto-grupo22-backend

### Integrantes del equipo

[Link-App-Producción]

| Nombre | GitHub | Email |
| :---------- | :--------- | :-------- |
| Vicente Espinosa | [@VicenteEspinosa] | [vnespinosa@uc.cl]
| Alejandro Rico | [@alericoj10] | [arico@uc.cl ]
| Ignacio Zúñiga | [@inzuniga] | [ Inzuniga@uc.cl ]


[@VicenteEspinosa]:              https://github.com/VicenteEspinosa
[vnespinosa@uc.cl]:    mailto:vnespinosa@uc.cl
[@alericoj10]:              https://github.com/alericoj10
[arico@uc.cl]:    mailto:arico@uc.cl
[@inzuniga]:              https://github.com/inzuniga
[Inzuniga@uc.cl ]:    mailto:Inzuniga@uc.cl 

[Link-App-Producción]: https://backend-dds-g22.herokuapp.com/

### Pasos para ejecutar Localmente
1. Clonar repositorio, última versión rama main
2. Ejecutar `bundle install`
3. Setear variables de entorno en archivo `.env`:
   1. `DATABASE_USERNAME=<usuario de tu base de datos>`
   2. `DATABASE_PASSWORD=<contraseña de tu usuario>`
   3. `DATABASE_HOST=localhost`
4. Ejecutar comando `rails db:create`
5. Ejecutar comando `rails db:migrate`
6. Ejecutar comando `rails db:seed`
7. Ejecutar comando `rails s -p 8000`


### Testing

Para correr los test, se debe correr el siguiente comando:

` bundle exec rspec`

Finalmente, en la carpeta coverage/index.html se encuentra el detalle del coverage.