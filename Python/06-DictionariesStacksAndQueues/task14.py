import json
book = {
    "Title": "Dżuma",
    "Author": "Albert Camus",
    "Genre": "Philosophical novel",
    "Release date": 1947,
    "Charaters": ["Doctor Bernard Rieux","Cottard","Jean Tarrou"]

}

with open("Python/06-DictionariesStacksAndQueues/favorite.json" ,"w", encoding="utf-8") as file:
    json.dump(book,file,indent=True,ensure_ascii=False)
