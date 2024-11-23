################################  Storage_Optimization.ipynb  ####################################
# Author: Sukhendu Sain
# Description: Main file of codebase. Houses main code
# Data: 22-Nov-2024
#################################################################################

# Import Necessary Libraries, Utils, and Config Files
from utils import *
from config import *



#### Read FILE:: (AKINS FoMoCo_Piece_Sales_112222_YTD.xlsx) into Dataframe
df_Akins = read_excel(AKINS_FOMO_FILE_PATH)
print_df(df_Akins) # Print the Dataframe



#### Read FILE:: (GPARTS Part Measures.xlsx) into Dataframe
df_Gparts = read_excel(GPARTS_FILE_PATH)
print_df(df_Gparts) # Print the Dataframe



#### Read FILE:: (Wholesale JAN_Oct_Parts_Ranking_Counter_Invoices_All_Brands.xlsx) into Dataframe
df_Wholesale = read_excel(WHOLESALE_FILE_PATH)

# Clean the Wholesale Dataframe
df_Wholesale = df_Wholesale.drop(columns=[col for col in df_Wholesale.columns if 'Unnamed' in col], inplace=False)
df_Wholesale_Ford = df_Wholesale[df_Wholesale['Vendor'] == 'FOR'] # Put only 'Ford' Brand Data into another DF

print_df(df_Wholesale_Ford) # Print the Dataframe



#### Read FILE:: (Service JAN_Oct_Parts_Ranking_ROs_All_Brands.xlsx) into Dataframe
df_Service = read_excel(SERVICE_FILE_PATH)

# Clean the Service Dataframe
df_Service = df_Service.drop(columns=[col for col in df_Service.columns if 'Unnamed' in col], inplace=False)
df_Service_Ford = df_Service[df_Service['Vendor'] == 'FOR'] # Put only 'Ford' Brand Data into another DF

print_df(df_Service_Ford, 100) # Print the Dataframe





df_CounterPad = read_excel(COUNTERPAD_FILE_PATH)
data = df_CounterPad.iloc[0,0]

# Split the data into lines
lines = data.strip().split('\\n')

# Create a list to store the parsed data
parsed_data = []

# Parse each line
for line in lines:
    # Split the line into columns
    columns = line.split()
    
    # Extract the data
    mfg = columns[0]
    src = columns[1]
    cost = float(columns[2].replace(',', ''))
    list_price = float(columns[3].replace(',', ''))
    bin = columns[4]
    part_number = columns[5]
    oh = float(columns[-1])
    
    # Extract the description (all columns between part_number and OH)
    description = ' '.join(columns[6:-1])
    
    # Add the parsed data to the list
    parsed_data.append({
        'Mfg': mfg,
        'Src': src,
        'Cost': cost,
        'List': list_price,
        'Bin': bin,
        'Part Number': part_number,
        'Description': description,
        'OH': oh
    })

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(parsed_data)

# Print the DataFrame
print_df(df, 100)

# Assuming you have DataFrames named df_Akins, df_Gparts, df_Wholesale, and df_Service
all_dfs = [df_Akins, df_Gparts, df_Wholesale, df_Service]

# Get the part number columns from each DataFrame
part_number_columns = ['Part#', 'Svc Part Number', 'Part Number', '* indicates a superseded part\nPart Number']  # Adjust if column names are different

# Find common part numbers
common_part_numbers = set(all_dfs[0][part_number_columns[0]])
for i in range(1, len(all_dfs)):
    common_part_numbers &= set(all_dfs[i][part_number_columns[i]])

print(f"Part numbers common to all DataFrames: {len(common_part_numbers)}")
print(common_part_numbers)