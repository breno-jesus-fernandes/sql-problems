SELECT 
    DISTINCT home_library_code
FROM
    library_usage
WHERE
    NOT provided_email_address AND
    circulation_active_year = 2016 AND
    notice_preference_definition = 'email'