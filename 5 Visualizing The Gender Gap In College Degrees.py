#!/usr/bin/env python
# coding: utf-8

# ## Introduction

# ### Visualizing the gender gap across STEM degrees through line charts

# To make the viewing experience more coherent, we can:
# 
# * use layout of a single row with multiple columns
# * order the plots in decreasing order of initial (1968) or recent (2011) gender gap

# If we're instead interested in the recent gender gaps in STEM degrees, we can order the plots from largest to smallest ending gender gaps.
# 
# We thus populate the list `stem_cats` with the six STEM degree categories, ordering them by decreasing ending gender gap as observed in plots from earlier mission.

# We'll replace the legend with text annotations, which would otherwise overlap with the rightmost line chart.
# 
# Legends consist of non-data ink and take up precious space that could be used for the visualizations themselves (data-ink).
# 
# Instead of trying to move the legend to a better location, we can replace it entirely by annotating the lines directly with the corresponding genders.

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

# Set the line color for the line charts visualizing women percentages to the dark blue color 
# from the Color Blind 10 palette (RGB value of (0, 107, 164))
cb_dark_blue = (0/255,107/255,164/255)

# Set the line color for the line charts visualizing men percentages to the orange color 
# from the Color Blind 10 palette (RGB value of (255, 128, 14))
cb_orange = (255/255, 128/255, 14/255)

# enlisting `stem_cats` with the six STEM degree categories, ordering them by decreasing ending gender gap
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

# annotating just the leftmost and the rightmost line charts
# prioritizing data-ink ratio over the consistency of elements
# add text annotations to plot by using Axes.text() method 

    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()


# We have improved the viewing experience by making our plots more color-blind friendly and thickening the line widths. 
# We used the layout and ordering of the plots as well annotations directly onto the plots to enhance the story that's being told to the viewer.

# ### Visualizing the gender gap across all college degree categories through line charts for comparison.

# Because there are seventeen degrees that we need to generate line charts for, we'll use a subplot grid layout of 6 rows by 3 columns. We can then group the degrees into STEM, liberal arts, and other.

# In[3]:


stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']


# While in the previous plot, the `stem_cats` list was ordered by ending gender gap, all three of these lists are ordered in descending order by the percentage of degrees awarded to women. 
# While `stem_cats` and `other_cats` have six degree categories as elements, `lib_arts_cats` only has five.

# In[4]:


fig = plt.figure(figsize=(16, 20))

# Generate first column of line charts for both male and female percentages for every degree in `stem_cats`
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

# Add text annotations for Women and Men in the topmost and bottommost plots.    
    if cat_index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif cat_index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')

# Generate second column of line charts for both male and female percentages for every degree in `lib_arts_cats`
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off")

# Add text annotations for Women and Men for only the topmost plot (since the lines overlap at the end in the bottommost plot)    
    if cat_index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')

# Generate third column of line charts for both male and female percentages for every degree in `other_cats`
for sp in range(2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
# Add text annotations for Women and Men in the topmost and bottommost plots
    if cat_index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 30, 'Women')
        
plt.show()


# With seventeen line charts in one diagram, the non-data elements quickly clutter the field of view. The most immediate issue that sticks out is the titles of some line charts overlapping with the x-axis labels for the line chart above it. If we remove the titles for each line chart, the viewer won't know what degree each line chart refers to. Let's instead remove the x-axis labels for every line chart in a column except for the bottom most one. We can accomplish this by modifying the call to `Axes.tick_params()` and setting `labelbottom` to `off`.

# #### Hiding x-axis labels

# In[5]:


fig = plt.figure(figsize=(16, 16))

# Generate first column of line charts for both male and female percentages for every degree in `stem_cats`
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[cat_index])
    # Disable the x-axis labels for all line charts in first column
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')

# Add text annotations for Women and Men in the topmost and bottommost plots      
    if cat_index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif cat_index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        # Enable the x-axis labels for bottommost line chart in first column
        ax.tick_params(labelbottom='on')

# Generate second column of line charts for both male and female percentages for every degree in `lib_arts_cats`
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[cat_index])
    # Disable the x-axis labels for all line charts in second column
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')

# Add text annotations for Women and Men for only the topmost plot (since the lines overlap at the end in the bottommost plot)    
    if cat_index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif cat_index == 4:
        # Enable the x-axis labels for bottommost line chart in second column
        ax.tick_params(labelbottom='on')

# Generate third column of line charts for both male and female percentages for every degree in `other_cats`
for sp in range(2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[cat_index])
    # Disable the x-axis labels for all line charts in third column
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')

# Add text annotations for Women and Men in the topmost and bottommost plots    
    if cat_index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 30, 'Women')
        # Enable the x-axis labels for bottommost line chart in third column
        ax.tick_params(labelbottom='on')
        
plt.show()


# Removing the x-axis labels for all but the bottommost plots solved the issue we noticed with the overlapping text. In addition, the plots are cleaner and more readable. The trade-off we made is that it's now more difficult for the viewer to discern approximately which years some interesting changes in trends may have happened. This is acceptable because we're primarily interested in enabling the viewer to quickly get a high level understanding of which degrees are prone to gender imbalance and how that has changed over time.
# 
# In the vein of reducing cluttering, let's also simplify the y-axis labels. Currently, all seventeen plots have six y-axis labels and even though they are consistent across the plots, they still add to the visual clutter. By keeping just the starting and ending labels (0 and 100), we can keep some of the benefits of having the y-axis labels to begin with.
# 
# We can use the `Axes.set_yticks()` method to specify which labels we want displayed.

# #### Setting y-axis labels

# In[6]:


fig = plt.figure(figsize=(16, 16))

# Generate first column of line charts for both male and female percentages for every degree in `stem_cats`
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[cat_index])
    # Disable the x-axis labels for all line charts in first column
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    # For all plots in first column enable just the y-axis labels at 0 and 100
    ax.set_yticks([0,100])

# Add text annotations for Women and Men in the topmost and bottommost plots  
    if cat_index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif cat_index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
         # Enable the x-axis labels for bottommost line chart in first column
        ax.tick_params(labelbottom='on')

# Generate second column of line charts for both male and female percentages for every degree in `lib_arts_cats`
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[cat_index])
    # Disable the x-axis labels for all line charts in second column
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    # For all plots in first column enable just the y-axis labels at 0 and 100
    ax.set_yticks([0,100])

# Add text annotations for Women and Men for only the topmost plot (since the lines overlap at the end in the bottommost plot)    
    if cat_index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif cat_index == 4:
        # Enable the x-axis labels for bottommost line chart in third column
        ax.tick_params(labelbottom='on')

# Generate third column of line charts for both male and female percentages for every degree in `other_cats`
for sp in range(2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[cat_index])
    # Disable the x-axis labels for all line charts in third column
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])

# Add text annotations for Women and Men in the topmost and bottommost plots    
    if cat_index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 30, 'Women')
        # Enable the x-axis labels for bottommost line chart in third column
        ax.tick_params(labelbottom='on')
        
plt.show()


# While removing most of the y-axis labels definitely reduced clutter, it also made it hard to understand which degrees have close to 50-50 gender breakdown. While keeping all of the y-axis labels would have made it easier, we can actually do one better and use a horizontal line across all of the line charts where the y-axis label 50 would have been.

# We can generate a horizontal line across an entire subplot using the `Axes.axhline()` method. The only required parameter is the y-axis location for the start of the line which is 50 in our case.

# #### Adding a horizontal line

# Let's use the color in the Color Blind 10 palette for this horizontal line, which has an RGB value of (171, 171, 171). Because we don't want this line to clutter the viewing experience, let's increase the transparency of the line. We can set the color using the c parameter and the transparency using the alpha parameter. The value passed in to the alpha parameter must range between 0 and 1.

# In[7]:


fig = plt.figure(figsize=(16, 16))

# Generate first column of line charts for both male and female percentages for every degree in `stem_cats`
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])
    # Generate a horizontal line which starts at the y-axis position 50
    # Set to the third color (light gray) in the Color Blind 10 palette
    # Has a transparency of 0.3
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    
    if cat_index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif cat_index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom='on')

# Generate second column of line charts for both male and female percentages for every degree in `lib_arts_cats`
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])
    # Generate a horizontal line which starts at the y-axis position 50
    # Set to the third color (light gray) in the Color Blind 10 palette
    # Has a transparency of 0.3
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    
    if cat_index == 0:
        ax.text(2003, 78, 'Women')
        ax.text(2005, 18, 'Men')
    elif cat_index == 4:
        ax.tick_params(labelbottom='on')

# Generate third column of line charts for both male and female percentages for every degree in `other_cats`
for sp in range(2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.set_yticks([0,100])
    # Generate a horizontal line which starts at the y-axis position 50
    # Set to the third color (light gray) in the Color Blind 10 palette
    # Has a transparency of 0.3
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    
    if cat_index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 30, 'Women')
        ax.tick_params(labelbottom='on')
        
plt.show()


# Matplotlib can be used many different ways. It can be used within a Jupyter Notebook interface (like this one), from the command line, or in an integrated development environment. Many of these ways of using matplotlib vary in workflow and handle the rendering of images differently as well. To help support these different use cases, matplotlib can target different outputs or backends. If we import matplotlib and run `matplotlib.get_backend()`, we'll see the specific backend we are currently using.

# In[12]:


import matplotlib
matplotlib.get_backend()


# With the current backend we're using, we can use `Figure.savefig()` or `pyplot.savefig()` to export all of the plots contained in the figure as a single image file. These have to be called before we display the figure using pyplot.show() .

# #### Exporting to a file

# We will now export the figure containing all of the line charts to "gender_degrees.png" .

# In[7]:


# Set backend to Agg.
fig = plt.figure(figsize=(16, 16))

# Generate first column of line charts for both male and female percentages for every degree in `stem_cats`
for sp in range(0,18,3):
    cat_index = int(sp/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.set_yticks([0,100])
    
    if cat_index == 0:
        ax.text(2003, 85, 'Women')
        ax.text(2005, 10, 'Men')
    elif cat_index == 5:
        ax.text(2005, 87, 'Men')
        ax.text(2003, 7, 'Women')
        ax.tick_params(labelbottom='on')

# Generate second column of line charts for both male and female percentages for every degree in `lib_arts_cats`
for sp in range(1,16,3):
    cat_index = int((sp-1)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(lib_arts_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.set_yticks([0,100])
    
    if cat_index == 0:
        ax.text(2003, 75, 'Women')
        ax.text(2005, 20, 'Men')
    elif cat_index == 4:
        ax.tick_params(labelbottom='on')

# Generate third column of line charts for both male and female percentages for every degree in `other_cats`
for sp in range(2,20,3):
    cat_index = int((sp-2)/3)
    ax = fig.add_subplot(6,3,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[cat_index]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[cat_index]], c=cb_orange, label='Men', linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(other_cats[cat_index])
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    ax.set_yticks([0,100])
    
    if cat_index == 0:
        ax.text(2003, 90, 'Women')
        ax.text(2005, 5, 'Men')
    elif cat_index == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2003, 30, 'Women')
        ax.tick_params(labelbottom='on')

# Export file before calling pyplot.show()
fig.savefig("gender_degrees.png")
plt.show()


# In the above code, we saved a line chart as a PNG file. The image will be exported into the same folder that our Jupyter Notebook server is running. Exporting plots we create using matplotlib allows us to use them in Word documents, Powerpoint presentations, and even in emails.
