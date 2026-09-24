# Crear un sistema de recomendación simple en Python usando datos de ejemplo

# Datos de ejemplo: usuarios y sus películas favoritas
users = {
    "Alice": ["Inception", "The Matrix", "Interstellar"],
    "Bob": ["The Godfather", "Pulp Fiction", "Goodfellas"],
    "Charlie": ["The Dark Knight", "Batman Begins", "Inception"]
}

# Función para encontrar películas similares a las favoritas de un usuario
def find_similar_movies(user, users_dict):
    user_movies = users_dict.get(user, [])
    similar_movies = []
    
    for other_user, movies in users_dict.items():
        if other_user != user:
            for movie in movies:
                if movie in user_movies and movie not in similar_movies:
                    similar_movies.append(movie)
    
    return similar_movies

# Ejemplo de uso
user = "Alice"
similar = find_similar_movies(user, users)
print(f"Películas similares a las favoritas de {user}: {similar}")

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


recommendations = recommend_movies("Alice", users)
print(f"Recomendaciones para Alice: {recommendations}")

