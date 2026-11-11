# LTDS_scrapper

Récupère les questions du jour du mode **facile** de [La Table des Savoirs](https://latabledessavoirs.fr) et les importe automatiquement dans [Kultero](https://kultero.cloud).

À chaque exécution, le script :
1. récupère les questions du jour (texte, réponses valides, thème) depuis l'API de La Table des Savoirs ;
2. crée sur Kultero une liste publique nommée avec la date du jour (`JJ-MM-AAAA`) et l'ajoute au groupe ;
3. crée chaque question avec toutes ses réponses acceptées, en convertissant le thème en label Kultero ;
4. ajoute chaque question à la liste.

## Installation

```bash
pip install requests pyyaml
```

## Configuration

Copier le modèle puis renseigner les deux tokens (sans le préfixe `Bearer `) :

```bash
cp config.example.yml config.yml
```

```yaml
ltds_token: "<token La Table des Savoirs>"
kultero_token: "<token Kultero>"
```

`config.yml` est ignoré par git, les tokens ne sont donc pas commités.

## Utilisation

```bash
python main.py
# ou avec un autre fichier de config
python main.py chemin/vers/config.yml
```

## Fichiers

- `main.py` : point d'entrée, lit la config et enchaîne récupération et envoi
- `content_getter.py` : récupère les questions depuis La Table des Savoirs
- `content_sender.py` : crée la liste et les questions sur Kultero
- `label_translator.py` : convertit les thèmes LTDS en labels Kultero
