import media
import fresh_tomatoes

fellowship = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
    "https://images-na.ssl-images-amazon.com/images/I/51Qvs9i5a%2BL.jpg",
    "https://www.youtube.com/watch?v=V75dMMIW2B4")
two_towers = media.Movie("The Lord of the Rings: The Two Towers",
    "https://images-na.ssl-images-amazon.com/images/I/51uGVkvLkCL.jpg",
    "https://www.youtube.com/watch?v=LbfMDwc4azU")
return_of_the_king = media.Movie("The Lord of the Rings: The Return of the King",
    "https://images-na.ssl-images-amazon.com/images/I/71X6YzwV0gL._SY550_.jpg",
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")
dark_knight = media.Movie("The Dark Knight",
    "https://images-na.ssl-images-amazon.com/images/I/51WR0izzCRL.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")
interstellar = media.Movie("Interstellar",
    "http://img.moviepostershop.com/interstellar-movie-poster-2014-1020771206.jpg",
    "https://www.youtube.com/watch?v=3WzHXI5HizQ")
prestige = media.Movie("The Prestige",
    "https://movieposters2.com/images/634831-b.jpg",
    "https://www.youtube.com/watch?v=o4gHCmTQDVI")
valhalla = media.Movie("Valhalla Rising",
    "http://img.moviepostershop.com/valhalla-rising-movie-poster-2009-1010554869.jpg",
    "https://www.youtube.com/watch?v=dQgoGccHJD4")
babadook = media.Movie("The Babadook",
    "http://www.bloodyposters.com/wp-content/uploads/2014/09/the-babadook-afposter-580x850.jpg",
    "https://www.youtube.com/watch?v=k5WQZzDRVtw")

movies = [fellowship, two_towers, return_of_the_king, dark_knight, interstellar,
    prestige, valhalla, babadook]

fresh_tomatoes.open_movies_page(movies)
