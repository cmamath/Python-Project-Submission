import requests
import random

def get_movies_by_genre(genre, api_key):
    # Get the list of genres from TMDb to find the corresponding genre ID
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genre_response = requests.get(genre_url)
    genres = genre_response.json().get('genres', [])

    genre_id = None
    for g in genres:
        if g['name'].lower() == genre:
            genre_id = g['id']
            break

    if genre_id is None:
        return []

    # Get the list of movies for the given genre
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    results = response.json().get('results', [])

    movies = []
    for movie in results:
        title = movie.get('title')
        rating = movie.get('vote_average')
        year = movie.get('release_date', '')[:4]

        movies.append({
            'title': title,
            'rating': rating,
            'year': year
        })

    return movies

def recommend_movie(movies):
    if not movies:
        return "No movies found for the given genre."
    
    recommended_movie = random.choice(movies)
    return f"Recommended Movie: {recommended_movie['title']} ({recommended_movie['year']}) with rating {recommended_movie['rating']}"

def main():
    api_key = "82a3ccb79549099fc99a1f3fdf1dd485"  # Replace with your TMDb API key
    genre = input("Enter the genre: ").strip().lower()
    movies = get_movies_by_genre(genre, api_key)
    recommendation = recommend_movie(movies)
    print(recommendation)

if __name__ == "__main__":
    main()
