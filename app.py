import streamlit as st

st.title("Portfolio of Degmar Barbosa")

st.markdown("""
### Name: Degmar Barbosa
**Profession:** DBA and Programmer

#### Primary Areas of Expertise:
- Database Administration
- Database Architecture
- Performance Tuning
- Backup Strategies
- Advanced Techniques using T-SQL

#### Interests:
- Relational Database Design using:
  - MSSQL Server
  - MySQL 8.0
  - PostgreSQL 12.0

#### Programming Skills:
- **Web Development:** NODE.JS, NEXT.JS, KNEX.JS, EXPRESS.JS, CSS3, HTML5, JAVASCRIPT
- **Scripting:** SHELLSCRIPT, PYTHON3, AWK (text-file manipulation)
- **Data Analysis:** PANDAS, Streamlit
- **Systems Programming:** C, C++ (NEW), RUST, Golang
- **Operating Systems:** Linux 20.04-Bash

#### Development Tools:
- Pycharm
- Visual Studio Code
- Code::Blocks
""")


# Set page title and favicon
#st.set_page_config(page_title="Programming Languages Showcase", page_icon=":snake:")

# Title of the page
#st.title("Programming Languages Showcase")

# Introduction
#st.write("""
#    Welcome to the Programming Languages Showcase! Here you'll find examples of various programming languages, including C++, Rust, Python, SQL, and Go. Explore the code snippets and get inspired!
#""")

# Sections for each programming language
languages = {
    "Python": "A versatile high-level programming language.",
    "Pandas": "A versatile high-level library for Python",
    "Streamlit": "A versatile high-level library for Python",
    "C ": "A powerful language with performance in mind.",
    "C++": "A powerful language with performance in mind.",
    "Rust": "A systems programming language focused on safety and concurrency.",
    "SQL": "A language designed for managing data in relational databases.",

}

# List of image filenames corresponding to each language
images = [
    "y1.jpg",
    "y2.jpg",
    "y3.jpg",
    "y4.jpg",
    "y5.jpg",
    "y6.jpg",
    "y7.jpg",
]

# Loop through languages and display content
for index, (lang, description) in enumerate(languages.items(), start=1):
    st.header(f"{index}. {lang}")
    st.write(description)
    st.image(f"images/{images[index - 1]}")
    st.code(f"# See Functions in {lang}")
    # You can add example functions for each language here

# Footer
st.write("---")
st.write("Created with Streamlit, HTML5, CSS3, and Tkinter.")
