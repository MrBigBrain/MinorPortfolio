# Personal Portfolio
This is The Portfolio from the minor Applied Data Science of Levy Duivenvoorden (18005152).<br/>
Team members: Niels (Nelis), Niels, Amin en Jefry.<br/>

# Project definition
We are team Zero and we work with our problem owner, mr. Rahola (He was also the problem owner of Brian).<br/>
The task that was given is to see if it is possible to predict the electricity production and consumption one day in advance on hourly resolution.<br/>
## onderzoeksvraag
The more specific research question is:<br/>
What is a suitable machine learning model to predict energy use & production of a “zero at the meter” residential house, one day in advance with (if possible) an hourly resolution?<br/>
## literature review
We did an individual literature study in the first weeks, and afterwards we came together and concluded which were the best.<br/>
We all delivered 3 papers with high potential. After which we all red the best papers. The papers were ranked in excel: <br/>
![LiteratureStudyAllSources](literaturePapersWeek5.xlsx)
After this we found some papers, however we found out that there aren't many papers that looks like our research.<br/>
Around week 10 we concluded that more literature was needed to find the best model to make.<br/>
I found three papers that had interesting results:<br/>
- The paper below uses an Neural Network (MLP) and three forms of LSTM to predict two hours in the future. The paper also shows all of the steps taken to come to the conclusion. The conclusion is that an LSTM works better than an NN (MLP).<br/>
![ANN_and_3_LSTM_forms](ANN_+_3_types_of_LSTM_with_clear_feature_selection.pdf)<br/>
- The paper below makes an new form of LSTM, the CNN-LSTM. This means that before the data is given to the LSTM the data is put through an CNN layer. This layer is mostly used in image and audio processing. The paper concluded that this greatly benefits the results, it is the best compared to all other methods.<br/>
![CNN_LSTM_combination](CNN-LSTM_combination.pdf)<br/>
- The paper below is from two years ago. The paper is an overview about all the used methods in the past to predict energy consumption. The conclusion is that SVR and LSTM work best, but the implementation scenario greatly influences the model to use.<br/>
![overview_paper](overview_of_prediction_consumption.pdf)<br/>
<br/>
After doing this research the conclusion is that LSTM works best and can be made in the short time of the minor. But for comparison a MVLR, NN (MLP) and a SVR will be made.<br/>
¬

### Data preprocessing<br/>
In the first weeks we got the dat in Excel format. The total size was around 9 GigaBytes.<br/>
Due to the rather large size loading was cumbersome. Therefore we discussed the best data format to put the data in.<br/>
It was concluded that seperating the data in numpy dataframes. I made the program to do this.<br/>
![ExcelToNumpyConversion](Convert_Excel_tp_Numpy.pdf)<br/>
The program loads the Excel file in an pandas dataframe. Whereafter it splits it up in numpy files, for every house and sheet combination one file.<br/>
After running the program, around 3600 numpy files have been generated. This greatly reduces the loading times.<br/>
<br/>
Nelis (Niels van Schaik) made a simple program to load in the numpy data in an dataframe.<br/>
This makes the program run a lot faster.<br/>
<br/>
After making an dataloader function, it was concluded that the timestamps were inconsistent. This needed to get fixed.<br/>
We had an Brainstorm session about it (with our problem owner), whereafter we concluded that resampling to one hour works best.<br/>
This was done by taking the differences in the values and then resampling to one hour by taking the sum of that hour.<br/>
The script wherein this happens was written by Nelis (Niels van Schaick).<br/>
![LoadingScript](Load_data.py)<br/>
<br/>
After this the team found out that most of the houses had huge datagaps in them.<br/>
To visualize these gaps an heatmap was made by Niels and I.<br/>
The heatmap shown in the program below makes it easy to select the right houses.<br/>
![Heatmap_Program](Heatmap_np.pdf)<br/>
<br/>
The method for splitting the data into training validating and testing was an big problem due to the seasonal patterns.<br/>
Therefore an Brainstorming session was held with the entire Team to discuss this.<br/>
We decided (after a few weeks) to stick with 60 percent training, 30 percent validation and 10 percent training. All in chronological order.<br/>
<br/>
After choosing the right datasets and the right models it was chosen to begin with the most simple models.<br/>
These are the MVLR and SVR (firstly only for production), I worked alone on the SVR.<br/>
Below is the SVR that I made: (the MVLR was made by Niels and Jefry.)<br/>
![SVR_model](W9_SVR_L.pdf)<br/>
<br/>
After this we all had the machine learning part done.<br/>
So it was time to move on to the deep learning part.<br/>
We started with an simple Neural Network (MLP), which we coded as an team in one day.<br/>
It took a few weeks to optimize the MLP, the final (optimized) version is below:<br/>
![NN_model](W12_NeuralNetwork-Copy8.pdf)<br/>
<br/>
The feature selection was done in an brainstorming session with the whole team.<br/>
When the best features were selected the datasets were made by Jefry.<br/>
(Link is in Jefry's portfolio.)<br/>
<br/>
After the Neural Network, the LSTM was realised. This was my task.<br/>
The first time I made the LSTM by repurposing an example notebook from Brian.<br/>
This however proved hard to do and it hadn't the expected outcome.<br/>
![ComplexLSTM_Levy](W12_NeuralNetwork-Copy8.pdf)<br/>
One week thereafter mr. Vuurens held an presentation about LSTM's.<br/>
Therefore it was chosen to scrap the last version of the LSTM and remake the LSTM in an simpler form.<br/>
Jefry and Niels worked on this much simpler LSTM, and after a few weeks of optimizing the LSTM was ready:<br/>
![Simple_LSTM](W15_LSTMConsumptionSimpleV14.pdf)<br/>
I adviced sometimes in the process of making this LSTM.<br/>
<br/>
We found out that peaks were a big problem in the data.<br/>
Nelis (Niels van Schaick) made an program to detect the peaks using the standarddeviation.<br/>
(The program is in his portfolio.)<br/>
<br/>

### chosen models
The models that were discussed before were for only one house. Of course we have 120 houses.<br/>
Thus with the help of Niels program 12 of the 120 houses have few datagaps bigger than 1 hour in 2019.<br/>
All of the models (SVR,MVLR,MLP(NN),LSTM) had to be ported to be used on all 12 houses.<br/>
Firstly Jefry provided the Datasets needed for all of the houses (more info in his portfolio).<br/>
After this I made an program that tests all of the houses in one big program, this however had problems.<br/>
![AllModelsOneScript](W16_AllInOne_TestProgram-Copy2.pdf)<br/>
The first is that the program isn't easily readable and it is to complex.<br/>
<br/>
After this mistake, all of the programs were seperated. One notebook for every model (4x) and consumption/production (2x) combination.<br/>
Below are all eight of these programs. All of the parameters were selected by Niels for one house.<br/>
It took around two full weeks to get the program right without any mistakes. Niels helped in this process.<br/>
<br>
**MVLR**<br>
This model is the easiest model of all the models, it takes the selected features and tries to predict the next day consumption.<br/>
The parameters weren't changed in this program. It performed all right, below is the total program:<br/>
![MVLR_consumption](W16_MVLR_MultipleHouses_consumption.pdf)<br>
![MVLR_production](W16_MVLR_MultipleHouses_production.pdf)<br>
<br/>
**SVR**<br>
This model had already been made by me weeks ago, therefore making it again was very easy.<br/>
The model performed slightly better than the MVLR, with no parameter changes:<br/>
![SVR_consumption](W16_SVR_MultipleHouses_consumption.pdf)<br>
![SVR_production](W16_SVR_MultipleHouses_production.pdf)<br>
<br/>
**NN (MLP)**<br>
The NN performed way worse than the MVLR. It looks like it can't find the patterns in the data.<br/>
This might be due to the non stationairity of the data.<br/>
![NN_consumption](W16_NN_MultipleHouses_consumption.pdf)<br>
![NN_production](W16_NN_MultipleHouses_production.pdf)<br>
<br/>
**LSTM**<br>
The LSTM performed the best of all models, it found the general daily pattern.<br/>
This is probably due to the remembering capabilities of the model.<br/>
![LSTM_consumption](W16_LSTM_MultipleHouses_consumption.pdf)<br>
![LSTM_production](W16_LSTM_MultipleHouses_production.pdf)<br>
<br/>
Every model is being reset at the beginning of training of the house.<br/>
¬
### Results


## conclusion
Therefore we can conclude that LSTM is the best of the considered models thus far.<br/>
There might be room for improvement due to the literature found than an CNN-LSTM outperformed the LSTM by around 30 percent.<br/>
However currently the results show that the MVLR performs best on the production data.<br/>
So there is room for improvement by making an LSTM that is better trained.<br/>
<br/>
# written code (notebooks)
The code that has been written will be here.
Only the general purpose of the notebook.
## DataCamp exercizes
Below are the mendatory DataCamp Courses:¬

![Datacamp](MendatoryDatacampCourses.png)
¬

The Extra DataCamp courses me (and the other Teammembers) did:
- Time Series Analysis in Python
- Visualizing Time Series Data in Python
- Manipulating Time Series Data in Python
- ARIMA Models in Python
- Machine Learning for Time Series Data in Python
## learned functions
All the learned methods in data science will be here.
With respect to the written code.

# Group effort
## Feature selection
What features were selected?<br/>
## General overview
The general plan will be stated here.<br/>
### planning
Every week we came together to make an sprint planning for the next week.<br/>
## presentations
Which presentations did I give?<br/>
## reflections
What did I learn this minor...<br/>

# Terminalogical (complex jargon)

END THINGS TO DO:<br/>
- check links.<br/>
- Make as short and specific as possible.<br/>
- check if the big picture is clear.<br/>
- Relation between the lectures and presentations and the problem.<br/>
- clear contribution per team member of each notebooks.<br/>
