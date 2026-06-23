film_title = input("Mi a film címe?: ")
film_duration = input("hány perces a film?:")

óra = int(film_duration) // 60
perc = int(film_duration) % 60

print(f"A film hossza: {óra} óra {perc} perc")