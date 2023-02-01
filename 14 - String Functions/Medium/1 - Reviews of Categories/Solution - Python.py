# Transform categories in array in table rows
yelp_business['category'] = yelp_business['categories'].str.split(';')
yelp_business = yelp_business.explode('category')

# Group by category and sum all reviews of with category
yelp_business = yelp_business.groupby(by='category', as_index=False)['review_count'].sum()

# Order by the greatest sum of reviews
yelp_business.sort_values(by='review_count', ascending=False)