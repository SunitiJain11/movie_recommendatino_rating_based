#!/usr/bin/env python3
# import pandas library 
#coffiecient correlation- rating based on data

import pandas as pd 

# Get the data 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 

path = 'file.tsv'

df = pd.read_csv(path, sep='\t', names=column_names) 

# Check the head of the data 
df.head(9) 


# Check out all the movies and their respective IDs 
movie_titles = pd.read_csv('Movie_Id_Titles.csv') 
movie_titles.head() 

data = pd.merge(df, movie_titles, on='item_id') 
data.head() 

# Calculate mean rating of all movies 
rating=data.groupby('title')['rating'].mean().sort_values(ascending=False)
# Calculate count rating of all movies 
data.groupby('title')['rating'].count().sort_values(ascending=False).head() 

# creating dataframe with 'rating' count values 
ratings = pd.DataFrame(data.groupby('title')['rating'].mean()) 

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 

# Sorting values according to 
# the 'num of rating column' 
moviemat = data.pivot_table(index ='user_id', 
			columns ='title', values ='rating') 

moviemat.head() 

ratings.sort_values('num of ratings', ascending = False).head(10) 

# analysing correlation with similar movies 
starwars_user_ratings = moviemat['Star Wars (1977)'] 


starwars_user_ratings.head() 

# analysing correlation with similar movies
#store userwse ratings 
similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
#apply 
corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 

# Similar movies like starwars 
corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 

corr_starwars.head() 
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head(20) 

##########for batman
liarliar_user_ratings = moviemat['Batman (1989)'] 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 
corr_starwars = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 

# Similar movies like starwars 
corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 

corr_starwars.head() 
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head(20) 

