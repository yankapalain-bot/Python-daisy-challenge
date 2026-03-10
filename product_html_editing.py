import requests
import json
# link obtained from freshco website flyer section using developer tools
url_freshco_mar_5_11_2026 = "https://dam.flippenterprise.net/flyerkit/publication/7813184/products?display_type=all&locale=en&access_token=881f0b9feea3693a704952a69b2a037a"

# Function to get the data as list of dictionaries - full information
def get_data(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()  # Automatically parses the JSON response
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()
  except json.JSONDecodeError:
    print("Error decoding JSON")
    exit()
  return data

# calling the previous function to get the full data into a variable called data_freshco
data_freshco = get_data(url_freshco_mar_5_11_2026)
print(len(data_freshco)) # to know how many products we have
print(type(data_freshco)) # to check what king of data structure we have (list)
print(data_freshco[0]) # to explore the one item in the list, user data_freshco[start_index:end_in




def create_website(template_file, html_output):
    """Function that reads the contents of a template html file
    dynamically update its content, and outputs into an index.html file

    Args:
        template_file (string): path to the template.html file
        html_output (string): path to the index.html file
    """
    
    # Read template.html file and store boilerplate code
    html_base = ""
    with open(template_file, "r") as website:
        html_base = website.read()

    # Update Title
    new_title = "My Website"
    modified_html = html_base.replace("<title>Document", f"<title>{new_title}")
    
    # Implement DaisyUI
    daisy_ui = """
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
    """
    
    modified_html = modified_html.replace("</head>", f"{daisy_ui}</head>")
    
    # Helper function to add element before body tag and return modified_html
    def add_to_body(modified_html, element_to_add):
        
        modified_html = modified_html.replace("</body>", f"{element_to_add}</body>")
        return modified_html
    
    # Apply Theme
    data_theme = "halloween"
    modified_html = modified_html.replace('<html lang="en">',
                                          f'<html lang="en" data-theme="{data_theme}">')
    
    # Add Title to Body
    h1_tag = "<h1>Welcome to My Website</h1>"
    modified_html = add_to_body(modified_html, h1_tag)
    
   

    # Add card to html    
    card = f"""
         <div class="card lg:card-side bg-base-100 shadow-sm">
            <figure>
                <img
                src="https://img.daisyui.com/images/stock/photo-1494232410401-ad00d5433cfa.webp"
                alt="Album" />
            </figure>
            <div class="card-body">
                <h2 class="card-title">New album is released!</h2>
                <p>Click the button to listen on Spotiwhy app.</p>
                <div class="card-actions justify-end">
                <button class="btn btn-primary">Listen</button>
                </div>
            </div>
        </div>     
        """
    modified_html = add_to_body(modified_html, card)

    # Add footer to html
    foot = f"""
        <p>  </p>
        <p>  </p>
        <footer class="footer sm:footer-horizontal bg-neutral text-neutral-content items-center p-4">
            <aside class="grid-flow-col items-center">    
                <p>Copyright ©2026 - All right reserved</p>
            </aside>            
        </footer>
        """
    modified_html = modified_html.replace("</body>", f"{foot}</body>")
    
    # Write index.html file after updating with Python
    with open(html_output, "w") as file:
        file.write(modified_html)
    
#create_website("./template.html", "./index.html")