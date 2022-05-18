# Data-Pipeline-Arkon 📈
Data pipeline para recolectar y almacenar los datos abiertos de la ubicación del Metrobus y poder consultarlos a través de una API Rest filtrando por unidad y alcaldía.

## Instalación 
Dokcer and Docker-compose son requeridos
```sh
docker-compose build
docker-compose up
docker-compose run --rm app python manage.py makemigrations
docker-compose run --rm app python manage.py migrate
```
## URLs
La APi se ubica en la dirección http://localhost:8000/ con los siguientes
EndPoints
| EndPoints | Uso |
| ------ | ------ |
| /api/unit/ | Lista las unidades disponibles |
| /api/unit/{id} | Ubicación de la unidad por id |
| /api/district/ | Lista de alcaldías disponibles |
| /api/district/{id}/unit_list/ | Lista de unidades disponibles por id de alcaldía |

También se pude hacer uso de peticiónes GraphQL
añadiendo ?query={} al EndPoint
Ejemplo

```url
/api/unit/?query={id}
```

## Testing
Se pueden correr 
```sh
docker-compose run --rm app python manage.py test
```

> Note: La carpeta .env será mandada al control de versiones para su despliegue automático, esta contiene las variables que son necesarias en la aplicación y en una aplicación real, no deben almacenarse en el control de versiones.




