# Import the libs
import pandas as pd

# Make the filtre in the target rows
target_rows = ((~library_usage['provided_email_address']) &
               (library_usage['circulation_active_year'] == 2016) &
               (library_usage['notice_preference_definition'] == 'email'))
               
# Apply the filter and get the unique values
library_usage.loc[target_rows, 'home_library_code'].drop_duplicates()