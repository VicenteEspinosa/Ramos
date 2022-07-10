# Requisitos para correr

Se necesita un usuario creado en AWS.

Luego se deben agregar las credenciales de este al ambiente:

```bash
export AWS_SECRET_ACCESS_KEY=
```

```bash
export AWS_ACCESS_KEY_ID=
```

```bash
export AWS_DEFAULT_REGION=us-east-1
```

Despues de esto se puede ejecutar el Terraform en esta carpeta

<br>

```bash
terraform init
```

Para descargar todo lo necesario para ejecutar el archivo

<br>

```bash
terraform validate
```

Para comprobar si la sintaxis del archivo es correcta

<br>

```bash
terraform plan
```

Para ver los cambios que serían aplicados al ejecutar

<br>

```bash
terraform apply
```

Para aplicar los cambios

<br>

```bash
terraform destroy
```

Para revertir los cambios