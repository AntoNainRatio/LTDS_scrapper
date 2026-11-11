import requests
import label_translator

from datetime import date

API = "https://kultero.cloud/api/question"
groupId = "dd77c561-14aa-4a6c-93c5-c6d2f93c29c9"

def send_initial_question(kultero_token, question, answer, label):
  headers = {"Authorization": "Bearer "+kultero_token}
  kultero_label = label_translator.translate(label)
  body = { 
    "text":question, 
    "answer":answer, 
    "label": kultero_label
  }

  r = requests.post(f"{API}/questions", json=body, headers=headers)
  r.raise_for_status()
  return r.json()['id']

def send_aditional_answer(kultero_token, questionId, answer):
  headers = {"Authorization": "Bearer "+kultero_token}
  body = { "text": answer }

  r = requests.post(f"{API}/questions/{questionId}/answers", json=body, headers=headers)
  r.raise_for_status()
  return r.json()['id']

def send_full_question(kultero_token, question, answers, label):
  questionId = send_initial_question(kultero_token, question, answers[0], label)
  for i in range (1,len(answers)):
    send_aditional_answer(kultero_token, questionId, answers[i])
  return questionId

def link_question_to_list(kultero_token, listId, questionId):
  headers = {"Authorization": "Bearer "+kultero_token}
  r = requests.put(f"{API}/lists/{listId}/questions/{questionId}", headers=headers)
  r.raise_for_status()

def create_list(kultero_token):
  now = date.today()
  day = str(now.day)

  month = str(now.month)
  if len(month) < 2:
    month = '0'+ month

  year = str(now.year)

  name = f"{day}-{month}-{year}"
  body = { 
    "title":name, 
    "description":"", 
    "label":"GENERAL", 
    "visibility":"PUBLIC" 
  }

  header = {"Authorization":"Bearer "+kultero_token}

  r = requests.post(f"{API}/lists", headers=header, json=body)
  r.raise_for_status()
  
  listId = r.json()["id"]

  r2 = requests.put(f"{API}/groups/{groupId}/lists/{listId}", headers=header)
  r2.raise_for_status()

  return listId

def send_full(kultero_token, questions):
  listId = create_list(kultero_token)
  for e in questions:
    questionId = send_full_question(kultero_token,e[0],e[1],e[2])
    link_question_to_list(kultero_token, listId, questionId)