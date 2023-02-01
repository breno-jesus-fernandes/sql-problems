-- Select utils columns and transform all jobtitles to be faster to compare with one of the patterns
WITH police_captain_salaries AS (
    SELECT
        employeename,
        basepay,
        lower(jobtitle) AS jobtitle
    FROM
        sf_public_salaries

)
-- Match just the rows with the patterns
SELECT
    employeename,
    basepay
FROM
    police_captain_salaries
WHERE
    jobtitle LIKE '%captain%police%' OR
    jobtitle LIKE '%police%captain%'