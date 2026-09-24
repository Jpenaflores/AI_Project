# Crear un sistema de recomendación simple en Python usando datos de ejemplo

# Datos de ejemplo: usuarios y sus películas favoritas
users = {
    "Alice": ["Inception", "The Matrix", "Interstellar"],
    "Bob": ["The Godfather", "Pulp Fiction", "Goodfellas"],
    "Charlie": ["The Dark Knight", "Batman Begins", "Inception"]
}

# Función para recomendar películas basadas en las preferencias de otros usuarios
def recommend_movies(user, users_dict, num_recommendations=3):
    user_movies = set(users_dict.get(user, []))
    recommendations = {}

    for other_user, movies in users_dict.items():
        if other_user != user:
            for movie in movies:
                if movie not in user_movies:
                    recommendations[movie] = recommendations.get(movie, 0) + 1

    # Ordenar recomendaciones por cantidad de usuarios que las han visto
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    # Devolver las primeras N recomendaciones
    return [movie for movie, count in sorted_recommendations[:num_recommendations]] 

# Recomendar a Alice películas de usuarios que compartan al menos una película favorita con ella y que Alice aún no haya visto
def recommend_movies(user, users_dict):
    user_movies = set(users_dict.get(user, []))
    recommendations = set()

    for other_user, movies in users_dict.items():
        if other_user != user:
            shared_movies = user_movies.intersection(movies)

            if shared_movies:
                for movie in movies:
                    if movie not in user_movies:
                        recommendations.add(movie)

    return list(recommendations)

recommendations_for_alice = recommend_movies("Alice", users)
print("Recomendaciones para Alice:", recommendations_for_alice)
recommendation_system.py 
