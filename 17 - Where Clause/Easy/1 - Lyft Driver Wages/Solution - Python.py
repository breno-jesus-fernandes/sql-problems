target_rows = (lyft_drivers['yearly_salary'] <= 30_000) | (lyft_drivers['yearly_salary'] >= 70_000)

lyft_drivers[target_rows]

