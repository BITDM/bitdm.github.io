
Relational Retrieval Using Random Walk With Restart(RWR)
Project Proposal

Main idea
Basically, the project will rely on retrieving the data from specific resources or dataset and implement some tasks to get the accurate results of the specified dataset to create the required queries which will help researchers in different domains such as Biological domain to get related scientific papers easier and finding the related scientific papers in a fast way. 
Relational retrieval means obtaining data from specific resources and this data is related with the data in the other sources to get the common model of that data.
Dataset
The data in our project, is a dataset which is in the format of “ .FLY  “ this dataset a biological literature graph which is an integrated database for Drosophila and Anopheles genomics, and contains about 127K papers tagged with genes and proteins.

In the beginning we will start by studying and analyzing the dataset to build the graph which will enable us to understand the main relations between the different entities in the schema .

In fact, scientific literature for example “.FLY”  naturally includes substantial metadata such as author names, citations, and publication venues, as well as derived metadata (such as gene and protein names, in the biomedical literature). The way to represent the scientific literature is as a labeled directed graph, with typed nodes representing documents, terms, and metadata, and labeled edges representing the relationships between them (e.g., “authorOf”, “datePublished”, etc).





Building Graph

Representing the scientific literature as a labeled graph enables a number of scientific tasks to be formulated as typed proximity queries in the graph, in which the user provides as input a set of query nodes and answer type, and receives as output a list of nodes of the desired answer type, ordered by proximity to the query nodes.
The graph will be constructed by using the dataset of which the project is based on. The dataset will be formulated in matrix in order to add the dataset in a database.

Then after building the graph , we will use the typed proximity queries to implement these tasks : 

•	suggest related work to author 
•	retrieve relevant papers given some key words. 
These tasks can be formulated as relational retrieval tasks in the graph .


Method 

We will use  Random with Restart Walk (RWR) which is a general-purpose graph proximity measure and fairly successful for many types of tasks. provides a good relevance  score  between  two  nodes  in  a  weighted  graph, and  it  has  been  successfully  used  in  numerous  settings, like  automatic  captioning  of  images,  generalizations  to the “connection sub graphs”, personalized PageRank, and many more. The implementations of  RWR  do  not  scale  for  large  graphs,  requiring  either quadratic space and cubic pre-computation time,  or slow response time on queries.
