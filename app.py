from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    features = [
        {
            'icon': 'fas fa-file-alt',
            'title': 'Multi-document Analysis',
            'description': 'Support for PDF, DOCX, and TXT files'
        },
        {
            'icon': 'fas fa-brain',
            'title': 'AI-powered Analysis',
            'description': 'Advanced thematic analysis using GPT models'
        },
        {
            'icon': 'fas fa-chart-bar',
            'title': 'Rich Visualizations',
            'description': 'Interactive charts and network graphs'
        }
    ]
    
    return render_template('index.html', features=features)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
