#!/usr/bin/python3

import sqlite3

from theProject import db
from theProject.models import Cat


def add_cat(name, color, eye_color, age, gender, price, image_path):
    # Create a connection to the existing database
    connection = sqlite3.connect("instance/database.db")
    cursor = connection.cursor()

    # Insert a new record into the cats table
    cursor.execute(
        """
        INSERT INTO cats (name, color, eye_color, age, gender, price, image)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (name, color, eye_color, age, gender, price, image_path),
    )

    # Commit changes and close the connection
    connection.commit()
    connection.close()


if __name__ == "__main__":
    # Example data to add to the database
    cats_data = [
        ("Snowball", "Orange", "Green", "adult", "Female", "150", "1.jpg"),
        ("Bella", "White", "Blue", "kitten", "Female", "200", "2.jpg"),
        ("Ola", "White", "Blue", "adult", "Female", "170", "3.jpg"),
        ("Lune", "Grey", "Blue", "adult", "Male", "180", "5.jpg"),
        ("Simba", "Mix", "Green", "adult", "Male", "160", "6.jpg"),
        ("Daisy", "Grey", "Yellow", "senior", "Female", "140", "7.jpg"),
        ("Charlie", "Mix", "Green", "senior", "Male", "130", "8.jpg"),
        ("Chloe", "Grey", "Yellow", "kitten", "Female", "210", "9.jpg"),
        ("Max", "Black", "Green", "adult", "Male", "170", "10.jpg"),
        ("Lucy", "Grey", "Yellow", "adult", "Male", "175", "11.jpg"),
        ("Leo", "Black", "Green", "senior", "Male", "120", "12.jpg"),
        ("Mia", "Mix", "Green", "adult", "Female", "160", "13.jpg"),
        ("Jasper", "Mix", "Green", "senior", "Male", "135", "14.jpg"),
        ("Willow", "White", "Yellow", "adult", "Male", "180", "15.jpg"),
        ("Milo", "Mix", "Yellow", "senior", "Female", "125", "16.jpg"),
        ("Sophie", "Brown", "Green", "adult", "Male", "165", "17.jpg"),
        ("Tiger", "Grey", "Green", "adult", "Male", "170", "18.jpg"),
        ("Zoe", "Brown", "Blue", "kitten", "Female", "220", "19.jpg"),
        ("Cleo", "Orange", "Blue", "senior", "Male", "110", "20.jpg"),
        ("Felix", "Brown", "Green", "senior", "Female", "130", "21.jpg"),
        ("Lily", "Mix", "Grey", "kitten", "Female", "200", "22.jpg"),
        ("Oscar", "Grey", "Yellow", "adult", "Male", "180", "23.jpg"),
        ("Zalta", "Orange", "Green", "adult", "Female", "170", "25.jpg"),
        ("Sammy", "Black", "Yellow", "adult", "Female", "160", "26.jpg"),
        ("Felix", "Orange", "Green", "senior", "Male", "120", "27.jpg"),
        ("Ginger", "White", "Grey", "senior", "Female", "130", "28.jpg"),
        ("Trumb", "Mix", "Green", "adult", "Male", "175", "29.jpg"),
        ("Pepper", "Grey", "Grey", "kitten", "Female", "190", "30.jpg"),
        ("Gizmo", "White", "Yellow", "senior", "Male", "110", "31.jpg"),
        ("Peanut", "Mix", "Yellow", "senior", "Female", "130", "32.jpg"),
        ("Obama", "White", "Blue", "adult", "Male", "180", "33.jpg"),
        ("Shadow", "Orange", "Yellow", "kitten", "Male", "210", "34.jpg"),
        ("Oliver", "White", "Blue", "adult", "Male", "180", "35.jpg"),
    ]

    # Add each cat to the database
    for cat in cats_data:
        add_cat(*cat)

    print("Cat data added successfully.")
