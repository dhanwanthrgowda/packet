def get_areas_by_postal_code(postal_code):
    # Example data set (replace with actual data source)
    bangalore_areas = {
        "560001": ["M.G. Road", "Brigade Road", "Cubbon Park"],
        "560002": ["Vidhana Soudha", "City Market", "Chickpet"],
        "560003": ["Malleswaram", "Yeshwanthpur", "Rajajinagar"],
        "560004": ["Basavanagudi", "Gandhi Bazaar", "Bugle Rock"],
        "560005": ["Indiranagar", "HAL", "Domlur"],
        "560006": ["Seshadripuram", "Kumara Park", "High Grounds"],
        "560007": ["Frazer Town", "Cox Town", "Richmond Town"],
        "560008": ["Jayanagar", "JP Nagar", "BTM Layout"],
        "560009": ["Benson Town", "Shivaji Nagar", "Cleveland Town"],
        "560010": ["Basaveshwaranagar", "Kamakshipalya", "Vijayanagar"],
        # Add more postal codes and corresponding areas as needed
    }
    
    if postal_code in bangalore_areas:
        return bangalore_areas[postal_code]
    else:
        return ["Unknown"]

