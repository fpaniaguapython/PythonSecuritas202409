import json

json_pelicula = '{"Title":"Indiana Jones and the Temple of Doom","Year":"1984","Rated":"PG","Released":"23 May 1984","Runtime":"118 min","Genre":"Action, Adventure","Director":"Steven Spielberg","Writer":"Willard Huyck, Gloria Katz, George Lucas","Actors":"Harrison Ford, Kate Capshaw, Ke Huy Quan","Plot":"In 1935, Indiana Jones is tasked by Indian villagers with reclaiming a rock stolen from them by a secret cult beneath the catacombs of an ancient palace.","Language":"English, Sinhala, Hindi","Country":"United States","Awards":"Won 1 Oscar. 11 wins & 22 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BYzgzMTIzNzctNmNiZC00ZDYyLWJjNzktMmQ2MDM2ZDkwZGVhXkEyXkFqcGdeQXVyMjM4MzQ4OTQ@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.5/10"},{"Source":"Rotten Tomatoes","Value":"77%"},{"Source":"Metacritic","Value":"57/100"}],"Metascore":"57","imdbRating":"7.5","imdbVotes":"540,216","imdbID":"tt0087469","Type":"movie","DVD":"N/A","BoxOffice":"$179,870,271","Production":"N/A","Website":"N/A","Response":"True"}'

pelicula = json.loads(json_pelicula)#Lectura y carga del contenido del string como objeto json
print(type(pelicula))#<class 'dict'>
print(pelicula['Title'])
print(pelicula['Ratings'][0]['Source'])
print(pelicula['Ratings'][0]['Value'])
