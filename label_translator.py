dict = {
  "Classique":"GENERAL",
  "Sport":"SPORT",
  "Jeux-vidéo / Culture Web":"WEB",
  "Moderne":"POP",
  "Histoire":"HISTOIRE",
  "Sciences":"SCIENCE",
  "Géographie":"GEOGRAPHIE",
  "Musiques":"MUSIQUE",
  "Animaux et plantes": "NATURE",
  "Culture générale": "GENERAL"
}

def translate(LTDS_label):
  return dict[LTDS_label]