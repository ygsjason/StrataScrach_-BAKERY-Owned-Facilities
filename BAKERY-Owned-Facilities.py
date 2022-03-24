# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections

df1 = df[(df['owner_name'].str.lower().str.find('baker') >= 0 ) & (df['pe_description'].str.lower().str.find('low risk') >= 0 )]
