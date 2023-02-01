SELECT 
    UNNEST(STRING_TO_ARRAY(categories, ';')) AS category,
    SUM(review_count) AS sum_review_count
FROM 
    yelp_business
GROUP BY
    category
ORDER BY 
    sum_review_count DESC