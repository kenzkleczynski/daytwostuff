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

# %% Recipe

# 1. Creating Repo
    # 1.1 Fork someone's or create a new repository
    # 1.2 Open the repository in Codespaces
        # Within the github repo click on the green "Code" button and select Codepaces
        # Then click on the "Create new codespace" button
        # Then click three dots and click "Open in Visual Studio Code"
# 2. Create Virtual Environment
    # 2.1 In the terminal, run the command: python3 -m venv .venv
    # 2.2 Activate the virtual environment: source .venv/bin/activate
# 3 Install the packages
    # 3.1  Install what you need for your project using pip install <package-name> in the terminal
# 4. Create the requirements.txt file
    # 4.1 In the terminal, run the command: pip freeze > requirements.txt 
         # This can be used to create the file the first time you run it, 
         # but should also be run every time you add a new package to keep the file up to date
# 5. Commit and Push your changes to the repository
    # 5.1 In the terminal, run the command: git add .
    # 5.2 Then run: git commit -m "Your commit message here"
    # 5.3 Then run: git push origin main


# Example following recipe: https://github.com/kenzkleczynski/DS3021---lab2