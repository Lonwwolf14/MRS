# Movie Recommendation System

This is a simple movie recommendation system built with Flask and SQLite. It uses content-based filtering to recommend movies based on genre similarity.

## Features

- Content-based movie recommendations
- Simple web interface for user interaction
- SQLite database for storing movie and user rating data
- RESTful API endpoint for getting recommendations

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Setup

Follow these steps to get your development environment set up:

1. Clone the repository:

2. Create a virtual environment:


3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install dependencies:

5. Set up the database:

6. Run the application:

## Usage

1. Open your web browser and visit `http://localhost:5000`.
2. Enter a user ID in the input field (use 1 or 2 for the sample data).
3. Click "Get Recommendations" to see movie recommendations for that user.

## API Usage

You can also get recommendations programmatically using the API:

Example:

This will return a JSON array of recommended movies for user 1, with a maximum of 5 recommendations.

## Project Structure

- `app/`: Main application package
  - `models/`: Database models
  - `routes/`: API route definitions
  - `services/`: Business logic, including recommendation algorithm
  - `utils/`: Utility functions, including database operations
- `config/`: Configuration files
- `data/`: Directory to store the SQLite database
- `scripts/`: Utility scripts, including database setup
- `static/`: Static files for the frontend
- `templates/`: HTML templates for the frontend
- `tests/`: Unit and integration tests

## Running Tests

To run the test suite, use the following command:

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Create a new Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please contact:

Your Name - youremail@example.com

Project Link: https://github.com/yourusername/movie-recommendation-system



