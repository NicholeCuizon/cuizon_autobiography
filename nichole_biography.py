import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title('Autobiography of Nichole Cuizon')

# Display Picture
st.image('FormalPic1.jpg', caption='Nichole Cuizon', use_column_width=True)

# Introduction
st.header('Introduction')
st.write("""
Hello! My name is Nichole Cuizon. I am a 4th-year student pursuing a Bachelor of Science in Information Technology at the Cebu Institute of Technology - University. My journey in technology and problem-solving has been driven by a deep curiosity and a passion for innovation. I am excited to share my experiences and the milestones I have achieved along the way.
""")

# Early Life and Education
with st.expander('Early Life and Education'):
    st.write("""
    I was born and raised in Liloan, Cebu, Philippines. Initially, my interests lay in the medical field, with a particular focus on pharmacology. However, due to unforeseen life circumstances, my path took an unexpected turn towards Information Technology.

    Over time, and with the guidance of inspiring instructors, I developed a deep fascination with technology and its power to address real-world challenges. This newfound passion led me to fully embrace my studies in IT. As a result, I have had the opportunity to explore a wide range of areas within the field, including coding, software development, project management, and user experience design.
    """)

# Academic and Professional Achievements
st.header('Academic and Professional Achievements')
st.write("""
Throughout my academic career, I have been involved in several significant projects that have helped shape my skills and understanding of technology. The most recent one is:

- **Mastermind Web App**: A comprehensive web application developed using the Django framework. Mastermind is designed to enhance the studying experience with features such as:
  - **Quiz Management**: Allows users to create and review quizzes, track progress, and improve performance.
  - **Notes Organization**: Enables seamless creation and management of study notes, accessible anytime and anywhere.
  - **Coding Practice**: Provides an integrated code editor for practicing languages such as C, C++, and Python.
  - **Peer Collaboration**: Supports real-time chat, group discussions, and collaborative study projects.

This project has been particularly rewarding, as it integrates various aspects of my learning and provides a valuable tool for students.
""")

# Skills and Interests
st.header('Skills and Interests')
st.write("""
Beyond my academic and project work, I have developed a strong skill set in:

- **Programming Languages**: Proficient in Python, Java, JavaScript, and C/C++.
- **Web Technologies**: Experienced with HTML, CSS, and various JavaScript frameworks.
- **Database Management**: Knowledgeable in SQL and database design.

In addition to my technical skills, I am passionate about continuous learning and personal growth. I enjoy exploring new technologies and staying updated with industry trends.
""")

# Personal Interests
with st.expander('Personal Interests'):
    st.write("""
    Outside of my professional life, I have a variety of interests that help me balance my work and personal life:

    - **Watching TV Shows and Movies**: I am an avid viewer of Netflix, enjoying a wide range of genres from sci-fi to drama.
    - **Reading Books**: I love diving into both fiction and non-fiction, with a particular interest in science fiction and technology.
    - **Playing the Guitar**: Music is a big part of my life, and I find joy in playing the guitar and exploring different musical styles.
    """)

# Future Aspirations
st.header('Future Aspirations')
st.write("""
Looking ahead, I aim to continue expanding my knowledge and expertise in technology, particularly in software development and data science. I am excited about the opportunities that lie ahead and am eager to contribute to innovative projects that make a positive impact on society.
""")

# Add a link to contact or LinkedIn profile
st.sidebar.header('Connect with Me')
st.sidebar.write("Feel free to reach out or connect with me through email:")
st.sidebar.markdown("[Email](mailto:nichole.cuizon.work@gmail.com)")

# Optionally add more interactivity
st.sidebar.header('Additional Resources')
st.sidebar.write("Here are some useful links:")
st.sidebar.markdown("[GitHub Portfolio](https://github.com/NicholeCuizon)")
st.sidebar.markdown("[Personal Blog](https://yourblog.com)")

# Interactive section: Skill Proficiency Chart
st.header('Skill Proficiency')
skills = {
    'Python': 90,
    'Java': 80,
    'JavaScript': 75,
    'C/C++': 70,
    'HTML/CSS': 85,
}

skills_df = pd.DataFrame(list(skills.items()), columns=['Skill', 'Proficiency'])
fig, ax = plt.subplots()
skills_df.plot(kind='bar', x='Skill', y='Proficiency', ax=ax, color='skyblue', legend=False)
ax.set_ylabel('Proficiency (%)')
ax.set_title('Skill Proficiency Chart')

st.pyplot(fig)

# Interactive section: Coding Practice Stats
st.header('Coding Practice Stats')
practice_options = st.selectbox('Choose a programming language:', ['Python', 'Java', 'JavaScript', 'C/C++'])

# Dummy data for visualization
np.random.seed(0)
days = np.arange(1, 31)
practice_hours = np.random.normal(loc=2, scale=0.5, size=30)  # Example data

fig, ax = plt.subplots()
ax.plot(days, practice_hours, marker='o', linestyle='-', color='orange')
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Hours Practiced')
ax.set_title(f'Coding Practice Hours in {practice_options}')

st.pyplot(fig)
