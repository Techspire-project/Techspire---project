from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'techspire_secret_2024'

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'techspire@2024'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    # Project Orders
    c.execute('''CREATE TABLE IF NOT EXISTS project_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, teammates TEXT, department TEXT,
        guide_name TEXT, project_topic TEXT, email TEXT, whatsapp TEXT, doc_pages INTEGER,
        front_page_name TEXT, heading_font INTEGER, subheading_font INTEGER, para_font INTEGER,
        language TEXT, expected_budget TEXT, total_amount REAL DEFAULT 0, advance_amount REAL DEFAULT 0,
        advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # Flex Orders
    c.execute('''CREATE TABLE IF NOT EXISTS flex_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, whatsapp TEXT, purpose TEXT,
        content_details TEXT, required_size TEXT, total_amount REAL DEFAULT 0,
        advance_amount REAL DEFAULT 0, advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # Invitation Orders
    c.execute('''CREATE TABLE IF NOT EXISTS invitation_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, whatsapp TEXT, purpose TEXT,
        content_details TEXT, font_style TEXT, font_size TEXT, total_amount REAL DEFAULT 0,
        advance_amount REAL DEFAULT 0, advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # PPT Orders
    c.execute('''CREATE TABLE IF NOT EXISTS ppt_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, department TEXT, whatsapp TEXT,
        purpose TEXT, total_slides INTEGER, topic TEXT, total_amount REAL DEFAULT 0,
        advance_amount REAL DEFAULT 0, advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # Paper Orders
    c.execute('''CREATE TABLE IF NOT EXISTS paper_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, department TEXT, whatsapp TEXT,
        topic TEXT, num_pages INTEGER, total_amount REAL DEFAULT 0, advance_amount REAL DEFAULT 0,
        advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # Report Orders
    c.execute('''CREATE TABLE IF NOT EXISTS report_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, department TEXT, whatsapp TEXT,
        report_headings TEXT, num_pages INTEGER, total_amount REAL DEFAULT 0,
        advance_amount REAL DEFAULT 0, advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # Article Orders
    c.execute('''CREATE TABLE IF NOT EXISTS article_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, whatsapp TEXT, topic TEXT,
        num_pages INTEGER, font_style TEXT, total_amount REAL DEFAULT 0, advance_amount REAL DEFAULT 0,
        advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    # Website Orders
    c.execute('''CREATE TABLE IF NOT EXISTS website_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, whatsapp TEXT, website_type TEXT,
        num_pages INTEGER, technology TEXT, total_amount REAL DEFAULT 0, advance_amount REAL DEFAULT 0,
        advance_paid INTEGER DEFAULT 0, full_payment_paid INTEGER DEFAULT 0,
        payment_method TEXT DEFAULT '', delivery_status TEXT DEFAULT 'Request Submitted',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

# ---- PUBLIC ROUTES ----
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service/project', methods=['GET','POST'])
def project_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('''INSERT INTO project_orders (name,teammates,department,guide_name,project_topic,
            email,whatsapp,doc_pages,front_page_name,heading_font,subheading_font,para_font,language,expected_budget)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
            (d['name'],d['teammates'],d['department'],d['guide_name'],d.get('project_topic',''),
             d['email'],d['whatsapp'],d['doc_pages'],d['front_page_name'],d['heading_font'],
             d['subheading_font'],d['para_font'],d['language'],d['expected_budget']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Project Order', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('project_form.html')

@app.route('/service/flex', methods=['GET','POST'])
def flex_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO flex_orders (name,whatsapp,purpose,content_details,required_size) VALUES (?,?,?,?,?)',
            (d['name'],d['whatsapp'],d['purpose'],d['content_details'],d['required_size']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Flex Design', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('flex_form.html')

@app.route('/service/invitation', methods=['GET','POST'])
def invitation_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO invitation_orders (name,whatsapp,purpose,content_details,font_style,font_size) VALUES (?,?,?,?,?,?)',
            (d['name'],d['whatsapp'],d['purpose'],d['content_details'],d['font_style'],d['font_size']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Invitation/Poster/GIF', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('invitation_form.html')

@app.route('/service/ppt', methods=['GET','POST'])
def ppt_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO ppt_orders (name,department,whatsapp,purpose,total_slides,topic) VALUES (?,?,?,?,?,?)',
            (d['name'],d['department'],d['whatsapp'],d['purpose'],d['total_slides'],d.get('topic','')))
        conn.commit(); conn.close()
        return render_template('success.html', service='PPT Creation', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('ppt_form.html')

@app.route('/service/paper', methods=['GET','POST'])
def paper_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO paper_orders (name,department,whatsapp,topic,num_pages) VALUES (?,?,?,?,?)',
            (d['name'],d['department'],d['whatsapp'],d['topic'],d['num_pages']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Paper Presentation', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('paper_form.html')

@app.route('/service/report', methods=['GET','POST'])
def report_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO report_orders (name,department,whatsapp,report_headings,num_pages) VALUES (?,?,?,?,?)',
            (d['name'],d['department'],d['whatsapp'],d['report_headings'],d['num_pages']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Report Writing', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('report_form.html')

@app.route('/service/article', methods=['GET','POST'])
def article_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO article_orders (name,whatsapp,topic,num_pages,font_style) VALUES (?,?,?,?,?)',
            (d['name'],d['whatsapp'],d['topic'],d['num_pages'],d['font_style']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Article Writing', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('article_form.html')

@app.route('/service/website', methods=['GET','POST'])
def website_form():
    if request.method == 'POST':
        d = request.form
        conn = get_db()
        conn.execute('INSERT INTO website_orders (name,whatsapp,website_type,num_pages,technology) VALUES (?,?,?,?,?)',
            (d['name'],d['whatsapp'],d['website_type'],d['num_pages'],d['technology']))
        conn.commit(); conn.close()
        return render_template('success.html', service='Website Development', name=d['name'], whatsapp=d['whatsapp'])
    return render_template('website_form.html')

# ---- ADMIN ROUTES ----
@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        if request.form['username']==ADMIN_USERNAME and request.form['password']==ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
        flash('Invalid credentials')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('admin_login'))

def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/admin')
@admin_required
def admin_dashboard():
    conn = get_db()
    stats = {}
    tables = ['project_orders','flex_orders','invitation_orders','ppt_orders',
              'paper_orders','report_orders','article_orders','website_orders']
    all_orders = []
    for t in tables:
        rows = conn.execute(f'SELECT *, "{t}" as table_name FROM {t} ORDER BY created_at DESC LIMIT 5').fetchall()
        stats[t] = conn.execute(f'SELECT COUNT(*) as cnt FROM {t}').fetchone()['cnt']
        for r in rows:
            all_orders.append(dict(r))
    conn.close()
    all_orders.sort(key=lambda x: x.get('created_at',''), reverse=True)
    return render_template('admin_dashboard.html', stats=stats, recent_orders=all_orders[:20])

@app.route('/admin/orders/<table>')
@admin_required
def admin_orders(table):
    valid = ['project_orders','flex_orders','invitation_orders','ppt_orders',
             'paper_orders','report_orders','article_orders','website_orders']
    if table not in valid:
        return redirect(url_for('admin_dashboard'))
    conn = get_db()
    orders = conn.execute(f'SELECT * FROM {table} ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('admin_orders.html', orders=orders, table=table)

@app.route('/admin/update/<table>/<int:order_id>', methods=['POST'])
@admin_required
def admin_update(table, order_id):
    valid = ['project_orders','flex_orders','invitation_orders','ppt_orders',
             'paper_orders','report_orders','article_orders','website_orders']
    if table not in valid:
        return redirect(url_for('admin_dashboard'))
    d = request.form
    conn = get_db()
    conn.execute(f'''UPDATE {table} SET total_amount=?, advance_amount=?, advance_paid=?,
        full_payment_paid=?, payment_method=?, delivery_status=? WHERE id=?''',
        (d.get('total_amount',0), d.get('advance_amount',0),
         1 if d.get('advance_paid') else 0,
         1 if d.get('full_payment_paid') else 0,
         d.get('payment_method',''), d.get('delivery_status','Request Submitted'), order_id))
    conn.commit(); conn.close()
    return redirect(url_for('admin_orders', table=table))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
