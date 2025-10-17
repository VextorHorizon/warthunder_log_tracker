from db import create_table, insert_session
from datetime import datetime

def main():
    create_table()
    print("War Thunder Session Logger\n")

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    vehicle = input("Vehicle: ")
    kills = int(input("Number of kills: "))
    deaths = int(input("Number of deaths: "))
    map_name = input("Map name: ")

    insert_session(date, vehicle, kills, deaths, map_name)
    print("\n ✅ Session logged successfully")

if __name__ == "__main__":
    main()