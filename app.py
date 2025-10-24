from flask import Flask, render_template, request, jsonify
from evaluation_ai import evaluator
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'advanced-ai-evaluation-system'

@app.route('/')
def index():
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
        employee_id = request.form.get('employee_id', '')
        
        # Employee info
        employee_info = {
            'name': request.form.get('employee_name', 'Employee'),
            'employee_id': employee_id,
            'department': request.form.get('department', 'General'),
            'position': request.form.get('position', 'Staff'),
            'period': request.form.get('period', 'Q1 2024'),
            'reviewer_name': request.form.get('reviewer_name', 'AI Evaluation System'),
            'tenure_months': tenure_months,
            'evaluation_date': datetime.now().strftime('%B %d, %Y %H:%M:%S'),
            'evaluation_id': f"EVAL-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        }
        
        # Perform advanced AI evaluation
        result = evaluator.evaluate_performance(scores, tenure_months)
        result.update(employee_info)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/system-info')
def system_info():
    """API endpoint showing AI system capabilities"""
    return jsonify({
        'system_name': 'Advanced AI Performance Analytics Engine',
        'version': '2.1.0',
        'ai_models': [
            'Performance Pattern Recognition',
            'Predictive Growth Analytics', 
            'Skill Gap Analysis Engine',
            'Benchmarking Algorithm',
            'Risk Assessment Model',
            'Career Trajectory Forecasting'
        ],
        'analysis_layers': 7,
        'data_points_analyzed': 28,
        'confidence_threshold': 0.75
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)