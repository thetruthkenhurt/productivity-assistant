# AI-Enhanced Personal Productivity Assistant

Welcome to the **AI-Enhanced Personal Productivity Assistant**! This is a Streamlit-based web application designed to help you manage tasks and habits efficiently while leveraging AI-powered Natural Language Processing (NLP) tools. The app integrates task and habit tracking with advanced features like text summarization, sentiment analysis, and news fetching.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the App](#running-the-app)
  - [Navigating the App](#navigating-the-app)
- [Technologies Used](#technologies-used)
- [Planned Improvements](#planned-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

### Task Management

- **Add Task**: Create new tasks with a title, description, and due date.
- **View Tasks**: Display all tasks with their details and completion status.
- **Update Task**: Update the completion status of existing tasks.
- **Delete Task**: Remove tasks from your task list.

### Habit Tracking

- **Add Habit**: Create new habits with a name and frequency (Daily, Weekly, Monthly).
- **View Habits**: Display all habits and log them to track progress.
- **Habit Logging**: Update the last logged time for habits to monitor consistency.

### Productivity Analytics

- **Task Completion Rate**: Visualize your task completion rate with a pie chart.
- **Habit Logging Frequency**: Analyze how frequently you're logging habits with bar charts and tables.

### Natural Language Processing Tools

- **Text Summarization**: Summarize long pieces of text using AI-powered models.
- **Sentiment Analysis**: Determine the sentiment (Positive/Negative) of the input text.
- **Fetch and Summarize News**: Retrieve the latest news articles on a topic of your choice.

---

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **Git** (for cloning the repository)
- **Virtual Environment** (recommended)

### Clone the Repository

```bash
git clone https://github.com/YourUsername/productivity-assistant.git
cd productivity-assistant
```

### Create and Activate a Virtual Environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Install Dependencies**
```bash
pip install -r requirements.txt
``` 

---

## Usage

### Running the app
**Ensure your virtual environment is activated and run: **
```bash
streamlit run app.py
```
This will start the app, and you can access it in your web browser at `http://localhost:8501`.

### Navigating the App

- **Sidebar Menu**: Use the sidebar to navigate between different sections:
  - **Add Task**
  - **View Tasks**
  - **Update Task**
  - **Delete Task**
  - **Add Habit**
  - **View Habits**
  - **Analytics**
  - **NLP Tools**

#### 1. Task Management

- **Add Task**: Input the task title, description, and due date, then click **"Add Task"**.
- **View Tasks**: See all your tasks listed with their details.
- **Update Task**: Change the completion status of a selected task.
- **Delete Task**: Remove a task from your list.

#### 2. Habit Tracking

- **Add Habit**: Enter the habit name and select the frequency.
- **View Habits**: View your habits and log them by clicking **"Log [Habit Name]"**.

#### 3. Analytics

- **Task Completion Rate**: Visual representation of completed vs. incomplete tasks.
- **Habit Logging Frequency**: Bar chart showing days since each habit was last logged.

#### 4. NLP Tools

- **Text Summarization**:
  - Enter the text you want to summarize.
  - Click **"Summarize"** to get a concise summary.
- **Sentiment Analysis**:
  - Input the text to analyze.
  - Click **"Analyze"** to see the sentiment result.
- **Fetch and Summarize News**:
  - Enter a topic to search for.
  - Click **"Fetch News"** to retrieve top news articles.

---

## Technologies Used

- **Python 3.7+**
- **Streamlit**: For building the web application interface.
- **SQLAlchemy**: For database operations.
- **Pandas**: For data manipulation.
- **Plotly Express**: For creating interactive charts.
- **Transformers (Hugging Face)**: For NLP tasks like text summarization and sentiment analysis.
- **BeautifulSoup**: For web scraping news articles.
- **Requests**: For handling HTTP requests.

---

## Planned Improvements

We are continually working to enhance the functionality and user experience of the **AI-Enhanced Personal Productivity Assistant**. Here are some features we're planning to implement:

### 1. Notifications and Reminders

- **Email Notifications**: Send email reminders for upcoming due tasks or habits that need logging.
- **In-App Alerts**: Real-time alerts within the app for due tasks and habit reminders.

### 2. Enhanced Task Tracking

- **Dashboard Overview**: A comprehensive dashboard displaying all tasks, habits, and analytics in one place.
- **Customizable Views**: Filter and sort tasks/habits based on categories, due dates, or completion status.
- **Calendar Integration**: Visual calendar to view tasks and habits scheduled over time.

### 3. Advanced Analytics

- **Progress Over Time**: Line charts showing productivity trends over weeks or months.
- **Goal Setting**: Set and track goals for task completion and habit consistency.
- **Comparative Analysis**: Compare productivity metrics across different periods.

### 4. Additional NLP Tools

- **Language Translation**: Translate text between different languages.
- **Keyword Extraction**: Identify key themes or topics within a text.
- **Text Classification**: Categorize text into predefined classes.

### 5. User Authentication

- **Account Creation**: Allow users to create accounts to save and access their data from anywhere.
- **Data Security**: Implement authentication protocols to secure user data.

### 6. Mobile Responsiveness

- **Responsive Design**: Optimize the app layout for mobile devices.
- **Progressive Web App (PWA)**: Enable installation of the app on mobile home screens.

---

## Contributing

We welcome contributions from the community! If you'd like to contribute:

1. **Fork the Repository**

   Click the **"Fork"** button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/YourUsername/productivity-assistant.git
   ```

3. **Create a Branch**
   ```
   git checkout -b feature/YourFeatureName
   ```

4. **Make your Changes**

	Implement your feature or fix.
	
5. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add Your Feature"
   git push origin feature/YourFeatureName
   ```

6. Submit a Pull Request
   Go to your forked repository and click on "New Pull Request".

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author**: Kenneth Goh 
- **Email**: kennethgjs@gmail.com
- **GitHub**: [thetruthkenhurt](https://github.com/thetruthkenhurt)

Feel free to reach out if you have any questions or suggestions!

---

**Thank you for using the AI-Enhanced Personal Productivity Assistant! We hope it helps you achieve greater productivity and organization in your daily life.**
