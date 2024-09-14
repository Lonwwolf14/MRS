# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**! 🍿 This powerful application leverages content-based filtering to recommend movies based on your preferred genres. Built with Flask, it offers a smooth web interface and a RESTful API for easy interaction with personalized movie recommendations.

## 🚀 Quick Start

Follow these simple steps to set up and run the application:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
python scripts/database_setup.py
```

### 5. Run the Application

```bash
python run.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser to start exploring!

---

## ✨ Features

- 🎯 **Smart Recommendations**: Get personalized movie suggestions based on your favorite genres.
- 🖥️ **Intuitive Web Interface**: A user-friendly platform for seamless interaction.
- 📊 **Efficient Data Storage**: Utilizes an SQLite database for fast access to movie and rating data.
- 🔗 **Developer-Friendly API**: Easily access recommendations programmatically.

---

## 🎮 How to Use

- **Choose Your Genre**: Enter your preferred genre through the web interface.
- **Discover Movies**: Click "Get Recommendations" to view a curated list of suggested films.

---

### Parameters:

- `genre`: The genre of movies you are interested in (e.g., action, comedy).
- `n`: The number of recommendations you want to receive.

### Example Request:

```bash
curl "http://localhost:5000/recommendations?genre=action&n=5"
```

---

## 📚 Dataset

This application uses **The Movies Dataset** from Kaggle, which provides rich metadata to enhance the accuracy of movie recommendations.

---

## 📁 Project Structure

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

---

## 🤝 Contributing

We welcome contributions! Here's how you can get involved:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Commit your changes.
5. Push to your fork and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 📬 Questions?

Feel free to reach out to:

**Your Name**  
[youremail@example.com](mailto:youremail@example.com)

---

Happy movie discovering! 🎥🍿
