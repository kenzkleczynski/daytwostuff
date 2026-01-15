#%% Opening Codespace
#What is your terminal display "path"? (type/paste as text into the .py file)
    # @kenzkleczynski ➜ /workspaces/daytwostuff (main) $

# %% Create Virtual Environment
# Should you include the environment in your repo or not?
     # no you should not
# Now what is your terminal display "path"? Is it different?
    # (.venv) @kenzkleczynski ➜ /workspaces/daytwostuff (main) $
# source .venv/bin/activate

# %% Viewing Dataset
import pandas as pd
data = pd.read_csv('titanic.csv')
print(data.head())

# %% Extension Managment
# Find the extension in the extension menu. What do you notice about the extension menu?
    # The menu chowees the instaltion you have installed localle and in the codepsace and also offeres you recomneations.
# Review the capabilities, what are three useful elements of Data Wrangler?
    # One element is the Data Filters/Sort. 
    # Another is the summary statistics of whole dataset. 
    # An lastly the Quick Insights is useful for quick assesments of spesfic columns.

# %% Package Managing
# pip show plotly
    # Version: 6.5.1
# Why do we use a requirements.txt file?
    # It lists all the packages and third-party tools needed for the project. 
    # This is helpful for individual tracking, but it is also important for collaborating or
    # sharing the project so others can recreate the exact same environment to run the code