# Cat Store Web App

A web application that allows users to browse and reserve cats based on various filters such as color, age, eye color, and gender. Users can log in, register, and reserve a cat, which will be ready for pickup at the store. The app is built using Python and Flask for the backend, with a responsive design powered by Bootstrap for the frontend.

## Features

-   **User Authentication:** Users can register, log in, and view or edit their profiles.
-   **Cat Gallery:** Browse cats with filters for color, age, eye color, and gender.
-   **Reservation System:** Reserve a cat, with a confirmation page that provides details about the reservation.
-   **Pagination:** Gallery page includes server-side pagination for easy browsing.
-   **Responsive Design:** Mobile-friendly layout with clean and professional UI.

## Technologies Used

-   **Backend:** Python, Flask, Flask-Login, SQLAlchemy
-   **Frontend:** HTML, CSS, Bootstrap
-   **Database:** SQLite (or mention another if you’ve used something else)
-   **Version Control:** Git, GitHub

## Setup Instructions

-   **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cat-store.git
    cd cat-store
    ```
-   **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
-   **Run the application:**
    ```bash
    flask run
    ```

## Screenshots

Include screenshots of the following:

-   **Login Page**
-   **Cat Gallery Page**
-   **Reservation Confirmation Page**

## Folder Structure

```bash
├── static
│   ├── css
│   └── images
├── templates
│   ├── base.html
│   ├── gallery.html
│   ├── confirm.html
├── models.py
├── auth/
│   └── gallery.py
├── app.py
├── README.md
└── requirements.txt
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any feature requests or bug reports.

## License

Mention the license (e.g., MIT License) if applicable.
