# Book Recommender System

## Overview
The **Book Recommender System** is a web-based application built using **Streamlit**. It provides personalized book recommendations based on collaborative filtering and also displays the most popular books on the home page.

![image](https://github.com/user-attachments/assets/7b5aa93f-60e0-4e59-b8a3-ab008f8155b5)
![image](https://github.com/user-attachments/assets/c40bbcc8-e888-4bcd-95ac-c677c71d88dd)


## Features
- **Home Page:** Displays the most popular books based on overall ratings.
- **Collaborative Filtering:** Recommends books based on user preferences using **cosine similarity**.
- **User-Based Filtering:** Considers only **intelligent users** (users with more than 200 ratings) and books rated by at least **50 users**.
- **Interactive UI:** Built using **Streamlit** for an easy and intuitive experience.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-recommender.git
   cd book-recommender
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. View the **most popular books** on the home page.
3. Enter a **book name** and specify the number of recommendations.
4. The system suggests similar books based on **collaborative filtering**.

## How It Works
### Popularity-Based Recommendations (Home Page)
- Books with the highest ratings are displayed on the home page.
- Used to provide trending and highly rated books to users.

### Collaborative Filtering (User-Based)
1. Filters users who have rated more than **200 books** (intelligent users).
2. Filters books that have been rated by at least **50 users**.
3. Creates a **pivot table** (users as rows, books as columns, ratings as values).
4. Uses **cosine similarity** to find books that are highly rated by similar users.
5. Returns top book recommendations based on user input.

## Dependencies
- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Numpy

## Contributing
Feel free to fork the repository and submit pull requests to enhance the recommendation system.

## License
This project is licensed under the MIT License.

