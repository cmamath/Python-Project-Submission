# Python-Project-Submission
Explanation:
Import Libraries:

requests is used to make HTTP requests to fetch data from the TMDb API.
random is used to randomly select a movie for recommendation.

get_movies_by_genre Function:

Fetches the list of genres from TMDb to find the corresponding genre ID.
Uses the genre ID to fetch the list of movies for the given genre.
Extracts movie titles, ratings, and years from the fetched data.
Returns a list of movies.

recommend_movie Function:

Takes the list of movies and randomly selects one to recommend.
Returns a formatted string with the recommended movie's details.
main Function:

Prompts the user to input a genre.
Fetches movies of the specified genre.
Prints the recommended movie.
Not
