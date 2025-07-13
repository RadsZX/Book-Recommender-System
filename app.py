from flask import Flask,render_template
import pickle
  
final_df = pickle.load(open('popular_df.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                           book_name=list(final_df['Book-Title'].values),
                           author=list(final_df['Book-Author'].values),
                           image=list(final_df['Image-URL-M'].values),
                           ratings=list(final_df['Avg Ratings'].values),
                           no_of_ratings=list(final_df['No. of Ratings'].values)
                           )
    
@app.route('/recommend')

def recommend():
    return render_template('recommend.html',
                           book_name=list(final_df['Book-Title'].values),
                           author=list(final_df['Book-Author'].values),
                           image=list(final_df['Image-URL-M'].values),
                           ratings=list(final_df['Avg Ratings'].values),
                           no_of_ratings=list(final_df['No. of Ratings'].values)
                           )
    
    
@app.route('/about')
def about():        
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)   