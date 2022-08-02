import csv
import os


def read_notes(file_name):
    """Returns list of notes"""
    with open(file_name) as file:
        reader = csv.reader(file)
        headers = next(reader)
        return list(reader)


def add_note(file_name, data):
    """add note to csv file, check rating value and film name value"""
    if not isinstance(data[-1], (int, float)):
        raise AttributeError('rating must be string or float')
    elif not 1 <= data[-1] <= 5:
        raise AttributeError('rating must be string in diapason [1,5]')

    if not os.path.exists(file_name) or os.stat(file_name).st_size == 0:
        colums_name = ['film_name', 'note', 'rating']
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(colums_name)
    if any((data[0] == item[0] for item in read_notes(file_name))):
        raise AttributeError('film name must be unique')
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def remove_note(file_name, film_name):
    '''remove note by film_name'''
    with open(file_name) as file:
        reader = csv.reader(file)
        new_csv = []
        for row in reader:
            if row[0] != film_name:
                new_csv.append(row)
    os.remove(file_name)
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in new_csv:
            writer.writerow(row)


def print_notes(file_name):
    """print notes to console"""
    with open(file_name) as file:
        reader = csv.DictReader(file)
        # headers = next(reader)
        for row in reader:
            print(f"Film name: {row['film_name']}, note: {row['note']}, rating: {row['rating']}")


def get_film_with_highest_rating(file_name):
    """return films with the highest rating value"""
    with open(file_name) as file:
        reader = list(csv.DictReader(file))

    m = max(reader, key=lambda x: x['rating'])
    highest_rating_films = []
    for row in reader:
        if row['rating'] == m['rating']:
            highest_rating_films.append(list(row.values()))
    return highest_rating_films


def get_films_with_lowest_rating(file_name):
    """return films with the lowest rating value"""
    with open(file_name) as file:
        reader = list(csv.DictReader(file))

    m = min(reader, key=lambda x: x['rating'])
    highest_rating_films = []
    for row in reader:
        if row['rating'] == m['rating']:
            highest_rating_films.append(list(row.values()))
    return highest_rating_films


def get_average_rating_films(file_name):
    """return average films rating"""
    with open(file_name) as file:
        reader = list(csv.DictReader(file))
        s = 0
        for row in reader:
            s += int(row['rating'])
    return s / len(reader)


