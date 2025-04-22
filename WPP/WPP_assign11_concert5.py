import pandas as pd
import numpy as np

def concert_count_per_artist_venue():
   
    num_concerts = int(input("Enter the number of concerts: "))

    artists = []
    venues = []
    dates = []
    
    for i in range(num_concerts):
        artist = input(f"Enter the artist for concert {i+1}: ").strip()
        venue = input(f"Enter the venue for concert {i+1}: ").strip()
        date = input(f"Enter the date of concert {i+1} (YYYY-MM-DD): ").strip()
        
        artists.append(artist)
        venues.append(venue)
        dates.append(date)
    
    df = pd.DataFrame({
        'artist': artists,
        'venue': venues,
        'date': pd.to_datetime(dates)  
    })
  
    df['year_month'] = df['date'].dt.to_period('M')  # This will give 'YYYY-MM' format
    
    concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='concert_count')
   
    pivot_table = concert_counts.pivot_table(
        index='year_month', 
        columns=['artist', 'venue'], 
        values='concert_count', 
        aggfunc='sum', 
        fill_value=0  # Fill missing values with 0
    )

    print("\nWide table with concert counts per (artist, venue) per year-month:")
    print(pivot_table)

concert_count_per_artist_venue()
