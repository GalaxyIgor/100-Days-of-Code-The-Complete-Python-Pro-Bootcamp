def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    # Contagem das letras de "TRUE"
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    # Contagem das letras de "LOVE"
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    # Formando o score
    love_score = int(str(true_count) + str(love_count))

    print(love_score)


calculate_love_score(name1="Angela Yu", name2="Jack Bauer")