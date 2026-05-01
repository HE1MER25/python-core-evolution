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

def scout_journals(categories, num_results=20):
    for filename, query in categories.items():
        print(f"Searching for: {filename}...")
        results_list = []
        
        try:
            # Corrected attribute: search_pubs
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
        
        # Save results if any were found
        if results_list:
            df = pd.DataFrame(results_list)
            
            # Save raw CSV
            df.to_csv(f"{filename}.csv", index=False)
            
            # Save formatted Excel (.xlsx) using the 'with' context manager
            # This automatically handles closing the file
            with pd.ExcelWriter(f"{filename}.xlsx", engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Heimer_Data', index=False)
                
                # Auto-adjust column widths for readability
                worksheet = writer.sheets['Heimer_Data']
                for i, col in enumerate(df.columns):
                    # Calculate width based on max content length or header length
                    column_len = max(df[col].astype(str).str.len().max(), len(col)) + 2
                    worksheet.set_column(i, i, column_len)
            
            print(f"Saved {len(df)} results to {filename}.csv and {filename}.xlsx")
        else:
            print(f"No results found for {filename}")

        # STRATEGIC DELAY: Move this here to pause BETWEEN categories
        print(f"Pausing 10s to avoid Google detection...")
        time.sleep(10)
# Run the Scout
scout_journals(search_categories)