from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, contact_details) VALUES (%s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id

def select_all():
    manufacturers = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['contact_details'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(row['name'], row['contact_details'], row['id'])
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, contact_details) = (%s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.contact_details, manufacturer.id]
    run_sql(sql, values)