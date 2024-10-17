import streamlit as st
from database import Task, Habit, session
import pandas as pd
import plotly.express as px
import datetime
from transformers import pipeline

# The following lines were used for debugging purposes and can be removed

#import logging
#logging.basicConfig(level=logging.INFO)

#import lxml
#print(lxml.__version__)

#import bs4
#print(bs4.builder.builder_registry.builders)

@st.cache_resource   # Cache the summarizer model to improve performance
def load_summarizer():
    # Load the text summarization pipeline using the TS-small model
    return pipeline("summarization", model="t5-small")

summarizer = load_summarizer() # Initialize the summarizer

def main():
    st.title("AI-Enhanced Personal Productivity Assistant") # Set the app title

    menu = ["Add Task", "View Tasks", "Update Task", "Delete Task", "Add Habit", "View Habits", "Analytics", "NLP Tools"]
    choice = st.sidebar.selectbox("Menu", menu) # Create a sidebar menu for navigation

    if choice == "Add Task":
        st.subheader("Add a New Task")  # Subheader for the "Add Task" section
        title = st.text_input("Title")  # Input field for task title
        description = st.text_area("Description")   # Text area for task description
        due_date = st.date_input("Due Date", datetime.date.today()) # Date picker for due date

        if st.button("Add Task"):   # When the "Add Task" button is clicked
            # Create a new Task object with the provided details
            task = Task(
                title=title,
                description=description,
                due_date=datetime.datetime.combine(due_date, datetime.datetime.min.time())
            )
            session.add(task)       # Add the task to the database session
            session.commit()         # Commit the session to save the task in the database
            st.success(f"Task '{title}' added successfully.")   # Display success message

    elif choice == "View Tasks":
        st.subheader("All Tasks")   # Subheader for the "View Tasks" section
        tasks = session.query(Task).all()   # Retrieve all tasks from the database
        for task in tasks:
            # Display each task's details
            st.write(f"**{task.title}** - Due: {task.due_date.strftime('%Y-%m-%d')}")
            st.write(f"Description: {task.description}")
            st.write(f"Completed: {'Yes' if task.completed else 'No'}")
            st.write("---") # Separator line

    elif choice == "Update Task":
        st.subheader("Update Task Status")  # Subheader for the "Update Task" section
        task_titles = [task.title for task in session.query(Task).all()]    # List of task titles
        selected_task = st.selectbox("Select Task", task_titles)    # Dropdown to select a task
        if selected_task:
            task = session.query(Task).filter_by(title=selected_task).first()   # Get the selected task
            new_status = st.selectbox("Completed", [True, False], index=int(task.completed))    # Select new status
            if st.button("Update Status"):   # When the "Update Status" button is clicked
                task.completed = new_status  # Update the task's completion status
                session.commit()    # Commit the changes to the database
                st.success(f"Task '{task.title}' updated.") # Display success message

    elif choice == "Delete Task":
        st.subheader("Delete a Task")    # Subheader for the "Delete Task" section
        task_titles = [task.title for task in session.query(Task).all()]    # List of task titles
        selected_task = st.selectbox("Select Task to Delete", task_titles)  # Dropdown to select a task to delete
        if st.button("Delete Task"):    # When the "Delete Task" button is clicked
            task = session.query(Task).filter_by(title=selected_task).first()   # Get the selected task
            session.delete(task)    # Delete the task from the session
            session.commit()    # Commit the changes to the database
            st.success(f"Task '{selected_task}' deleted.")  # Display success message
    
    elif choice == "Add Habit":
        st.subheader("Add a New Habit") # Subheader for the "Add Habit" section
        name = st.text_input("Habit Name")  # Input field for habit name
        frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])   # Dropdown for habit frequency
        if st.button("Add Habit"):   # When the "Add Habit" button is clicked
            # Create a new Habit object with the provided details
            habit = Habit(name=name, frequency=frequency, last_logged=datetime.datetime.now())
            session.add(habit)  # Add the habit to the database session
            session.commit()    # Commit the session to save the habit in the database
            st.success(f"Habit '{name}' added.")    # Display success message

    elif choice == "View Habits":
        st.subheader("Your Habits") # Subheader for the "View Habits" section
        habits = session.query(Habit).all() # Retrieve all habits from the database
        for habit in habits:
            # Display each habit's details
            st.write(f"**{habit.name}** - Frequency: {habit.frequency}")
            st.write(f"Last Logged: {habit.last_logged.strftime('%Y-%m-%d %H:%M:%S')}")
            if st.button(f"Log '{habit.name}'"):        # Button to log the habit
                habit.last_logged = datetime.datetime.now() # Update the last logged time
                session.commit()                        # Commit the changes to the database
                st.success(f"Habit '{habit.name}' logged at {habit.last_logged}.")      # Display success message
            st.write("---")                             # Separator line        

    elif choice == "Analytics":
        st.subheader("Productivity Analytics")          # Subheader for the "Analytics" section

        # Task Completion Rate
        tasks = session.query(Task).all()               # Retrieve all tasks
        if tasks:
            # Create a DataFrame from tasks data               
            df_tasks = pd.DataFrame([{
                'Title': task.title,
                'Completed': task.completed
            } for task in tasks])

            completion_rate = df_tasks['Completed'].mean() * 100    # Calculate completion rate
            st.write(f"**Task Completion Rate:** {completion_rate:.2f}%")   # Display completion rate

            # Create a pie chart for task completion
            fig = px.pie(df_tasks, names='Completed', title='Tasks Completed vs Incomplete')
            st.plotly_chart(fig)    # Display the pie chart
        else:
            st.write("No tasks to analyze.")    # Message if there are no tasks

        # Habit Logging Frequency
        habits = session.query(Habit).all()     # Retrieve all habits
        if habits:
            # Create a DataFrame from habits data
            df_habits = pd.DataFrame([{
                'Name': habit.name,
                'Last Logged': habit.last_logged
            } for habit in habits])
            # Calculate days since each habit was last logged
            df_habits['Days Since Last Logged'] = (datetime.datetime.now() - df_habits['Last Logged']).dt.days

            st.write("**Habits Logging Overview:**")    # Display overview text
            st.table(df_habits[['Name', 'Days Since Last Logged']]) # Display the data in a table

            # Create a bar chart for habit logging frequency
            fig = px.bar(df_habits, x='Name', y='Days Since Last Logged', title='Days Since Each Habit Was Last Logged')
            st.plotly_chart(fig)    # Display the bar chart
        else:
            st.write("No habits to analyze.")   # Message if there are no habits

    elif choice == "NLP Tools":
        st.subheader("Natural Language Processing Tools")   # Subheader for the "NLP Tools" sectio

        # Dropdown to select an NLP task
        nlp_option = st.selectbox("Choose an NLP Task", ["Text Summarization", "Sentiment Analysis", "Fetch and Summarize News"])

        if nlp_option == "Text Summarization":
            st.write("Enter the text you want to summarize:")   # Prompt for text input
            text = st.text_area("Input Text")                   # Text area for input text
            if st.button("Summarize"):                          # When the "Summarize" button is clicked
                if text:
                    if len(text.split()) > 500:
                        st.warning("Please enter text with fewer than 500 words.")  # Warn if text is too long
                    else:
                        with st.spinner('Summarizing...'):      # Display a spinner while processing
                            try:
                                summary = summarizer(text, max_length=130, min_length=30, do_sample=False)  # Generate summary
                                st.write("**Summary:**")
                                st.write(summary[0]['summary_text'])    # Display the summary
                            except Exception as e:
                                st.error(f"An error occurred during summarization: {e}")    # Display error message
                else:
                    st.warning("Please enter text to summarize.")   # Warn if no text is entered

        elif nlp_option == "Sentiment Analysis":
            st.write("Enter the text you want to analyze:")     # Prompt for text input
            text = st.text_area("Input Text")                   # Text area for input text
            if st.button("Analyze"):                            # When the "Analyze" button is clicked
                if text:
                    from transformers import pipeline   # Import pipeline for sentiment analysis
                    sentiment_analyzer = pipeline("sentiment-analysis")  # Initialize sentiment analyzer
                    sentiment = sentiment_analyzer(text)     # Perform sentiment analysis
                    st.write("**Sentiment Analysis Result:**")
                    st.write(sentiment) # Display the analysis result
                else:
                    st.warning("Please enter text to analyze.")   # Warn if no text is entered

        elif nlp_option == "Fetch and Summarize News":
            st.write("Enter a topic to search for news articles:")  # Prompt for topic input
            topic = st.text_input("Topic")  # Input field for the topic
            if st.button("Fetch News"): # When the "Fetch News" button is clicked
                if topic:
                    try:
                        import requests # Import requests for HTTP requests
                        from bs4 import BeautifulSoup   # Import BeautifulSoup for parsing HTML/XML


                        # Build the RSS feed URL based on the topic
                        rss_url = f"https://news.google.com/rss/search?q={topic}"
                        response = requests.get(rss_url)    # Fetch the RSS feed
                        response.raise_for_status()  # Raise an exception for HTTP errors & bad responses

                        # Parse the RSS feed using lxml-xml parser
                        soup = BeautifulSoup(response.content, "lxml-xml")  # specify using the lxml parser

                        articles = soup.findAll('item') # Find all articles in the feed

                        if articles:
                            st.write(f"**Top news articles for '{topic}':**")
                            for article in articles[:5]:    # Display the top 5 articles
                                title = article.title.text  # Get the article title
                                link = article.link.text    # Get the article link
                                st.write(f"**{title}**")    # Display the title
                                st.write(f"[Read more]({link})")    # Provide a link to the article
                                st.write("---")             # Separator line
                        else:
                            st.info("No articles found for this topic.")     # Inform if no articles are found
                    except requests.exceptions.RequestException as e:
                        st.error(f"An error occurred while fetching news: {e}") # Display request error
                    except Exception as e:
                        st.error(f"An error occurred: {e}")     # Display any other errors
                else:
                    st.warning("Please enter a topic.") # Warn if no topic is entered

        
if __name__ == "__main__":
    main()      # Execute the main function when the script is run directly
