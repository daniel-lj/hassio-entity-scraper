This program extracts entity id's from home assistant and puts them into an Excel file.
It is useful when for example, in my case, changing from ZHA to MQTT. So I can rename my entities to the same names and keep automations and scripts without altering them.
I created this because it is time consuming to manually download every entity id.

Steps:
- Access Home Assistant API: Home Assistant provides an API to get device and entity information. Generate a long term token. We will use HTTP requests to interact with this API.
- Authentication: The program will need an access token (Bearer Token) to authenticate against the Home Assistant API.
- Fetch Devices and Entities: Using the /api/devices and /api/states endpoints of Home Assistant, we will retrieve device and entity information.
- Store Data in an Excel File: Use the pandas library to process the data and save it to an Excel file.
- Sort the Data: We will sort the data based on device names and entity IDs.
- Install Required Libraries: We'll use requests for API calls, and pandas and openpyxl for handling Excel files.

Usage:
- Run 'pip install requests pandas openpyxl' to install dependencies
- Replace the HA_URL and ACCESS_TOKEN with your Home Assistant details.
- Run the script, and it will generate an Excel file home_assistant_devices_entities.xlsx with the sorted device and entity data.
