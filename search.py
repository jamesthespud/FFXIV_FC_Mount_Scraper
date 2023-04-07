import requests

# Enter your API key and Free Company ID here
api_key = "your_api_key_here"
fc_id = "your_fc_id_here"

# Define the URL for the mounts endpoint
url = f"https://xivapi.com/freecompany/{fc_id}?data=MOUNTS"

# Define headers with your API key
headers = {"Authorization": f"Bearer {api_key}"}

# Make a request to the API and retrieve the response
response = requests.get(url, headers=headers)

# Check for errors in the response
if response.status_code != 200:
    print("Error:", response.json()["Error"])
else:
    # Create a dictionary to hold the mounts by expansion
    mounts_by_expansion = {}

    # Group the mounts by expansion
    for member in response.json()["FreeCompany"]["Mounts"]:
        for mount in member["Mounts"]:
            if mount["Item"]["LevelItem"]["Expansion"]["ID"] not in mounts_by_expansion:
                mounts_by_expansion[mount["Item"]["LevelItem"]["Expansion"]["ID"]] = {
                    "Name": mount["Item"]["LevelItem"]["Expansion"]["Name"],
                    "Mounts": []
                }
            mounts_by_expansion[mount["Item"]["LevelItem"]["Expansion"]["ID"]]["Mounts"].append(mount["Name"])

    # Print the list of mounts by expansion
    for expansion_id, expansion in sorted(mounts_by_expansion.items()):
        print(expansion["Name"])
        print("-" * len(expansion["Name"]))
        for mount in sorted(expansion["Mounts"]):
            print(mount)
        print("")
