import requests

def get_page(token):
  API = "https://api.latabledessavoirs.fr"
  headers= {"Authorization": "Bearer "+token}

  r = requests.get(f"{API}/game/facile", headers=headers)

  r.raise_for_status()
  data = r.json()

  return data

def print_data(data):
  print("Score: "+str(data["playerGame"]["score"]))
  for q, a in zip(data["day"]["questions"], data["playerGame"]["quizState"]["answers"]):
      print(q["order"], q["theme"], q["text"], "->", a["answer"], a["result"], a["points"])

def get_questions(data):
  res = []
  for q, a in zip(data["day"]["questions"], data["playerGame"]["quizState"]["answers"]):
    tmp = [q["text"], q["validAnswers"], q["theme"]]
    res.append(tmp)
  return res

def print_list(l):
  for e in l:
    print(f"({e[2]}) - {e[0]} --> {e[1]}")