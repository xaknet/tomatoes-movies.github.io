import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
print(avatar.storyline)
#avatar.show_trailer()


guardians = media.Movie("Guardians of the Galaxy",
                        "Guardians of the Galaxy is a 2014 American superhero film based on the Marvel Comics",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",
                        "https://www.youtube.com/watch?v=crIaEzXgqto")
#guardians.show_trailer()

movies = [toy_story, avatar, guardians]

fresh_tomatoes.open_movies_page(movies)
