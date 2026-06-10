#!/usr/bin/python3
"""Consommation de l'API JSONPlaceholder avec requests."""
import requests
import csv


def fetch_and_print_posts():
    """Récupère les posts et affiche le code de statut + les titres."""
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    donnees = reponse.json()
    print(f"Status Code: {reponse.status_code}")

    if reponse.status_code == 200:
        for donnee in donnees:
            print(donnee['title'])


def fetch_and_save_posts():
    """Récupère les posts et les enregistre dans un fichier CSV."""
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    donnees = reponse.json()
    print(f"Status Code: {reponse.status_code}")

    if reponse.status_code == 200:
        extrait = [{"id": data["id"], "title": data["title"],
                    "body": data["body"]} for data in donnees]

        with open("posts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(extrait)
