# Movie Recommendation System

Welcome to the Movie Recommendation System! This simple yet powerful application uses content-based filtering to suggest movies based on your favorite genres. Built with Flask, this system offers a web interface and a RESTful API to interact with movie recommendations easily.

## Quick Start

Follow these steps to get up and running with the Movie Recommendation System:

### Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### Set Up Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Set Up the Database

Initialize the SQLite database:

```bash
python scripts/database_setup.py
```

### Run the Application

Start the Flask application:

```bash
python run.py
```

Navigate to [http://localhost:5000](http://localhost:5000) in your browser to start using the app.

## Features

- **Content-Based Movie Recommendations:** Get tailored movie suggestions based on your genre preferences.
- **Web Interface:** User-friendly interface for easy interaction with the recommendation system.
- **SQLite Database:** Efficient storage of movie and rating data.
- **RESTful API:** Access recommendations programmatically.

## How to Use

1. **Enter a Genre:** Use the web interface to input your preferred genre.
2. **Get Recommendations:** Click the "Get Recommendations" button to view a list of suggested movies.

## API Usage

Retrieve movie recommendations via the RESTful API:

### Endpoint

**GET** `/recommendations?genre={genre}&n={number}`

- **Parameters:**
  - `genre`: The genre for which you want recommendations (e.g., `action`, `comedy`).
  - `n`: The number of recommendations to return.

- **Example Request:**

  ```bash
  curl "http://localhost:5000/recommendations?genre=action&n=5"
  ```

## Project Structure

Here's an overview of the project structure:

```
movie_recommendation_system/
├── app/
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── services/        # Recommendation logic
│   └── utils/           # Utility functions
├── config/              # Configuration files
├── data/                # Data files
├── scripts/             # Setup and utility scripts
├── static/              # Static files (CSS, JS)
├── templates/           # HTML templates
└── tests/               # Test cases
```

## Contributing

We welcome contributions to improve the Movie Recommendation System. Here’s how you can contribute:

1. **Fork the Repository**
2. **Create a New Branch**
3. **Make Your Changes**
4. **Commit Your Changes**
5. **Push and Create a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Questions?

Feel free to reach out:

**Your Name**  
[youremail@example.com](mailto:youremail@example.com)

---
