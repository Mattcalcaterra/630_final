<p align="center">
    <h1 align="center">PRESCRIPTION ADVICE EXTRACTION</h1>
</p>
<p align="center">
    <em>Leveraging information exctraction and multi-class labeling in prescription drug handouts</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/Mattcalcaterra/prescriptionAdviceExtraction?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Mattcalcaterra/prescriptionAdviceExtraction?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Mattcalcaterra/prescriptionAdviceExtraction?style=flat&color=0080ff" alt="repo-language-count">
<p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)

---

##  Overview

Medical documentation can often be dense with complex terms which are difficult for patients to read and interpret. This can cause confusion and decreased education for patients. The application of natural language processing (NLP) techniques and models have the potential to create more easily understandable advice for patient. Two model systems were deployed to handle the tasks of extracting specific advice from medication handouts and labeling the advice with different categories. 

A variety of binary relevance models and a transformer based roBERTa model proved to be sufficient for advice labeling. The results further indicated that labeling of advice for patient could be done efficiently with low computational overhead. 

The deployment of transformer-based models for advice extraction from raw handout text showed results indicating that they could be viable to patient implementation, however further interactions and refinements will be needed first. BIOE tagging was used to indicate the position of advice in the text, and predict advice position. Condition random field layers added on top of the base transformer models show positive increases in the performance of advice extract, and post-processing treatment of the model predictions could potentially increase this further.

With further refinement of the model processes, the advice extraction and labeling could be combined into a single pipeline for handout extraction and labeling. This would prove to be a pivotal application of NLP for patient implementation to improve health education and outcomes.

A full write up of the project can be found in the [technical report](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/technicalReport.pdf).

---

##  Features

- **Advice Labeling**
    - Randomized Baseline
        - Random selection of labels was used to set a baseline for the multi-class labeling of the annotated data
    - Binary Relevance
        - Three models were created to predict the presence of each label without considering the presence of other labels
            - Logistic Regression
            - SVC
            - K-Nearest Neighbors
    - roBERTa Model
        - A transformer-based model was created to predict the presence of each label without considering the presence of other labels

- **Advice Extraction**
    - BIOE Tagging
        - A tagging system was used to indicate the position of advice in the text
        - The tags were generated by locating the advice spans from the annotated data within the lines of the raw data
    - Randomized Baseline
        - Random selection of advice spans was used to set a baseline for the advice extraction from the raw data
        - The baseline was evaluated at a token-level and span-level
    - roBERTa Model
        - A roBERTa model was fine-tuned for the downstream task of advice extraction via BIOE tagging
        - A CRF layer was added on top of the base model to improve the performance of the advice extraction
        - The loss function was modified to account for the BIOE tagging scheme and the unequal distribution of advice labels
        - The model was evaluated at a token-level and span-level, both with and without the CRF layer
    - post-processing
        - The model predictions were post-processed to improve the performance of the advice extraction
        - The the predictions of the model were compared with and without post-processing

---

##  Repository Structure

```sh
└── prescriptionAdviceExtraction/
    ├── data
    │   ├── AnnotatedData
    │   ├── RawData
    │   └── results
    ├── technicalReport.pdf
    ├── data_viewing.ipynb
    ├── adviceLabeling.ipynb
    └── informationExtraction.ipynb
```

---

##  Modules

<summary>Technical Report</summary>

<details closed><summary>Data</summary>

| File                                                                                                                                  | Summary                                                 |
| ---                                                                                                                                   | ---                                                     |
| [AnnotatedData](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/AnnotatedData)                   | Contains annotated prescription handout text data, indicating specific segments of advice with corresponding labels |
| [RawData](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/RawData) | Contains raw handout text files for 92 classes of drugs |
| [results](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/results)               | Model performance results data        |

</details>

<details closed><summary>Notebooks</summary>

| File                                                                                                                                  | Summary                                                 |
| ---                                                                                                                                   | ---                                                     |
| [data_viewing.ipynb](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/data_viewing.ipynb)                   | Notebook setup to create visualizations of the model results data          |
| [informationExtraction.ipynb](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/informationExtraction.ipynb) | Data pre-processing, label generation, baseline generation, model creation, and model evaluation for advice extraction from the raw data |
| [adviceLabeling.ipynb](https://github.com/Mattcalcaterra/prescriptionAdviceExtraction/blob/master/adviceLabeling.ipynb)               | Data pre-processing, baseline generation, model creation, and model evaluation and comparison for the multi-class labeling of the annotated data        |

</details>

---

[**Return**](#-quick-links)

---