import pandas as pd

def add_days_til_party():
    party_schedule = []
    
    for i in range(10):
        party = input(f"Will there be a party on day {i + 1} (yes/no)? ").strip().lower()
       
        if party == 'yes':
            party_schedule.append(True)
        else:
            party_schedule.append(False)

    df = pd.DataFrame({
        'day': range(1, 11),
        'party': party_schedule
    })

    days_til_party = [None] * len(df)  
    
    next_party_day = None  
    for i in range(len(df)-1, -1, -1):  # Loop backwards from the last day
        if df.loc[i, 'party']:  # If there is a party on the current day
            next_party_day = i
            days_til_party[i] = 0
        elif next_party_day is not None:
            days_til_party[i] = next_party_day - i

    df['days_til_party'] = days_til_party

    print("\nSchedule with 'days_til_party':")
    print(df)

add_days_til_party()
