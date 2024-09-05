#!/usr/bin/python3

import sqlite3

from myProject import db
from myProject.models import Cat


def add_cat(name, color, eye_color, age, gender, image_path):
    # Create a connection to the existing database
    connection = sqlite3.connect("instance/database.db")
    cursor = connection.cursor()

    # Insert a new record into the cats table
    cursor.execute(
        """
        INSERT INTO cats (name, color, eye_color, age, gender, image)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (name, color, eye_color, age, gender, image_path),
    )

    # Commit changes and close the connection
    connection.commit()
    connection.close()


if __name__ == "__main__":
    # Example data to add to the database
    cats_data = [
        ("Snowball", "Orange", "Green", 1, "Female", "1.jpg"),
        ("Bella", "White", "Blue", 0.5, "Female", "2.jpg"),
        ("Ola", "White", "Blue", 1, "Female", "3.jpg"),
        ("Lune", "Grey", "Blue", 1, "Male", "5.jpg"),
        ("Simba", "Mix", "Green", 1, "Male", "6.jpg"),
        ("Daisy", "Grey", "Yellow", 2, "Female", "7.jpg"),
        ("Charlie", "Mix", "Green", 2, "Male", "8.jpg"),
        ("Chloe", "Grey", "Yellow", 0.5, "Female", "9.jpg"),
        ("Max", "Black", "Green", 1, "Male", "10.jpg"),
        ("Lucy", "Grey", "Yellow", 1, "Male", "11.jpg"),
        ("Leo", "Black", "Green", 2, "Male", "12.jpg"),
        ("Mia", "Mix", "Green", 1, "Female", "13.jpg"),
        ("Jasper", "Mix", "Green", 2, "Male", "14.jpg"),
        ("Willow", "White", "Yellow", 1, "Male", "15.jpg"),
        ("Milo", "Mix", "Yellow", 2, "Female", "16.jpg"),
        ("Sophie", "Brown", "Green", 1, "Male", "17.jpg"),
        ("Tiger", "Grey", "Green", 1, "Male", "18.jpg"),
        ("Zoe", "Brown", "Blue", 0.5, "Female", "19.jpg"),
        ("Cleo", "Orange", "Blue", 2, "Male", "20.jpg"),
        ("Felix", "Brown", "Green", 2, "Female", "21.jpg"),
        ("Lily", "Mix", "Grey", 0.5, "Female", "22.jpg"),
        ("Oscar", "Grey", "Yellow", 1, "Male", "23.jpg"),
        ("Zalta", "Orange", "Green", 1, "Female", "25.jpg"),
        ("Sammy", "Black", "Yellow", 1, "Female", "26.jpg"),
        ("Felix", "Orange", "Green", 2, "Male", "27.jpg"),
        ("Ginger", "White", "Grey", 2, "Female", "28.jpg"),
        ("Trumb", "Mix", "Green", 1, "Male", "29.jpg"),
        ("Pepper", "Grey", "Grey", 0.5, "Female", "30.jpg"),
        ("Gizmo", "White", "Yellow", 2, "Male", "31.jpg"),
        ("Peanut", "Mix", "Yellow", 2, "Female", "32.jpg"),
        ("Obama", "White", "Blue", 1, "Male", "33.jpg"),
        ("Shadow", "Orange", "Yellow", 0.5, "Male", "34.jpg"),
        ("Oliver", "White", "Blue", 1, "Male", "35.jpg"),
    ]

    # Add each cat to the database
    for cat in cats_data:
        add_cat(*cat)

    print("Cat data added successfully.")
