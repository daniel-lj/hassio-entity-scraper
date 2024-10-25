import requests
import pandas as pd

# Step 1: Set up Home Assistant connection details
HA_URL = 'http://your-home-assistant-url:8123'  # Replace with your Home Assistant URL
ACCESS_TOKEN = 'your-access-token-here'  # Replace with your Home Assistant long-lived access token

# Step 2: Function to get entity states from Home Assistant
def get_entities():
    url = f'{HA_URL}/api/states'
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching entities: {response.status_code}")
        return []

# Step 3: Process entities and save to Excel
def save_to_excel(entities, output_file='home_assistant_entities.xlsx'):
    # Process entities into a DataFrame
    entity_list = []
    for entity in entities:
        entity_list.append({
            'Entity ID': entity['entity_id'],
            'Entity Name': entity['attributes'].get('friendly_name', 'N/A'),
            'State': entity['state']
        })

    entity_df = pd.DataFrame(entity_list)

    # Sort the DataFrame by Entity Name and Entity ID
    sorted_df = entity_df.sort_values(by=['Entity Name', 'Entity ID'])

    # Save to Excel
    sorted_df.to_excel(output_file, index=False)

    print(f"Data saved to {output_file}")

# Step 4: Main execution
if __name__ == '__main__':
    # Fetch entities
    entities = get_entities()

    # Save data to Excel
    if entities:
        save_to_excel(entities)
