# 📚 Python Portfolio Projects

A collection of Python projects organized by difficulty level to showcase programming skills and build a strong GitHub portfolio.

## 🎯 Overview

This portfolio contains progressively challenging Python projects designed to demonstrate various skills including:
- Basic Python syntax and control structures
- Object-Oriented Programming (OOP)
- Web scraping and API integration
- File handling and automation
- Web development with Flask
- Data analysis and visualization

## 📁 Project Structure

```
portfolio/
│
├── beginner-projects/
│   ├── calculator/          # Simple calculator application
│   ├── guessing-game/       # Number guessing game with CLI
│   └── todo-list/          # Command-line task manager
│
├── intermediate-projects/
│   ├── news-scraper/       # Web scraper for news headlines
│   ├── weather-api/        # Weather data API client
│   └── file-organizer/     # Automated file organization tool
│
├── advanced-projects/
│   ├── flask-webapp/       # Web application with Flask
│   └── data-analysis/      # Data analysis and visualization
│
├── README.md              # This file
└── requirements.txt       # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-portfolio.git
   cd python-portfolio
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Projects Overview

### 🟢 Beginner Level Projects

#### 1. Simple Calculator
- **Description**: Basic calculator with arithmetic operations
- **Skills**: Basic Python, user input handling, conditional statements
- **Run**: `python calculator.py`

#### 2. Number Guessing Game
- **Description**: Interactive CLI game to guess random numbers
- **Skills**: Random module, loops, exception handling
- **Run**: `python guessing_game.py`

#### 3. CLI To-Do List
- **Description**: Task management system with add/remove/complete features
- **Skills**: OOP, list manipulation, user interface design
- **Run**: `python todo_list.py`

### 🟡 Intermediate Level Projects

#### 4. News Web Scraper
- **Description**: Extracts news headlines from websites
- **Skills**: Web scraping, BeautifulSoup, HTTP requests
- **Dependencies**: `requests`, `beautifulsoup4`
- **Run**: `python news_scraper.py`

#### 5. Weather API Client
- **Description**: Fetches and displays weather data from OpenWeatherMap API
- **Skills**: API integration, JSON handling, error management
- **Setup**: Requires API key from [OpenWeatherMap](https://openweathermap.org/api)
- **Run**: `python weather_client.py`

#### 6. File Organizer
- **Description**: Automatically categorizes files by type into folders
- **Skills**: File system operations, path manipulation, automation
- **Run**: `python file_organizer.py`

### 🔴 Advanced Level Projects

#### 7. Flask Web Application
- **Description**: Web-based calculator with REST API
- **Skills**: Web development, Flask framework, REST APIs
- **Dependencies**: `flask`
- **Run**: `python app.py`
- **Access**: http://localhost:5000

#### 8. Data Analysis Project
- **Description**: Analyzes datasets with statistical methods and visualizations
- **Skills**: Data manipulation, pandas, matplotlib, seaborn
- **Dependencies**: `pandas`, `matplotlib`, `seaborn`
- **Run**: `python data_analysis.py`

## 🛠️ Technologies Used

- **Core Python**: Standard library, OOP principles
- **Web Development**: Flask, REST APIs
- **Data Processing**: pandas, NumPy
- **Data Visualization**: matplotlib, seaborn
- **Web Scraping**: BeautifulSoup, requests
- **File Handling**: os, shutil, pathlib

## 📦 Dependencies

All required packages are listed in `requirements.txt`:

```txt
requests==2.31.0
beautifulsoup4==4.12.2
flask==2.3.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 🎯 Learning Objectives

- **Foundation**: Master Python syntax and basic programming concepts
- **OOP**: Implement object-oriented design patterns
- **APIs**: Work with external services and web APIs
- **Automation**: Create scripts for practical tasks
- **Web Development**: Build full-stack applications
- **Data Science**: Perform data analysis and visualization

## 📝 Usage Notes

1. **API Keys**: Some projects require API keys (e.g., Weather API)
2. **Virtual Environment**: Recommended to avoid dependency conflicts
3. **File Paths**: Update directory paths in file organizer as needed
4. **Web Scraping**: Respect websites' terms of service and robots.txt

## 🤝 Contributing

Feel free to fork this repository and add your own projects! When contributing:

1. Follow the existing project structure
2. Maintain clean, well-commented code
3. Include proper documentation
4. Add tests if possible

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/your-username/python-portfolio](https://github.com/your-username/python-portfolio)

---

**⭐ Don't forget to star this repository if you find it helpful!**

---

## 🚀 Next Steps

1. Complete projects in order of difficulty
2. Customize and enhance each project
3. Add your own unique features
4. Deploy web applications to platforms like Heroku or PythonAnywhere
5. Continue learning with more advanced topics like:
   - Machine Learning with scikit-learn
   - Web frameworks like Django
   - Database integration
   - Testing with pytest

Happy coding! 🐍