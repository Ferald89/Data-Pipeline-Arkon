# Data-Pipeline-Arkon 馃搱
Data pipeline para recolectar y almacenar los datos abiertos de la ubicaci贸n del Metrobus y poder consultarlos a trav茅s de una API Rest filtrando por unidad y alcald铆a.

## Instalaci贸n 
Dokcer and Docker-compose son requeridos
```sh
docker-compose build
docker-compose up
docker-compose run --rm app python manage.py makemigrations
docker-compose run --rm app python manage.py migrate
```
## URLs
La APi se ubica en la direcci贸n http://localhost:8000/ con los siguientes
EndPoints
| EndPoints | Uso |
| ------ | ------ |
| /api/unit/ | Lista las unidades disponibles |
| /api/unit/{id} | Ubicaci贸n de la unidad por id |
| /api/district/ | Lista de alcald铆as disponibles |
| /api/district/{id}/unit_list/ | Lista de unidades disponibles por id de alcald铆a |

Tambi茅n se pude hacer uso de petici贸nes GraphQL
a帽adiendo ?query={} al EndPoint
Ejemplo

```url
/api/unit/?query={id}
```

## Testing
Se pueden correr 
```sh
docker-compose run --rm app python manage.py test
```

> Note: La carpeta .env ser谩 mandada al control de versiones para su despliegue autom谩tico, esta contiene las variables que son necesarias en la aplicaci贸n y en una aplicaci贸n real, no deben almacenarse en el control de versiones.




