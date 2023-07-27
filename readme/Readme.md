Movie Recommendation System :

In this project , we use two datasets :
Movie : Containing Details about movie budget, runtime ,production house
Credits : Containing Details about Crew : Director , Cast

We filter the genre ,  keywords , overview (Synopsis) , cast , crew , runtime ,language ,concatenate them to form a superset and use Porter Stemmer to revert words to root form 
for each individual movie which is processed in Training Model , based on number of matched unique words by comparing each movie , we find the closest ones which match most features and recommend
the list to the user . 
By Default , it returns unique movie ids of 5 most matched movies . Next , creating an API from the TMDB database , we fetch the movie posters
and movie title ,and use Streamlit module of Python to create frontend for the user . 
Lastly , Streamlit Community Cloud is used to host the code on the cloud .

Working Link : https://movie-recommendation-system-3pzppfuoeczedrrb3gfjbv.streamlit.app/

Dataset Models link, and necessary api links are stored in Credentials.txt file.
