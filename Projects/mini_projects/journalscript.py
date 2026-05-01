import time
from scholarly import scholarly
import pandas as pd

# Define your Categorized Search Queries
search_categories = {
    "Ibadan_1D_Links": '("Vertical Electrical Sounding" OR "VES") AND "Ibadan" AND "Basement"',
    "Ibadan_2D_Links": '("Electrical Resistivity Tomography" OR "2D ERT") AND "Ibadan" AND "Fracture"',
    "Ibadan_Tech_Links": '("Resistivity Inversion" OR "Non-uniqueness") AND "Nigeria" AND "Machine Learning"',
    "Ibadan_Localized_Links": '("Geoelectric") AND ("Akinyele" OR "Iddo") AND "Groundwater"'
}

def scout_journals(categories, num_results=20): # Reduced to 5 to avoid bot detection
    # Add this right after the loop saves the CSV:
    print(f"Pausing to avoid detection...")
    time.sleep(10) # Wait 10 seconds before the next category
    for filename, query in categories.items():
        print(f"Searching for: {filename}...")
        results_list = []
        
        # CORRECTED ATTRIBUTE: search_pubs
        try:
            search_query = scholarly.search_pubs(query)
            
            for i in range(num_results):
                try:
                    result = next(search_query)
                    results_list.append({
                        "Title": result['bib'].get('title'),
                        "Author": result['bib'].get('author'),
                        "Year": result['bib'].get('pub_year'),
                        "Link": result.get('pub_url'),
                        "Snippet": result.get('snippet')
                    })
                except StopIteration:
                    break
        except Exception as e:
            print(f"Error searching for {filename}: {e}")
        
        # Save each category to its own CSV
        if results_list:
            df = pd.DataFrame(results_list)
            df.to_csv(f"{filename}.csv", index=False)
            print(f"Saved {len(df)} links to {filename}.csv")
        else:
            print(f"No results found for {filename}")

# Run the Scout
scout_journals(search_categories)