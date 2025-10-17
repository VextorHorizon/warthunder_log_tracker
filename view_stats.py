from db import connect_db

def view_all_sessions():
    with connect_db() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM sessions ORDER BY id DESC")
        rows = c.fetchall()

        if not rows:
            print("Have no data!")
            return
        
        print("War Thunder Session History\n")
        for row in rows:
            id, date, vehicle, kills, deaths, map_name = row
            print(f"[{id}]| {date} | {vehicle} | Kills: {kills} Deaths: {deaths} | {map_name}")

if __name__ == "__main__":
    view_all_sessions()