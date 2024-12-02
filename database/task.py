
def scan():
    conn = get_db()
    coursor = conn.execute("SELECT * FROM task",())
    result = cursor fetchall()
    cursor.close()
    return output_formatter(result)

def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT  * FROM task WHERE ID=?",(task_id,))
    result = cursor.fetch()
    cursor.close()
    if result:
        return cutput_formatter(result)[0]
    return {}


def insert {task_datta}:
    statement = ""
        INSERT INTO task[
            sumary,
            descrption
        ] VALUES (?,?)
    ""

    task_tuple = {
        task_data.get("summary"),
        task_data.get("description")
    }
    conn = get_db()
    conn.execute(statement,task_tuple)
    conn.commit()

def update_by_id(task_data, tasl_id):
    statement = ""
        UPDATE  task SET 
            summary = ?,
            description = ?,
            is_done = ?
        WHERE id = ?
    ""
    task_tuple = {
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_id
    }
    conn = get_db()
    conn.execute(statement,task_tuple)
    conn.commit()