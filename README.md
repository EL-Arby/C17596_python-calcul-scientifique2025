<<<<<<< HEAD
# FD_2025
=======
Mini_Projet 
Formation doctorale de l'Université de Nouakchott




This readme file was generated on 2025-06-02 by Mohamed EL Moustapha CHRIF

-
#  GENERAL INFORMATION
-

1. Title:  Mini-Project for Sentiment Analysis applied on HASSANIYA Dialect 


2. contact

Name: Mohamed EL Moustapha CHRIF
ORCID: 0000-0001-6107-8766
Institution: Department of Computer Science, Faculty of Science and Technology, University of Nouakchott
Email: arbimoustapha01@gmail.com

Institution: Department of Computer Science, Faculty of Sciences Dhar El Mahraz, Sidi Mohamed Ben Abdellah University
Email: mohamedelmoustapha.chrif@usmba.ac.ma




 

4. Description of the dataset:
This dataset represents the first publicly available version designed to address the lack of HASSANIYA dialect resources and advance research in the field of natural language processing.

HASSANIYA is one of the standard Arabic, various, dialects. In addition to Mauritania, it is spoken along the Sahel region, within several states including Southern Morocco, Algeria, Mali, Niger, and some areas of Libya. Mauritania, however, could be considered as the cradle of this dialect compared to its neighboring countries. It is estimated that about 80% of the Mauritanian citizens speak HASSANIYA in their daily life.  
The Mauritanian version of HASSANIYA is spoken with different accents, but each is slightly distinct from one another. The Eastern, Western and Northen citizens’ accents and style are still recognizable despite approximately the over 98% similarities in everything between the different regions. Sometimes those differences melt away, in case the speaker is grown up in one of the big cities like Nouakchott.
 Like any other language or dialect, the cross-culture influence such as the number of borrowed words, neighborhood, and borders with none Arab states, etc. has affected the dialect at different levels that might include: phonology, morphology, semantics and syntax. Therefore, it is important to emphasize that this diversity shows one of the complexities of the HASSANIYA dialect, and so will be the nature of any research that targets this dialect. Subsequently, the data could help data scientist researchers fill the gap in natural language models specific to this dialect.

The dataset represents the first and only data available in the HASSANIYA dialect. It consists of 1851 records extracted from relevant comments published on Facebook.


5. Date of data collection: The dataset was gathered in two phases: a preliminary collection in June–July 2021, followed by a more extensive compilation spanning March 2023 – August 2024.


-
# SHARING/ACCESS INFORMATION
-


1. Data sources: Social media, notably Facebook pages.

2. Dataset citation: El ARBY, Med El Moustapha (2025), “HASSANIYA-DTCD: A new Dataset for Benchmarking Text Classification Tasks on HASSANIYA Dialect”, Mendeley Data, V1, doi: 10.17632/r5k9ktwr4g.1

https://data.mendeley.com/datasets/m2swkr2bhx/1



-
# DATA & FILE OVERVIEW
-

Filename: TD_TF
Description: contains the correction of TD and TP. 

Filename: Mini_Projet
Description: contains a Python script used to implement the SVM technique to classify HASSANIYA data into three categories: positive, negative and neutral.

Filename: hassaniya-preprocessing
format: (.ipynb)
Description: contains the script(python) used to preprocess the data, such as removing stop words, punctuation, and duplication.




-
Data-specific information for: Mini_project
-

1.  Number of instances: 1851

2.  Number of rows: 1853

4.  Number of classes: 3
	• Positive
	• Negative
	• Neutral

5.  Attribute list: 
	
	•  id: a unique identifier for each comment
	•  annotation: Indicates whether the entry has been annotated (1) or not (0)
	•  created_at: the timestamp when the comment was stored
	•  text: the full content of the comment
	•  annotation_result: Assigned sentiment label (positive, negative, or neutral)


# METHODOLOGICAL INFORMATION

-
Description of methods used for data preparation:
-

The dataset preparation process proceeded through the following key steps:

1. Data collection: We gathered high-quality data from multiple sources, restricting our selection to the Facebook pages of prominent individuals—bloggers, public officials, and political leaders (e.g., presidential and ministerial pages)—to ensure relevance, credibility, and topical diversity. 


2. Record verification: We reviewed each entry individually to confirm that its content was both pertinent and objective. 


3. Annotation: The research team—leveraging its expertise in the HASSANIYA dialect and regional sociolinguistic norms—guided the annotation process; ambiguous cases were resolved by consulting Modern Standard Arabic as a neutral reference, Additionally, annotators represented two distinct regional backgrounds to ensure diverse perspectives during the annotation process.


4.  Pre-processing is an important step in preparing data for analysis. It consists of data cleaning, transformation, and integration. The necessary library to clean data was dedicated to removing non-Arabic words, spaces, punctuation, stopwords, etc.
The library needed for data cleaning was used to: clean and normalize text, remove repetitions, remove non-Arabic, and remove Hassaniya_stopwords listed in the attached file (see attached file in IPython Notebook format ).


-
# Software-specific information needed to analyze the data
-



1. The packages and libraries needed to run scripts are listed in the attached file (IPython Notebook format ).


2. Environmental/Tools: 
	- Kaggle: We used the Kaggle platform to implement our experiment.  
	- Web scraper used to gather comments from Facebook pages.
	- Label Studio is used to annotate each entry.
2. Library: 
	- Numpy
	 - Pandas
	 - Sklearn
	 - nltk
	
 
-
Acknowledgements
-

This README file template is adapted from the following source: https://data.research.cornell.edu/content/readme#bestpractices
>>>>>>> 34cb976 (first commit)
