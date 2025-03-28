import sqlite3, json
from re import sub
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ast import literal_eval

# Database functions class
class DataBase:
    def __init__(self, db_name: str, table_name: str, titles: dict[str, str]) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self.titles = titles
        self.types = {
                    "INTEGER":   lambda x: int(x),
                    "BOOLEAN":   lambda x: bool(x),
                    "INTEGER[]": lambda x: [int(el) for el in literal_eval(sub(r"{(.*?)}", r"[\1]", x))],
                    "BOOLEAN[]": lambda x: [bool(el) for el in literal_eval(sub(r"{(.*?)}", r"[\1]", x))],
                    "TEXT[]":    lambda x: [json.loads(el) for el in literal_eval(sub(r"^{(.*?)}$", r"[\1]", x))],
                    "DATETIME":  lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"), 
                    "CHAR":      lambda x: str(x),
                    "TEXT":      lambda x: str(x)
                    }
    
    # Database creation function
    def create(self) -> None:
        conn = sqlite3.connect(self.db_name); cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({',\n'.join(f"{key} {value}" for key, value in self.titles.items())})")
        conn.close()
        
    # Function of insert or update data
    def insert_or_update_data(self, record_id: str, values: dict[str, list[bool|int]|bool|int|str]) -> None:
        conn = sqlite3.connect(self.db_name); cursor = conn.cursor()
        
        placeholders = ', '.join(['?'] * (len(self.titles)))
        
        sql = f"REPLACE INTO {self.table_name} ({', '.join(list(self.titles.keys()))}) VALUES ({placeholders})"
        cursor.execute(sql, [record_id] + [ sub(r"^\[(.*?)\]$", r'{\1}', str([json.dumps(el) if type(el)==dict else int(el) for el in val ])) if type(val)==list else val for val in values.values() ])
        
        conn.commit(); conn.close()

    # Function for load data in dictionary
    def load_data_from_db(self) -> dict[str, dict[str, list[bool|int]|bool|int|str]]:
        loaded_data = dict(); conn = sqlite3.connect(self.db_name); cursor = conn.cursor()
        cursor.execute(f"SELECT {', '.join(list(self.titles.keys()))} FROM {self.table_name}")
        rows = cursor.fetchall()
        for row in rows:
            id = row[0]; loaded_data[id] = dict()
            for i, (key, value) in enumerate(list(self.titles.items())[1:], 1):
                loaded_data[id][key] = self.types[value](row[i])
        conn.close()
        return loaded_data

# Database visualization
if __name__ == "__main__":
    base = DataBase(db_name="UsersData.db", table_name="users_data_table", titles={"id": "TEXT PRIMARY KEY", "text": "INTEGER[]",
                        "sessions_messages": "TEXT[]", "some": "BOOLEAN",
                        "images": "CHAR", "free" : "BOOLEAN", "basic" : "BOOLEAN",
                        "pro" : "BOOLEAN", "incoming_tokens": "INTEGER", "outgoing_tokens" : "INTEGER",
                        "free_requests" : "INTEGER", "datetime_sub": "DATETIME", "promocode": "BOOLEAN", "ref": "TEXT"})
    base.create(); db = base.load_data_from_db(); N = 8
    uid = input()
    if uid != '':
        if "pro" in uid:
            db[uid.split()[0]] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": True, "pro": True, "incoming_tokens": 1.7*10**5, "outgoing_tokens": 5*10**5, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(months=1), "promocode": False, "ref": ""}
        elif 'admin' in uid:
            db[uid.split()[0]] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": True, "pro": True, "incoming_tokens": 100*10**5, "outgoing_tokens": 100*10**5, "free_requests": 1000, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(years=5), "promocode": False, "ref": ""}
        else:
            db[uid] = {"text": [0]*N, "sessions_messages": [], "some": False, "images": "", "free": False, "basic": False, "pro": False, "incoming_tokens": 0, "outgoing_tokens": 0, "free_requests": 10, "datetime_sub": datetime.now().replace(microsecond=0)+relativedelta(days=1), "promocode": False, "ref": ""}
        base.insert_or_update_data(uid.split()[0], db[uid.split()[0]])