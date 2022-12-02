#!/bin/zsh
echo "\n ==== Comenzando a ejecutar scrapers ==== \n"

for python_file_name in $(find scrapers -name '*.py')

do
   echo "Ejecutando $python_file_name..."
   python3 $python_file_name
done

echo "Scrapers ejecutados con éxito \n"