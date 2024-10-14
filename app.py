from flask import Flask, render_template, redirect, url_for, request, session, flash
from pymongo import MongoClient
import bcrypt
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient('mongodb://localhost:27017/')
db = client['Library_database']
users = db['users']
books = db['books']
members = db['members']
borrow_records = db['borrow_records']

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = username
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert_one({'username': username, 'password': hashed})
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        books.insert_one({'title': title, 'author': author, 'isbn': isbn})
        return redirect(url_for('book_list'))
    return render_template('add_book.html')

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        membership_id = request.form['membership_id']
        members.insert_one({'name': name, 'email': email, 'membership_id': membership_id})
        return redirect(url_for('member_list'))
    return render_template('add_member.html')

@app.route('/book_list')
def book_list():
    if 'username' not in session:
        return redirect(url_for('login'))
    books_list = books.find()
    return render_template('book_list.html', books=books_list)

@app.route('/member_list')
def member_list():
    if 'username' not in session:
        return redirect(url_for('login'))
    members_list = members.find()
    return render_template('member_list.html', members=members_list)

@app.route('/update_book/<id>', methods=['GET', 'POST'])
def update_book(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    book = books.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form.get('isbn')
        if isbn:
            books.update_one({'_id': ObjectId(id)}, {'$set': {'title': title, 'author': author, 'isbn': isbn}})
            return redirect(url_for('book_list'))
        else:
            flash('ISBN is required to update the book.')
            return render_template('update_book.html', book=book)
    return render_template('update_book.html', book=book)

@app.route('/delete_book/<id>', methods=['GET', 'POST'])
def delete_book(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    books.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('book_list'))

@app.route('/update_member/<id>', methods=['GET', 'POST'])
def update_member(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    member = members.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        membership_id = request.form['membership_id']
        members.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email, 'membership_id': membership_id}})
        return redirect(url_for('member_list'))
    return render_template('update_member.html', member=member)

@app.route('/delete_member/<id>', methods=['GET', 'POST'])
def delete_member(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    members.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('member_list'))

@app.route('/borrow_book', methods=['GET', 'POST'])
def borrow_book():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        isbn = request.form['isbn']
        membership_id = request.form['membership_id']
        book = books.find_one({'isbn': isbn})
        member = members.find_one({'membership_id': membership_id})
        if book and member:
            borrow_records.insert_one({
                'isbn': book['isbn'],
                'title': book['title'],
                'author': book['author'],
                'member_name': member['name'],
                'membership_id': member['membership_id']
            })
            return redirect(url_for('borrow_list'))
        else:
            flash('Invalid ISBN or Membership ID')
    return render_template('borrow_book.html')

@app.route('/borrow_list')
def borrow_list():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Fetch borrow records from the collection
    borrow_list_entries = list(borrow_records.find())
    
    return render_template('borrow_list.html', borrow_list=borrow_list_entries)

if __name__ == '__main__':
    app.run(debug=True)
