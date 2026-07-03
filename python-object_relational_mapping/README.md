# Python - Object-relational mapping

## Description
Interaction avec une base de données MySQL depuis Python : d'abord avec `MySQLdb` (requêtes SQL brutes), puis avec l'ORM SQLAlchemy (modèles `State` et `City`).

## Fichiers

| Fichier | Description |
|---|---|
| `0-select_states.py` / `.sql` | Affiche tous les états d'une base de données |
| `1-filter_states.py` | Affiche les états dont le nom commence par une lettre donnée |
| `2-my_filter_states.py` | Variante sécurisée avec paramètres |
| `3-my_safe_filter_states.py` | Requête sécurisée contre les injections SQL |
| `4-cities_by_state.py` / `.sql` | Affiche les villes par état |
| `5-filter_cities.py` | Affiche les villes d'un état donné |
| `6-model_state.py` / `.sql` | Premier modèle SQLAlchemy `State` |
| `7-model_state_fetch_all.py` / `.sql` | Récupère tous les états via SQLAlchemy |
| `8-model_state_fetch_first.py` | Récupère le premier état via SQLAlchemy |
| `9-model_state_filter_a.py` | Filtre les états contenant la lettre `a` |
| `10-model_state_my_get.py` | Récupère un état par son nom |
| `11-model_state_insert.py` | Insère un nouvel état |
| `12-model_state_update_id_2.py` | Met à jour un état |
| `13-model_state_delete_a.py` | Supprime les états contenant `a` |
| `14-model_city_fetch_by_state.py` / `.sql` | Récupère les villes liées aux états |
| `model_state.py` / `model_city.py` | Définitions des modèles SQLAlchemy `State` et `City` |

## Auteur
Vadim Gavet - Holberton School
