from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []
did_not_read = []