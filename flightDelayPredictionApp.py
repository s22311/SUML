import streamlit as st
import make_pred
from datetime import datetime

dep_time_blk_mapping = {
    '00:01-05:59': 0, '06:00-06:59': 1, '07:00-07:59': 2, '08:00-08:59': 3, '09:00-09:59': 4, '10:00-10:59': 5,
    '11:00-11:59': 6, '12:00-12:59': 7,
    '13:00-13:59': 8, '14:00-14:59': 9, '15:00-15:59': 10, '16:00-16:59': 11, '17:00-17:59': 12, '18:00-18:59': 13,
    '19:00-19:59': 14,
    '20:00-20:59': 15, '21:00-21:59': 16, '22:00-22:59': 17, '23:00-23:59': 18
}

carrier_name_mapping = {
    'Alaska Airlines Inc.': 0, 'Allegiant Air': 1, 'American Airlines Inc.': 2, 'American Eagle Airlines Inc.': 3,
    'Atlantic Southeast Airlines': 4,
    'Comair Inc.': 5, 'Delta Air Lines Inc.': 6, 'Endeavor Air Inc.': 7, 'Frontier Airlines Inc.': 8,
    'Hawaiian Airlines Inc.': 9, 'JetBlue Airways': 10,
    'Mesa Airlines Inc.': 11, 'Midwest Airline, Inc.': 12, 'SkyWest Airlines Inc.': 13, 'Southwest Airlines Co.': 14,
    'Spirit Air Lines': 15,
    'United Air Lines Inc.': 16
}

departing_airport_mapping = {
    'Adams Field': 0, 'Albany International': 1, 'Albuquerque International Sunport': 2, 'Anchorage International': 3,
    'Atlanta Municipal': 4,
    'Austin - Bergstrom International': 5, 'Birmingham Airport': 6, 'Boise Air Terminal': 7, 'Bradley International': 8,
    'Charleston International': 9,
    'Chicago Midway International': 10, "Chicago O'Hare International": 11,
    'Cincinnati/Northern Kentucky International': 12, 'Cleveland-Hopkins International': 13,
    'Dallas Fort Worth Regional': 14, 'Dallas Love Field': 15, 'Des Moines Municipal': 16,
    'Detroit Metro Wayne County': 17, 'Douglas Municipal': 18,
    'El Paso International': 19, 'Eppley Airfield': 20, 'Fort Lauderdale-Hollywood International': 21,
    'Friendship International': 22, 'General Mitchell Field': 23,
    'Greater Buffalo International': 24, 'Greenville-Spartanburg': 25, 'Hollywood-Burbank Midpoint': 26,
    'Honolulu International': 27, 'Houston Intercontinental': 28,
    'Indianapolis Muni/Weir Cook': 29, 'Jacksonville International': 30, 'James M Cox/Dayton International': 31,
    'John F. Kennedy International': 32, 'Kahului Airport': 33,
    'Kansas City International': 34, 'Keahole': 35, 'Kent County': 36, 'LaGuardia': 37,
    'Lambert-St. Louis International': 38, 'Lihue Airport': 39, 'Logan International': 40,
    'Long Beach Daugherty Field': 41, 'Los Angeles International': 42, 'Louis Armstrong New Orleans International': 43,
    'McCarran International': 44, 'McGhee Tyson': 45,
    'Memphis International': 46, 'Metropolitan Oakland International': 47, 'Miami International': 48,
    'Minneapolis-St Paul International': 49, 'Myrtle Beach International': 50,
    'Nashville International': 51, 'Newark Liberty International': 52, 'Norfolk International': 53,
    'Northwest Arkansas Regional': 54, 'Ontario International': 55, 'Orange County': 56,
    'Orlando International': 57, 'Palm Beach International': 58, 'Palm Springs International': 59,
    'Pensacola Regional': 60, 'Philadelphia International': 61,
    'Phoenix Sky Harbor International': 62, 'Piedmont Triad International': 63, 'Pittsburgh International': 64,
    'Port Columbus International': 65, 'Portland International': 66,
    'Portland International Jetport': 67, 'Puerto Rico International': 68, 'Raleigh-Durham International': 69,
    'Reno/Tahoe International': 70, 'Richmond International': 71,
    'Rochester Monroe County': 72, 'Ronald Reagan Washington National': 73, 'Sacramento International': 74,
    'Salt Lake City International': 75, 'San Antonio International': 76,
    'San Diego International Lindbergh Fl': 77, 'San Francisco International': 78, 'San Jose International': 79,
    'Sanford NAS': 80, 'Savannah/Hilton Head International': 81,
    'Seattle International': 82, 'Southwest Florida International': 83, 'Spokane International': 84,
    'Standiford Field': 85, 'Stapleton International': 86,
    'Syracuse Hancock International': 87, 'Tampa International': 88, 'Theodore Francis Green State': 89,
    'Truax Field': 90, 'Tucson International': 91,
    'Tulsa International': 92, 'Washington Dulles International': 93, 'Will Rogers World': 94, 'William P Hobby': 95
}

st.title("Czy twój lot opóźni się conajmniej 15 min?")

date = st.date_input("Select a date", datetime.today())
month = date.month
day_of_week = date.weekday()

dep_time_blk = st.selectbox("Select Departure Time Block", list(dep_time_blk_mapping.keys()))
dep_time_blk_value = dep_time_blk_mapping[dep_time_blk]

# Dropdown for CARRIER_NAME
carrier_name = st.selectbox("Select Carrier Name", list(carrier_name_mapping.keys()))
carrier_name_value = carrier_name_mapping[carrier_name]

# Dropdown for DEPARTING_AIRPORT
departing_airport = st.selectbox("Select Departing Airport", list(departing_airport_mapping.keys()))
departing_airport_value = departing_airport_mapping[departing_airport]

short_flight = st.checkbox("Is this a short flight?")
# over 720 miles

snow = st.checkbox("Is it snowing?")

rain = st.checkbox("Is it raining?")

input_data = [
    month,
    day_of_week,
    dep_time_blk_value,
    carrier_name_value,
    departing_airport_value,
    short_flight,
    snow,
    rain
]

if st.button("Make Prediction"):
    prediction = make_pred.predict(input_data)
    st.write(f"The prediction is: {prediction}")
