from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def select_all():
    manufacturers = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['contact_details'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers