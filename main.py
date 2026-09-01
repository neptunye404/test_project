meme_dict = {
    "CRINGE": "Roblox New Gen",
    "LOL": "Mirtilli",
}

parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola in meme_dict.keys():
    if parola == "CRINGE":
        print("Roblox New Gen")
    elif parola == "LOL":
        print("Mirtilli")
else:
    print("La parola non è stata trovata");
