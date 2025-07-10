from ai_models.energy_usage_insights import train_energy_usage_model
from ai_models.predictive_maintenance import train_predictive_maintenance_model
from ai_models.dynamic_recommendations import train_dynamic_recommendations_model

def ai_controller():
    # Load data
    energy_data = load_energy_data()
    maintenance_data = load_maintenance_data()
    recommendations_data = load_recommendations_data()

    # Train models
    energy_model = train_energy_usage_model(energy_data)
    maintenance_model = train_predictive_maintenance_model(maintenance_data)
    recommendations_model = train_dynamic_recommendations_model(recommendations_data)

    # Save models
    save_model(energy_model, 'energy_usage_model.pkl')
    save_model(maintenance_model, 'predictive_maintenance_model.pkl')
    save_model(recommendations_model, 'dynamic_recommendations_model.pkl')