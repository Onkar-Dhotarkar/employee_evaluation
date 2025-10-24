from flask import Flask, render_template, request, jsonify
from evaluation_ai import evaluator
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-123')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate_performance():
    try:
        # Get form data
        scores = {
            'quality_of_work': int(request.form.get('quality_of_work', 5)),
            'productivity': int(request.form.get('productivity', 5)),
            'teamwork': int(request.form.get('teamwork', 5)),
            'communication': int(request.form.get('communication', 5)),
            'initiative': int(request.form.get('initiative', 5))
        }
        
        # Validate scores
        for key, value in scores.items():
            if value < 1 or value > 10:
                return jsonify({'error': f'{key} must be between 1 and 10'})
        
        # Get additional parameters
        tenure_months = int(request.form.get('tenure_months', 12))
        
        # Employee info
        employee_info = {
            'name': request.form.get('employee_name', 'Employee'),
            'employee_id': request.form.get('employee_id', ''),
            'department': request.form.get('department', 'General'),
            'position': request.form.get('position', 'Staff'),
            'period': request.form.get('period', 'Q1 2024'),
            'reviewer_name': request.form.get('reviewer_name', 'Manager'),
            'tenure_months': tenure_months,
            'evaluation_date': datetime.now().strftime('%B %d, %Y')
        }
        
        # Perform evaluation
        result = evaluator.evaluate_performance(scores)
        result.update(employee_info)
        
        # Add enhanced fields for UI
        result['ai_score'] = round(result['overall_score'] * 0.95 + 0.5, 2)
        result['confidence'] = "High" if result['overall_score'] >= 7 else "Medium"
        result['predicted_growth'] = "Strong" if result['overall_score'] >= 7 else "Moderate"
        result['benchmark_comparison'] = "Meeting expectations"
        result['improvement_priority'] = [
            ('quality_of_work', 0.8),
            ('communication', 0.6), 
            ('initiative', 0.5)
        ]
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error: {e}")  # This will show in Vercel logs
        return jsonify({'error': str(e)})

# This works for both local and Vercel
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
else:
    # For Vercel deployment
    application = app