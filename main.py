import openai
import os
import sys
# import json


openai.api_key = os.environ['OPENAI_API_KEY']

import openai
import streamlit as st
import numpy as np

# zainicjowanie połączenia z OpenAI API


# stworzenie interfejsu użytkownika za pomocą streamlit
st.title("Marketing Specialist Chatbot")
st.write("Witaj! Jestem specjalistą marketingu i mogę Ci pomóc w pisaniu cold maili i maili sprzedażowych. Co chcesz napisać?")

# pole wyboru języka
language = st.selectbox("Wybierz język", ["Angielski", "Francuski", "Niemiecki","Polski"])

# pole wyboru typu wiadomości
message_type = st.selectbox("Wybierz typ wiadomości", ["Cold email", "Mail sprzedażowy"])

# pole wyboru celu
purpose = st.selectbox("Wybierz cel wiadomości", ["Pozyskanie nowych klientów", "Podtrzymanie relacji z obecnymi klientami"])

# pole wyboru segmentu docelowego
target_segment = st.selectbox("Wybierz segment docelowy", ["Segment rynku", "Wiek", "Lokalizacja"])

# pole wprowadzania tekstu
user_input = st.text_input("Napisz swoją wiadomość")

# przycisk generowania odpowiedzi
if st.button("Wygeneruj odpowiedź"):
    # wywołanie OpenAI API, aby uzyskać odpowiedź na pytanie użytkownika
    prompt = f"Język: {language} \n Typ wiadomości: {message_type} \n Cel: {purpose} \n Segment docelowy: {target_segment} \n Treść wiadomości: {user_input}"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Jesteś specjalistą od spraw ecommerce. Potrafisz pisać unikalne opisy produktów.  "},
        {"role": "user",
         "content":prompt}
    ]
)
    st.write("Oto odpowiedź na Twoją wiadomość:")
    st.write(response['choices'][0]['message']['content'])

# pole wyboru generowania przykładowych tekstów
sample_texts = [
    "Jak zdobyć więcej klientów?",
    "Jak zwiększyć sprzedaż?",
    "Jak zwiększyć zasięg swojego biznesu?",
]
sample_text = st.selectbox("Wybierz przykładowy tekst", sample_texts)

# przycisk wyświetlania przykładowych tekstów
if st.button("Pokaż przykładowy tekst"):
    st.write("Oto przykładowy tekst:")
    st.write(sample_text)

# funkcja zapisywania historii wiadomości
if st.button("Zapisz historię wiadomości"):
    with open("historia.txt", "a") as f:
        f.write(user_input + "\n")
    st.write("Wiadomość została zapisana!")







# pytanie = input('Zadaj pytanie')
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "Jesteś specjalistą od spraw ecommerce. Potrafisz pisać unikalne opisy produktów.  "},
#         {"role": "user",
#          "content":pytanie}
#     ]
# )
#
# odpowiedz = response['choices'][0]['message']['content']
# print(response['usage'])
# print(response['id'])
# print(response['object'])
# print(response.keys())
#
# with open('pytania_odpowiedzi.json', 'w',encoding='utf-8') as f:
#     dane = {
#     "id": 1,
#     "pytanie": pytanie,
#     "odpowiedz": odpowiedz
#     }
#     json.dump(dane, f, ensure_ascii=False, indent=4)
#
# print(f'odpowiedź: {odpowiedz}')