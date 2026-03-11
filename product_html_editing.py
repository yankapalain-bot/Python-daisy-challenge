import requests 
import json
import pandas as pd
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
#print(len(data_freshco)) # to know how many products we have
#print(type(data_freshco)) # to check what king of data structure we have (list)
#print(data_freshco[0]) # to explore the one item in the list, user data_freshco[start_index:end_in
#for key,  value in data_freshco[0].items():
#   print(key)

# use of list comprehension create a list of dictionaries to select only 3 elements from every item -> name, price, pic, image_url
results_Freshco = [{'name': item['name'], 'price': item['price_text'], 'pic': item['image_url']} for item in data_freshco]
#print(type(results_Freshco))

###creating a dataframe
dataframe = pd.DataFrame(results_Freshco)
#print(dataframe.head())

#generating a html table from a dataframe     ---- use pandas library
html_table = dataframe.to_html()

#generating a html file
#with open("pandas_table.html", "w") as table:
#   table.write(html_table)


# displawying the image in the table
# helper function to change url link
def format_as_img(url):
    return f'<img src="{url}" width="100">'

# modifying the dataframe
#styled_df = dataframe.style.format({'pic': format_as_img})

# creating table
#html_table_img = styled_df.to_html()

# writing new files with pics
#with open("pandas_table_img.html", "w") as table:
#  table.write(html_table_img)


#data = results_Freshco[0]

button_tag = f"""
    <td>
        <button class="btn btn-success">Edit</button>
        <button class="btn btn-error">Delete</button>
    </td>
    \n
"""
#core_table += f"<td> {index} </td> \n"
core_table = f""
for index, data in enumerate(results_Freshco):   
   core_table += f"<tr> \n"   
   core_table += f"<td> {index+1} </td> \n"
   for key, value in data.items():
      if key == "pic":
        img_tag = f'<img src="{value}" width="50" height="50">'
        core_table += f"""
            <td>
            <a href="link">
                <div class="flex items-center gap-3">
                    <div class="avatar">
                        <div class="mask mask-squircle h-12 w-12">
                            {img_tag}
                        </div>
                    </div>                
                </div>
            </a>
            </td>            
        """
      else:        
        core_table += f"<td>{value}</td>  \n" 
     
   core_table += button_tag
   core_table += f"</tr>  \n"
   

#print(core_table)



def create_website(template_file, html_output):
     
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
    #data_theme = "halloween"
    #modified_html = modified_html.replace('<html lang="en">',
    #                                     f'<html lang="en" data-theme="{data_theme}">')
    
    # Add Title to Body
    h1_tag = '\n <h1 class="font-bold text-center text-lg"> Welcome to Frescho list product page </h1>'
    modified_html = add_to_body(modified_html, h1_tag)
    
   

    # Add table html    
    head_table = f"""
         <div class="overflow-x-auto">
            <table class="table">               
                <thead>
                    <tr> 
                        <th>#</th>                     
                        <th>Name</th>
                        <th>Price</th>
                        <th>image</th>     
                        <th>Actions</th>                  
                    </tr>
                </thead>
                <tbody>
        """
    
    foot_table = f"""
                </tbody>
            </table>
        </div>

    """
     
    modified_html = add_to_body(modified_html, head_table)
    modified_html = add_to_body(modified_html, core_table)
    modified_html = add_to_body(modified_html, foot_table)



    # Add footer to html
    foot = f"""
        \n
        \n
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
    
create_website("./template.html", "./index.html")
