import sqlite3


def get_timetable_by_group_title(title):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    id_group = cur.execute(
        f"SELECT id FROM groups WHERE title='{title}'"
    ).fetchone()[0]

    lessons = cur.execute(
        f"SELECT * FROM timetable WHERE id_group={id_group}"
    ).fetchall()

    # списочное выражение нам в помощь
    lessons = [
        [item[2], item[3], item[4], item[5]]
        for item in lessons
    ]

    result = [[0] * 8 for _ in range(6)]

    for element in lessons:
        id_subject = element[0]
        subject = cur.execute(
            f"SELECT title FROM subjects WHERE id={id_subject}"
        ).fetchone()[0]

        id_teacher = element[1]
        teacher = cur.execute(
            f"SELECT fullname FROM teachers WHERE id={id_teacher}"
        ).fetchone()[0]

        day = element[2]
        stream = element[3]
        result[day - 1][stream - 1] = (subject, teacher)

    return result


get_timetable_by_group_title('9-1')
