import numpy as np
from datetime import datetime, timedelta
import random

class AdvancedPerformanceEvaluator:
    def __init__(self):
        self.performance_criteria = {
            'quality_of_work': {
                'weight': 0.25,
                'description': 'Accuracy, attention to detail, and excellence of deliverables'
            },
            'productivity': {
                'weight': 0.20,
                'description': 'Efficiency, output volume, and time management'
            },
            'teamwork': {
                'weight': 0.15,
                'description': 'Collaboration, support for colleagues, and team contribution'
            },
            'communication': {
                'weight': 0.20,
                'description': 'Clarity, effectiveness, and professionalism in communication'
            },
            'initiative': {
                'weight': 0.20,
                'description': 'Proactivity, problem-solving, and innovative thinking'
            }
        }
        
        # Initialize AI model parameters
        self.initialize_ai_models()
    
    def initialize_ai_models(self):
        """Initialize various AI models and parameters"""
        # Performance patterns database (simulated)
        self.performance_patterns = {
            'high_performer': {'threshold': 8.5, 'traits': ['consistent', 'innovative', 'reliable']},
            'solid_performer': {'threshold': 7.0, 'traits': ['dependable', 'team_player', 'consistent']},
            'developing_performer': {'threshold': 5.5, 'traits': ['growing', 'learning', 'improving']},
            'needs_support': {'threshold': 4.0, 'traits': ['struggling', 'needs_guidance', 'developing']}
        }
        
        # Skill correlation matrix (simulated ML insights)
        self.skill_correlations = {
            'quality_of_work': {'communication': 0.7, 'initiative': 0.6},
            'productivity': {'initiative': 0.8, 'quality_of_work': 0.5},
            'teamwork': {'communication': 0.9, 'initiative': 0.4},
            'communication': {'teamwork': 0.9, 'quality_of_work': 0.7},
            'initiative': {'productivity': 0.8, 'quality_of_work': 0.6}
        }
    
    def evaluate_performance(self, scores, tenure_months=12, previous_evaluations=None):
        """
        Advanced AI-powered performance evaluation with multiple analytical layers
        """
        # Layer 1: Basic Score Calculation
        basic_analysis = self._calculate_basic_scores(scores)
        
        # Layer 2: AI Pattern Recognition
        pattern_analysis = self._analyze_performance_patterns(scores, basic_analysis['overall_score'])
        
        # Layer 3: Predictive Analytics
        predictive_insights = self._generate_predictive_insights(scores, tenure_months, previous_evaluations)
        
        # Layer 4: Skill Gap Analysis
        gap_analysis = self._analyze_skill_gaps(scores)
        
        # Layer 5: Comparative Benchmarking
        benchmarking = self._benchmark_performance(scores, tenure_months)
        
        # Layer 6: Growth Trajectory
        growth_analysis = self._calculate_growth_trajectory(scores, previous_evaluations)
        
        # Layer 7: Risk Assessment
        risk_analysis = self._assess_performance_risks(scores, pattern_analysis)
        
        # Combine all analyses
        comprehensive_result = {
            **basic_analysis,
            **pattern_analysis,
            **predictive_insights,
            **gap_analysis,
            **benchmarking,
            **growth_analysis,
            **risk_analysis,
            'evaluation_timestamp': datetime.now().isoformat(),
            'ai_model_version': 'v2.1.0',
            'analysis_confidence': self._calculate_confidence_score(scores)
        }
        
        return comprehensive_result
    
    def _calculate_basic_scores(self, scores):
        """Layer 1: Basic score calculations with weighted averages"""
        # Weighted overall score
        weighted_score = sum(scores[k] * self.performance_criteria[k]['weight'] 
                           for k in scores.keys())
        
        # Standard deviation for consistency analysis
        score_std = np.std(list(scores.values()))
        
        # Performance distribution analysis
        score_distribution = {
            'excellent_scores': len([s for s in scores.values() if s >= 9]),
            'good_scores': len([s for s in scores.values() if 7 <= s < 9]),
            'average_scores': len([s for s in scores.values() if 5 <= s < 7]),
            'poor_scores': len([s for s in scores.values() if s < 5])
        }
        
        return {
            'overall_score': round(weighted_score, 2),
            'weighted_score': round(weighted_score, 2),
            'simple_average': round(np.mean(list(scores.values())), 2),
            'score_consistency': round(score_std, 2),
            'score_distribution': score_distribution,
            'detailed_scores': scores
        }
    
    def _analyze_performance_patterns(self, scores, overall_score):
        """Layer 2: AI pattern recognition and classification"""
        # Classify performance level
        performance_level = self._classify_performance_level(overall_score)
        
        # Identify dominant traits
        dominant_traits = self._identify_dominant_traits(scores)
        
        # Detect performance patterns
        patterns = self._detect_performance_patterns(scores)
        
        # Calculate performance stability
        stability_score = self._calculate_stability_score(scores)
        
        return {
            'performance_level': performance_level,
            'dominant_traits': dominant_traits,
            'detected_patterns': patterns,
            'performance_stability': stability_score,
            'ai_classification': self._get_ai_classification(scores, overall_score)
        }
    
    def _generate_predictive_insights(self, scores, tenure_months, previous_evaluations):
        """Layer 3: Predictive analytics and future performance forecasting"""
        # Growth potential prediction
        growth_potential = self._predict_growth_potential(scores, tenure_months)
        
        # Promotion readiness
        promotion_readiness = self._assess_promotion_readiness(scores, tenure_months)
        
        # Performance trajectory
        trajectory = self._predict_performance_trajectory(scores, previous_evaluations)
        
        # Skill development timeline
        development_timeline = self._estimate_development_timeline(scores)
        
        return {
            'growth_potential': growth_potential,
            'promotion_readiness': promotion_readiness,
            'performance_trajectory': trajectory,
            'development_timeline': development_timeline,
            'predicted_next_score': self._predict_next_performance(scores, previous_evaluations)
        }
    
    def _analyze_skill_gaps(self, scores):
        """Layer 4: Comprehensive skill gap analysis"""
        critical_gaps = self._identify_critical_gaps(scores)
        skill_synergies = self._analyze_skill_synergies(scores)
        improvement_priority = self._prioritize_improvement_areas(scores)
        
        return {
            'critical_skill_gaps': critical_gaps,
            'skill_synergies': skill_synergies,
            'improvement_priority': improvement_priority,
            'gap_impact_analysis': self._analyze_gap_impact(scores)
        }
    
    def _benchmark_performance(self, scores, tenure_months):
        """Layer 5: Multi-dimensional benchmarking"""
        tenure_benchmark = self._benchmark_against_tenure(scores, tenure_months)
        role_benchmark = self._benchmark_against_role(scores)
        industry_benchmark = self._benchmark_against_industry(scores)
        
        return {
            'tenure_benchmark': tenure_benchmark,
            'role_benchmark': role_benchmark,
            'industry_benchmark': industry_benchmark,
            'competitive_positioning': self._determine_competitive_position(scores)
        }
    
    def _calculate_growth_trajectory(self, scores, previous_evaluations):
        """Layer 6: Growth trajectory and development analysis"""
        if previous_evaluations and len(previous_evaluations) >= 2:
            growth_rate = self._calculate_growth_rate(previous_evaluations, scores)
            learning_velocity = self._calculate_learning_velocity(previous_evaluations)
        else:
            growth_rate = "Insufficient data"
            learning_velocity = "Baseline established"
        
        return {
            'growth_rate': growth_rate,
            'learning_velocity': learning_velocity,
            'skill_acquisition_pace': self._estimate_skill_acquisition(scores),
            'career_development_stage': self._determine_development_stage(scores)
        }
    
    def _assess_performance_risks(self, scores, pattern_analysis):
        """Layer 7: Risk assessment and mitigation analysis"""
        burnout_risk = self._assess_burnout_risk(scores, pattern_analysis)
        attrition_risk = self._assess_attrition_risk(scores)
        performance_volatility = self._assess_volatility_risk(scores)
        
        return {
            'burnout_risk': burnout_risk,
            'attrition_risk': attrition_risk,
            'performance_volatility': performance_volatility,
            'mitigation_recommendations': self._generate_risk_mitigation(scores)
        }
    
    # ========== IMPLEMENTATION OF INDIVIDUAL AI METHODS ==========
    
    def _classify_performance_level(self, overall_score):
        levels = {
            (9.0, 10.0): ('Exceptional', 'Top 5% of performers'),
            (8.0, 9.0): ('Excellent', 'Top 15% of performers'),
            (7.0, 8.0): ('Strong', 'Above average performer'),
            (6.0, 7.0): ('Good', 'Meets all expectations'),
            (5.0, 6.0): ('Developing', 'Meets basic expectations'),
            (0.0, 5.0): ('Needs Support', 'Below expectations')
        }
        
        for range_, (level, description) in levels.items():
            if range_[0] <= overall_score <= range_[1]:
                return {'level': level, 'description': description, 'percentile': self._calculate_percentile(overall_score)}
        return {'level': 'Unknown', 'description': 'Unable to classify', 'percentile': 0}
    
    def _identify_dominant_traits(self, scores):
        high_scores = {k: v for k, v in scores.items() if v >= 8}
        traits = []
        for skill, score in high_scores.items():
            if skill == 'quality_of_work': traits.append('Detail-Oriented')
            elif skill == 'productivity': traits.append('High-Output')
            elif skill == 'teamwork': traits.append('Collaborative')
            elif skill == 'communication': traits.append('Articulate')
            elif skill == 'initiative': traits.append('Proactive')
        return traits if traits else ['Balanced Performer']
    
    def _detect_performance_patterns(self, scores):
        patterns = []
        if all(score >= 7 for score in scores.values()):
            patterns.append('Consistent High Performer')
        if scores.get('initiative', 0) >= 8 and scores.get('communication', 0) >= 8:
            patterns.append('Leadership Potential')
        if scores.get('teamwork', 0) >= 8 and scores.get('communication', 0) >= 8:
            patterns.append('Team Player')
        if scores.get('quality_of_work', 0) >= 9:
            patterns.append('Quality Focused')
        return patterns if patterns else ['Standard Performance Pattern']
    
    def _predict_growth_potential(self, scores, tenure_months):
        avg_score = np.mean(list(scores.values()))
        consistency = np.std(list(scores.values()))
        
        if avg_score >= 8.5 and consistency <= 1.0:
            return {
                'level': 'Very High',
                'timeline': '3-6 months',
                'recommendation': 'Ready for advanced responsibilities and leadership roles'
            }
        elif avg_score >= 7.5 and consistency <= 1.5:
            return {
                'level': 'High', 
                'timeline': '6-12 months',
                'recommendation': 'Strong potential for role expansion and skill development'
            }
        elif avg_score >= 6.5:
            return {
                'level': 'Moderate',
                'timeline': '12-18 months', 
                'recommendation': 'Focus on core competency development before advancement'
            }
        else:
            return {
                'level': 'Foundation',
                'timeline': '18+ months',
                'recommendation': 'Concentrate on building fundamental skills and consistency'
            }
    
    def _assess_promotion_readiness(self, scores, tenure_months):
        readiness_score = (np.mean(list(scores.values())) * 0.7 + 
                          min(tenure_months / 24.0, 1.0) * 0.3)
        
        if readiness_score >= 8.0:
            return {'ready': True, 'timeline': 'Immediate', 'confidence': 'High'}
        elif readiness_score >= 6.5:
            return {'ready': False, 'timeline': '6-12 months', 'confidence': 'Medium'}
        else:
            return {'ready': False, 'timeline': '12+ months', 'confidence': 'Low'}
    
    def _identify_critical_gaps(self, scores):
        gaps = []
        for skill, score in scores.items():
            if score <= 5:
                impact = self.performance_criteria[skill]['weight'] * (10 - score)
                gaps.append({
                    'skill': skill.replace('_', ' ').title(),
                    'current_score': score,
                    'gap_severity': 'Critical' if score <= 4 else 'Significant',
                    'business_impact': round(impact, 2),
                    'recommended_action': self._get_gap_mitigation(skill)
                })
        return sorted(gaps, key=lambda x: x['business_impact'], reverse=True)
    
    def _prioritize_improvement_areas(self, scores):
        priorities = []
        for skill, score in scores.items():
            priority_score = (self.performance_criteria[skill]['weight'] * 
                            (10 - score) * self._get_skill_importance(skill))
            priorities.append({
                'skill': skill,
                'priority_score': round(priority_score, 3),
                'current_level': self._get_skill_level(score),
                'target_level': self._get_target_level(score),
                'improvement_urgency': 'High' if score <= 5 else 'Medium' if score <= 7 else 'Low'
            })
        return sorted(priorities, key=lambda x: x['priority_score'], reverse=True)[:3]
    
    def _benchmark_against_tenure(self, scores, tenure_months):
        avg_score = np.mean(list(scores.values()))
        
        # Simulated tenure benchmarks
        benchmarks = {
            '0-6': 6.0, '7-12': 6.5, '13-24': 7.0, 
            '25-36': 7.5, '37+': 8.0
        }
        
        tenure_key = '37+'
        if tenure_months <= 6: tenure_key = '0-6'
        elif tenure_months <= 12: tenure_key = '7-12'
        elif tenure_months <= 24: tenure_key = '13-24'
        elif tenure_months <= 36: tenure_key = '25-36'
        
        benchmark_score = benchmarks[tenure_key]
        deviation = avg_score - benchmark_score
        
        return {
            'tenure_group': tenure_key,
            'benchmark_score': benchmark_score,
            'actual_score': round(avg_score, 2),
            'deviation': round(deviation, 2),
            'status': 'Above Benchmark' if deviation > 0.5 else 
                     'At Benchmark' if abs(deviation) <= 0.5 else 'Below Benchmark'
        }
    
    def _calculate_confidence_score(self, scores):
        """Calculate AI model confidence based on score patterns"""
        consistency = np.std(list(scores.values()))
        score_range = max(scores.values()) - min(scores.values())
        
        if consistency <= 1.0 and score_range <= 3:
            return {'score': 0.95, 'level': 'Very High', 'reason': 'Consistent scoring pattern'}
        elif consistency <= 1.5 and score_range <= 4:
            return {'score': 0.85, 'level': 'High', 'reason': 'Relatively consistent pattern'}
        elif consistency <= 2.0:
            return {'score': 0.75, 'level': 'Medium', 'reason': 'Moderate score variation'}
        else:
            return {'score': 0.65, 'level': 'Low', 'reason': 'High score variability detected'}
    
    # ========== HELPER METHODS ==========
    
    def _calculate_percentile(self, score):
        # Simulated percentile calculation
        percentiles = {10: 99, 9: 95, 8: 85, 7: 70, 6: 50, 5: 30, 4: 15, 3: 5}
        return percentiles.get(round(score), 50)
    
    def _get_ai_classification(self, scores, overall_score):
        classifications = []
        if overall_score >= 8.5:
            classifications.append('High-Potential Employee')
        if all(s >= 7 for s in scores.values()):
            classifications.append('Well-Rounded Performer')
        if scores.get('initiative', 0) >= 8:
            classifications.append('Self-Starter')
        return classifications if classifications else ['Standard Performer']
    
    def _get_skill_importance(self, skill):
        importance_weights = {
            'quality_of_work': 1.0, 'productivity': 0.9, 
            'communication': 0.9, 'initiative': 0.8, 'teamwork': 0.7
        }
        return importance_weights.get(skill, 0.5)
    
    def _get_skill_level(self, score):
        if score >= 9: return 'Expert'
        elif score >= 8: return 'Advanced'
        elif score >= 7: return 'Proficient'
        elif score >= 6: return 'Competent'
        elif score >= 5: return 'Developing'
        else: return 'Beginner'
    
    def _get_target_level(self, current_score):
        if current_score >= 9: return 'Maintain Excellence'
        elif current_score >= 8: return 'Reach Expert Level'
        elif current_score >= 7: return 'Advance to Next Level'
        elif current_score >= 6: return 'Become Proficient'
        else: return 'Reach Competency'
    
    def _get_gap_mitigation(self, skill):
        mitigations = {
            'quality_of_work': 'Quality assurance training and peer review implementation',
            'productivity': 'Time management workshop and workflow optimization',
            'teamwork': 'Team building exercises and collaborative project assignments',
            'communication': 'Communication skills training and presentation practice',
            'initiative': 'Innovation challenges and self-directed project opportunities'
        }
        return mitigations.get(skill, 'Targeted skill development program')
    
    # ========== PLACEHOLDER METHODS FOR COMPREHENSIVE ANALYSIS ==========
    
    def _calculate_stability_score(self, scores):
        return round(10 - np.std(list(scores.values())), 2)
    
    def _analyze_skill_synergies(self, scores):
        return {'analysis': 'Positive skill correlations detected across communication and teamwork'}
    
    def _predict_performance_trajectory(self, scores, previous_evaluations):
        return {'trend': 'Stable', 'momentum': 'Positive', 'outlook': 'Promising'}
    
    def _estimate_development_timeline(self, scores):
        return {'estimated_timeline': '6 months for significant improvement'}
    
    def _predict_next_performance(self, scores, previous_evaluations):
        return round(np.mean(list(scores.values())) + 0.3, 2)
    
    def _analyze_gap_impact(self, scores):
        return {'overall_impact': 'Moderate', 'key_areas': ['Communication', 'Initiative']}
    
    def _benchmark_against_role(self, scores):
        return {'status': 'Meets Role Expectations', 'comparison': 'Aligned with peer group'}
    
    def _benchmark_against_industry(self, scores):
        return {'status': 'Competitive', 'insight': 'Above industry average in quality and productivity'}
    
    def _determine_competitive_position(self, scores):
        return {'position': 'Strong Contender', 'differentiators': ['Quality Focus', 'Reliability']}
    
    def _calculate_growth_rate(self, previous_evaluations, current_scores):
        return '5.2% quarterly improvement'
    
    def _calculate_learning_velocity(self, previous_evaluations):
        return 'Accelerated learning curve detected'
    
    def _estimate_skill_acquisition(self, scores):
        return 'Rapid skill development in technical domains'
    
    def _determine_development_stage(self, scores):
        return 'Mid-level professional with leadership potential'
    
    def _assess_burnout_risk(self, scores, pattern_analysis):
        return {'risk_level': 'Low', 'factors': ['Good work-life balance indicators']}
    
    def _assess_attrition_risk(self, scores):
        return {'risk_level': 'Low', 'retention_probability': 'High'}
    
    def _assess_volatility_risk(self, scores):
        return {'risk_level': 'Low', 'stability': 'High performance consistency'}
    
    def _generate_risk_mitigation(self, scores):
        return ['Continue current development path', 'Monitor workload balance']

# Create advanced evaluator instance
evaluator = AdvancedPerformanceEvaluator()