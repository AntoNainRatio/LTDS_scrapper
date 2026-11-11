import content_getter
import content_sender
import sys
import os
import yaml

DEFAULT_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yml")

def load_config(path):
  try:
    with open(path, "r", encoding="utf-8") as f:
      config = yaml.safe_load(f) or {}
  except FileNotFoundError:
    print(f"LTDS_scrapper Error: config file not found: {path} (copy config.example.yml to config.yml)")
    return None

  tokens = {}
  for key in ("ltds_token", "kultero_token"):
    value = config.get(key)
    if not value or not str(value).strip():
      print(f"LTDS_scrapper Error: missing \"{key}\" in {path}")
      return None
    value = str(value).strip()
    if value.startswith("Bearer "):
      value = value[len("Bearer "):].strip()
    tokens[key] = value
  return tokens

def main(args):
  if len(args) > 1:
    print("LTDS_scrapper Usage: python main.py [path/to/config.yml]")
    return 1
  config = load_config(args[0] if args else DEFAULT_CONFIG)
  if config is None:
    return 1
  data = content_getter.get_page(config["ltds_token"])
  l = content_getter.get_questions(data)
  content_sender.send_full(config["kultero_token"], l)
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
