<a href="https://freeimage.host/"><img src="https://iili.io/Hk8jhaR.png" alt="Hk8jhaR.png" border="0"></a><br /><a target='_blank' href='https://freeimage.host/'></a><br />

AI-enabled Phishing link Detection and Alert System.
<h1>Table of content </h1>
<ul>
<li>Introduction.</li>
<li>Insallation.</li>
<li>Directory Tree.</li>
<li>Terminology used<.li>
<li>Result.</li>
<li>Conclusion.</li>
</ul>
<h2>INTRODUCTION</h2>
<p>
With the increasing number of crime the crime detection tools has also increased at an alarming rate.On the 3rd of March, the economic times of India mentioned that:- 
                About 30 crore people are vulnerable to phishing attacks in India, of which 5 lakh potentially fall prey to scamsters.That's why we came up with the idea of PhishSleuth.It is a Phishing Links Detection and Alert system is to help individuals and organizations protect themselves from phising attacks. Phishing attacks are a common and growing threat to personal and business security, and they can result in the loss of sensitive information, financial loss, and other consequences. BY developing a solution that can detect and alert users of potential phishing attacks across vsrious digital channels, we can provide an additional layer of security and protection attacks across various digital channels, we can provide an additional layer of security and protection. Ultimately, the goal of developing  a solution like this is to empower individuals and organixations to protect themselves from phishing attacks and minimize the risk of data breaches, financial loss, and other negative consequences.
  
  <div style="display: flex; justify-content: left;">
   <img src="https://iili.io/Hk8lARs.md.png" alt="Description of image 2" style="width: 1068px; height: 453px; margin-right: 30px;">
   <img src="https://iili.io/Hk8luJn.md.png" alt="Description of image 3" style="width: 1068px; height: 453px;">
   <img src="https://iili.io/Hk8cWnp.md.png"  alt="Description of image 3" style="width: 515px; height: 573px;">
    <img src="https://iili.io/Hk8MaFp.md.png" alt="Description of image 2" style="width: 768px; height: 342px; margin-right: 10px;">
   </div>
   <div style="display: flex; justify-content: left;">
  </div>

</p>
<h2>Installation</h2>
<ol>
  <li> Download the zip file and unzip the the file in a particular folder.</li>
<li> Go the chrome  seetings manage extensions. </li> 
<li> Now turn on developer mode.</li>
<li> Select load unpacked and import mainfiest content from the folder.</li>
</ol>

<h2>Directory tree</h2>
<p>
|-backend<br>
|    |-classifier<br>
|    |-datasets<br>
|-frontend<br>
|   |-icons<br>
|   |-js<br>
|   |-manifest.json<br>
|   |-plugin_ui.css<br>
|   |-plugin_ui.html<br>
|   |-tempstorage.json<br>
|   |-test.html<br>
|-static<br>
|   |-classifier.json<br>
|   |-testdata.json</p>


<h3>Terminology Used</h3>
<p><ul>
<li>Support Vector Machine (SVM)-<br>Support vector machines (SVMs) is used for theclassi¿cation of both linear and nonlinear data.</li>

<li>Decision Tree-<br>A decision tree is a directed, acyclic graph with
two types of nodes, namely; internal nodes that represents a test and terminal node holds a class label.</li>

<li>K-Nearest Neighbour-<br>These are distance-based comparisons that intrinsically assign equal weights to each attribute.</li>
<li>Rotation Forest (RoF)-<br> Rotation Forest (RoF) is an ensemble classifier in which the training data is created by randomly
splitting the feature set into K subsets and Principal.</li>
  <li>Component Analysis (PCA) is applied to each subset for any base classifier.</li>

<li>Random Forests (RF)-<br>Random Forests can be built in tandem with random attribute selection using bagging. Random Forests follow an ensemble approach to learning, that is a divide and
  conquer approach for improving performance.</li>
</ul></p>

<h3>Result </h3>
<p>Accuracy of various model used for Phishing detection</p>
<table>
  <tr>
    <th></th>
    <th>ML Model</th>
    <th>Accuracy</th>
    <th>f1_score</th>
    <th>Recall</th>
    <th>Precision</th>
  </tr>
  <tr>
     <td>0</td>
     <td>Rotation Forest (RoF)</td>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
   <tr>
     <td>1</td>
     <td>Random Forests(RF)</td>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
   <tr>
     <td>3</td>
     <td>	Support Vector Machine</td>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
   <tr>
     <td>4</td>
     <td>Decision Tree</td>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>5</td>
     <td>K-Nearest Neighbour</td>
     <td></td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  
 </table>
 <h3>Conclusion</h3>
 <p>The final take away form this project is to explore various machine learning models, perform Exploratory Data Analysis on phishing dataset and understanding their features.
Gradient Boosting Classifier currectly classify URL upto 95.6% respective classes and hence reduces the chance of malicious attachments.</p>
