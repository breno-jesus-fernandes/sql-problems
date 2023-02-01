-- Match just the rows with the patterns, ILIKE is insensitive
SELECT
    employeename,
    basepay
FROM
    sf_public_salaries
WHERE
    jobtitle ILIKE '%captain%police%' OR
    jobtitle ILIKE '%police%captain%'