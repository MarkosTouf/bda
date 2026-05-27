import csv

# 1. State Allocation (O(1) Space)
first_5_rows = []
usa_count = 0
first_exact_action = None
first_partial_action = None

with open("movies.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    
    # 2. The Processing Engine (Single O(N) Time Pass)
    for i, row in enumerate(reader):
        
        # Grab the first 5 rows
        if i < 5:
            first_5_rows.append(row)
            
        # Using .get() prevents fatal crashes if a cell is completely empty
        country = row.get("country", "")
        genres = row.get("genres", "")
            
        if "USA" in country:
            usa_count += 1
            
        # Locks the exact match
        if not first_exact_action and genres == "Action":
            first_exact_action = row
            
        # Ensures we find a movie that contains Action, but isn't ONLY Action
        if not first_partial_action and "Action" in genres and genres != "Action":
            first_partial_action = row

# 3. Clean Final Delivery
print("--- 1. Field Names ---")
print(headers)

print("\n--- 2. First 5 Data Rows ---")
for r in first_5_rows:
    print(r)

print(f"\n--- 3. USA Movies Count: {usa_count} ---")

print("\n--- 4. First Exact 'Action' Movie ---")
print(first_exact_action)

print("\n--- 5. First Partial 'Action' Match ---")
print(first_partial_action)