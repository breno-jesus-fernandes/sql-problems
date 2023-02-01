police_cap_regex = '.*CAPTAIN.*POLICE.*|.*POLICE.*CAPTAIN.*'
police_captains_rows = sf_public_salaries['jobtitle'].str.contains(police_cap_regex, case=False, regex=True)
sf_public_salaries.loc[police_captains_rows][['employeename', 'basepay']]