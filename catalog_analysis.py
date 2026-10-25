import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    total = 0
    for movie in movies:
        total = total + movie["rating"]
    average = total / len(movies)
    return round(average, 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 7:
        return "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015 and year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count = count + 1
    return count


def normalize_title(title):
    words = title.split(" ")
    new_words = []
    for word in words:
        new_word = word[0].upper() + word[1:]
        new_words.append(new_word)
    return " ".join(new_words)


def make_slug(title):
    slug = title.lower()
    slug = slug.replace(" ", "-")
    return slug


def format_report_line(movie):
    genres = sorted(movie["genres"])
    genres_text = ", ".join(genres)
    duration = duration_in_hours(movie["duration_min"])
    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    line = f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres_text}'
    return line


def movie_rating(movie):
    return movie["rating"]


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=movie_rating, reverse=True)
    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=movie_rating, reverse=True)
    top = []
    for movie in sorted_movies[:n]:
        pair = (movie["title"], movie["rating"])
        top.append(pair)
    return top


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    films = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in films:
                films[actor] = []
            films[actor].append(movie["title"])
    return films


average = average_rating(movies)
ratings_above_average = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average
}


def main():
    print("Hello from dz-catalog-analysis-damashova-m-26-555!")

    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(movies[index]["title"])
            break
        index = index + 1
    else:
        print("Шедевров не найдено")


if __name__ == "__main__":
    main()
