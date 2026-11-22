# Module Reflections

## Week 1 Reflections

### Section1

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. How does the notebook format, combining written explanation with live code, compare to tools you currently use at work (e.g. Excel, Word, dashboards)? What are its advantages and limitations? (MLO1)
2. Identify a dataset you work with in your role. Is it closer to raw *data*, an organised *dataset*, or part of a *database*? What would need to change for it to move up a level? Justify your answer (MLO2)
3. Using the METEO dataset as an example, describe one step you could take to move from the DIKUW pyramid *Information* level (a statistic) to the *Knowledge* level (a meaningful insight). What additional context or comparison would you need? (MLO1)

#### Responses

1. In the NHS, specifically in my role, I use Excel, Power BI, SQL, and Python as the basis of my analysis work to present my data. The notebook format is very useful because I can document my code and explain what it does in a structured way, giving full visibility into both the coding, the explanation, and the outputs all in one place. I believe this will help stakeholders understand my process and findings.
I can document the steps I have taken to cleanse data, such as the RTT waiting list data. In comparison with a dashboard where the cleansing could happen in Power Query within the dashboard. 
In order to achieve the same results, I would need one source of the truth (consistent data source). I would use Jupyter Notebook to document and track methods of approach whilst continuing to use Power BI service and dashboards for performance monitoring.


2. The RTT waiting list dataset consists numerous fields that are used to aid, assist and track treatment waiting times. This specific dataset is closer to database. In order produce this report as efficiently as possible, it requires numerous derived columns, and connections via a range of identifiers such as primary and foreign keys in our data warehouse. The next stage would categorically be improvement in the data warehouse.
In terms of the three above, this data cannot move further; it can be improved over time to support the reporting function and the needs of the organisation such as new fields, columns, etc and better integration with the appointments table, e.g., (Date of First Future Appointment, Date of First Investigations), and the use of AI to automate manual validation. However, these improvements would need to be carefully implemented,along with NHS England ethhics and guidlines and validation will still require operational oversight.

3. The one step I would take is to conduct some trend analysis and compare month on month, year on year, location, seasonality, and some data quality metrics based on the average sunshine duration against different locations available, to ensure the data is reliable in its entirety. This would then help me identify any data quality issues within the meteo dataset. With these changes and improvements this will allow my data set to evolve from Information to a meaningful insight."Accumulated data lacks the uniformity and homogeneity often implied in pyramid models, misrepresenting the role of evidence and argument in the construction of knowledge and wisdom". (Peters, Michael A,2024,p.7-17)

References (if applicable):
By:Peters, Michael A.In:Psychosociological Issues in Human Resource Management, 2024, volume 12, issue 2, pages 7-17 (11p)Business Source Elite

---

## Week 2 Reflections

### Section_1

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. When might you store a price field as a text string instead of a decimal? Describe one specific problem that might arise, such as, in a calculation, a report, or a data import, and provide a brief example.

#### Responses

1. In our data warehouse, we store financial data as well as patient data, and in some cases, this is stored financial information from our PLICs system and Income information for SLAM (Service Level Agreement Monitoring). If I were to extract this as a text field and tried to do calculations or mathematical formulas with this it would produce incorrect output or incorrect sums on a financial total, which is detrimental to understanding the organisation's financial position, both expenditure and income. Microsoft (n.d., SUM (Transact-SQL)) explains that the SQL SUM function can only be used with numeric data types.


References (if applicable):

Microsoft (n.d.) SUM (Transact-SQL) – SQL Server. https://learn.microsoft.com/en-us/sql/t-sql/functions/sum-transact-sql

---

### Section_2

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Using this week's distinction between mutable and immutable data, identify one situation in your role where data *should* be protected from change, where accidental modification would cause a problem. Then identify one where it *must* be changeable, where the data needs to be updated to reflect changes and the old value is no longer valid.Does your workplace's current handling of this distinction get the balance right? Justify your view.

#### Responses

1. The DM01 diagnostic data is immutable, as it is published and widely used in the Department of Health insights, so we cannot make changes. I would identify our IP (Inpatient) Waiting list as mutable. Even though the script is maintained due to business needs. It requires daily updates from our data warehouse extract files to establish an updated worklist. This will update the necessary information for the operational teams, which includes waiting times, pathway updates, etc.
My organisation approaches this strategically by storing the snapshots and providing read-only access to staff. This business logic is also managed by in-house change control processes. There have been instances where the stored processes in our SQL Agent jobs have failed due to another process failing in the sequence. These processes have caused inaccuracy in our board reporting at times. This raised the necessary reconciliation tasks for the BI team to maintain integrity and accuracy. “Patient records, treatment histories, and diagnostic results must remain unchanged to ensure accuracy and trust. Immutable data ensures that once information is recorded, it cannot be tampered with, offering a reliable and auditable history.”
Tan, L. (2025) Immutable vs. mutable: The data debate that could define your success. Available at: https://estore.flexxon.com/blogs/immutable-storage/immutable-vs-mutable-the-data-debate-that-could-define-your-success

---

### Section_3

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Describe a situation in your workplace where data moves between formats. For example, from a database to a spreadsheet, or from an API to a report. Why are these conversions necessary? What challenges might arise during this conversion? Think about what information can be lost or changed when moving between, for example, a nested format (JSON) and a flat one (CSV).

#### Responses

1. In my workplace, we use a system called NETCALL as one of our tools for waiting list validation. This will then send a text message on a weekly basis asking patients whether they would like to stay on the relevant waiting list. Once this process is complete, we get the responses via an API call, which we retrieve the responses in a JSON file, which we then convert to a CSV and upload to our data warehouse via an SSIS package. This transformation is necessary to obtain the relevant format to be used and combined with our other datasets. Whilst on this project, numerous issues prolonged completion of the reporting phase. This was due to issues with the special characters in text fields & numerous date formats.

---

### Section_4

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Using this week's normalisation principles, would you defend storing in a medical clinic's appointment datablase the doctor's name in every appointment row, the unnormalised approach? Should it be normalised? Justify your position in terms of what could go wrong, rather than just naming the normal form.

#### Responses

1. I would normalise the appointment database and store the clinicians in a fact table that we could join to. In our Lorenzo system, we had this problem where there were many clinicians' names attached to the same generic medical consultant number, which meant we had multiple names attached to one clinician. In our reporting, this flagged numerous data quality issues. This also affected our slot utilisation by clinician, as the numerator and denominator were affected by the split. By creating a fact table apply one table with a primary key that can join, we can apply the one-to-many join. I would also maintain the historical changes for audit purposes.

---

## Week 3 Reflections

### Section1

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Sometimes 100% completeness or accuracy isn't achievable or cost-effective. What completeness or accuracy threshold would you accept for different business scenarios you encounter in your workplace (e.g., operational reporting vs. strategic planning)?

#### Responses

1. In terms of reporting, we aim for a 99% accuracy threshold, especially when it comes to reporting our waiting list, to provide as much information as possible. There are many critical fields required to produce the RTT Waiting List, such as clock start date, RTT treatment status, referral type, clinical priority code, and RTT week number for tracking. Any inaccuracy in any field could affect clinical and operational decision making. In terms of strategic planning, such as forecasting demand and assembling our trajectories. We allow a tolerance of 95% completeness, as this does not necessarily affect the model in terms of forecasting. In terms of our mandatory submissions, there are cases where we are expected to populate 100% of the fields to comply with the NHS contractual obligations. Completness thresholds should be a case by case scenario among the dataset size, as the percentage matters for the dataset. The accurate recording and reporting of referral to treatment (RTT) waiting times information is extremely important. Patients can and do use this information to inform their choice of where to be referred and also to understand how long they might expect to wait before starting their treatment."The accurate recording and reporting of referral to treatment (RTT) waiting times 
information is extremely important."(NHS England, 2022, p. 4).

References (if applicable):
NHS ENGLAND, 2021. Recording and reporting referral to treatment (RTT) waiting times for consultant-led elective care. London: NHS England. Available from: https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2021/05/Recording-and-Reporting-guidance-April_2021.pdf

---

### Section2

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Which FAIR principle would most improve data sharing in your workplace? What barriers prevent implementing this principle? (MLO2)

2. What role do data management systems play in your workplace's digital and technology solutions? Using an example from your workplace, what are the strenths and challenges you find with the system? Justify your view with reference to one challenge you have encountered implementing, managing, or using it. (MLO1, MLO2)

#### Responses

1. Data sharing in the NHS would improve ease of access (accessibility). Our operational and clinical colleagues require access to data in a timely manage to aid in the assistance of running the services efficiently and effectively. Ensuring everyone has access to the relevant reports would reduce the burden of ad hoc requests that we, the Information/BI Team receive.
This would need to be balance alongside row level security ensuring staff only have access to the necessary information related to their job role and senior approval is granted based on job description. The barriers preventing this implementation would be an additional process, inconsistences around job roles, delayed access and potentially an increase of burden of the Information/BI Team. I’d recommend a Lakehouse of all potential patient identifiable data with an automated access approval flow to ensure less reliance on my team and full accountability & governance of the operational teams.


2. Our systems support our operational reporting through our data warehouse. This supports our Power BI reports which support a range of reports for every aspect of the Trust. One of the strengths is that we have our data centralised so querying makes things so easy over a range of systems. This provides consistent reporting and  a single source of the truth. A challenge that I have faced SQL agent jobs failing because of an earlier process that has failed. This has affected our integrated performance reporting which is used to steer direction over operation decisions. This issue was identified, investigated, and resolved. However, regardless of automation, data warehouse monitoring is just as important. The data warehouse is dependent on numerous daily checks, and SQL alerts. The data warehouse is the centre of our data repository, but its reliability depends on our daily runs being successful. “No matter how well you tune your data warehouse, reliability of data is tantamount to any successful project. And even simple discrepancies can cause serious repercussions when attempting to make well-founded business decisions based on the warehouse data. Krill, P. (1998)”

References (if applicable):

Krill, P. (1998) ‘Data warehouses have need for clean data’, InfoWorld, 16 March. Available at: https://research.ebsco.com/c/m7mrx2/search/details/4mjzqctlkb

---

### Section3

- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*
- **MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Identify a business question in your workplace that requires joining data. Using the join types we have seen in Part 2, which is appropriate, and why would the wrong choice produce a misleading answer?

#### Responses

1. One question that is frequently asked on the RTT waiting list, is how many patients on the PTL have multiple DNA’s (Did Not Attend) and consecutive DNA’s. This is because there is NHS guidance ruling that a patient awaiting their first appointment that has DNA’d consecutively is allowed to be discharged back to the GP. This is a measure in place to aid waiting list reduction.  I would join a temp table of the outpatient appointments by DNA and aggregate a count based on the patientpathwayid and LEFT JOIN on to the RTT PTL. This would give me the full PTL and the aggregate DNA count in one single line. However, if I was to use for an INNER JOIN, this would give me only those records that have DNA’s linked by patientpathwayid and exclude everything else. This would be a misrepresentation of the waiting list size and reduce the accuracy of the PTL. According to NHS England (2022, p. 6), a patient who does not attend their first appointment on an RTT pathway may have their RTT clock nullified and be returned to primary care, provided the relevant clinical and communication requirements are met.



References (if applicable):NHS England (2022) Re-stating RTT Rules: Referral to Treatment Rules Guidance v1.3.

---

## Week 4 Reflections

### Section1

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. This notebook compared quantitative, qualitative and secondary data sources, such as customer feedback, tracked usage figures and published economic statistics. Identify two different sources of data you regularly rely on in your role. What challenges does the diversity of these sources create when you need to gather data for an analysis?

2. Identify a data source you regularly use in your role. What potential sources of bias might affect it? How does this influence your interpretation? You can use one of the sources from question 1 for your answer.

#### Responses

1. Lorenzo, our PAS system, is our quantitative data source, which generates our referrals, waiting lists, outpatient appointments, and admin and clinical information. Qualitative data comes from our divisions and operational teams. In our RTT data especially the validation data that requires operational input for essential pathway validation.   
This qualitive information is not only from pathway validation but also from understanding the bottlenecks that are stopping improvement and treatment waiting times. There are times that the validation has been inconsistent between different validators, inconsistent recording and discharge outcomes. This is critical to highlight potential issues with pathway validation and make decisions on our validation strategy. 


2. As mentioned above, the RTT waiting list may incur a potential source of bias from incomplete information or unvalidated or uncashed outcomes. Patients may have received their treatment, but because outcomes may not be cashed up, their pathway status may no longer represent a true reflection of their pathway. If uncashed outcomes are not cashed in a timely manner, it could inflate the waiting list. NHS England (2025, pg. 74–75) highlights the importance of recording outpatient clinical outcomes through the cashing up process to support accurate RTT reporting.
Another source would be inconsistent validation across specialties. In many cases, the more scrutinised the service is in terms of performance, the more intense the validation. Some services would be more up to date than others. There are cases where DQ issues only exist in specific areas because of the services and the digital pathway (method of referral received). Upon reflection, I understand that recorded data does not entirely represent operational activity accurately. There are many things to consider, such as completeness, timeliness, and data accuracy.


References (if applicable):

NHS England (2025) Recording and reporting referral to treatment (RTT) waiting times for consultant-led elective care. Version 5.0. London: NHS England.
https://www.england.nhs.uk/wp-content/uploads/sites/2/2025/02/Recording-and-reporting-RTT-waiting-times-guidance-v5.0-Feb25.pdf

---

### Section2

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Identify two variables in your work that you suspect correlate. How would understanding this correlation, and any potential underlying causation, change any business decisions?

#### Responses

1. The two variables would be outpatient capacity and the number of non-admitted patients on our booking waiting list. For services that have significantly long waiters, normally, you would expect these to have less capacity. Outpatient Capacity can differ between first and follow-up appointments. The services would then compare slot utilisation against their waiting lists per specialty. However, correlation does not necessarily mean causation, as there are factors to consider. Things to consider in terms of outpatient capacity would be staff shortages, session cancellations, waiting list initiatives (additional capacity), specialist clinics, and patient availability. For specialties struggling with demand, additional capacity will need to be considered to optimise operational flow.

---

### Section3

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Think of a recent presentation or report in your organisation. What visualisation types were used? Were they effective? What would you change?

#### Responses

1. We are on a Tier 1 performance review, and a presentation on our Elective and Diagnostics performance was part of a performance pack. The performance pack included Line charts, SPC charts, bar graphs specifically for Long Waiters, 1st appointments, and performance against trajectories. I think this was very effective in displaying and highlighting the issues the organisation faces in some of these areas, as well as specifying our recovery plan. I would add some further RAG ratings to highlight improvements, complement the trends, and potentially do a deep dive into the specialties that need focus, to make clear where recovery needs to start. I would add some KPI cards with clear measures for ease of understanding.

---

## Week 5 Reflections

### Section1

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Identify a project in your organisation where multiple roles, such as project managers, analysts, developers and business stakeholders, needed to collaborate. Using the interest/influence matrix from this notebook, map these roles and stakeholders, and explain how better collaboration between them could have improved the project's outcome.

#### Responses

1. A more recent project has been our Preoperative Assessment pathway and Dashboard. Using the matrix above, I would identify the POA service coordinators and preop nurses as high interest and high influence. This is because a majority of the engagement will come from these members of staff. The information analyst, developers, and the admin staff will have high interest but low decision-making, as we are providing the services, bringing everything together whilst maintaining constant communication. The senior operational management have high interest but low day to day interest, as they are not consistently working with the data and mainly focus on the aggregated outputs. There are stakeholders with limited involvement, but who are still necessary, such as the waiting list team, so I would consider this low influence, low interest. Upon reflection, a clear outline and KPI definitions would have supported the reporting requirements and the necessary DQ issues. The data needed to be clean, with the admin staff resolving the DQ issues for effective monitoring, as well as regular feedback.

---

### Section2a

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Define, in your own words, the difference between a data model and a measurement. Using this notebook's regression model as an example, explain how you would apply these concepts in your workplace to understand the profitability of a product, service or project.

#### Responses

1. A measurement is a measure or value, and a data model brings together different variables to understand trends and predict specific outcomes. This is highly dependent on the configuration of the model and which model is used. I would apply these concepts to our current Theatre productivity. I would consider theatre utilisation, maximising procedures, average procedure length, and average cases per list as my measurements. 

Based on that, I would use a regression model so we could assess whether higher theatre utilisation is associated with lower cost per procedure. Variables I would consider in this regression model would include specialty, subspecialty, and case mix. 

With all of this in mind, I would use this model to identify financial opportunities and utilisation opportunities to achieve maximum potential.

---

### Section2b

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Would stakeholders in your role care more about a clustering model's accuracy or the interpretability of the segments it produces? Why? How does this affect your choice of model?

#### Responses

1. Stakeholders in the NHS would care more about the interpretability of the model than the accuracy, however, accuracy is still important. For example, in RTT, whilst accuracy is very important, stakeholders could identify clusters of patients that need operational input, even if accuracy is not at its peak. Whereas you could have a model that is more accurate, but the clusters do not amount to anything that useful unless interpreted. This could potentially identify patients that require immediate booking in order to improve a specialty's position and waiting times, specifically to target intervention. Therefore, I would choose a clustering model such as K-means where the output groups can be interpreted and translated to stakeholders easily. “K-means is widely used because of its simplicity and efficiency in grouping observations based on similar characteristics 
(Choudhari and Satav, 2026, p. 1)”.

References (if applicable):
Choudhari, P.M. and Satav, K.S. (2026) ‘To study customer analytics using K-means clustering for business growth at Sarth Solar’, International Scientific Journal of Engineering & Management, 5(4), pp. 1–4.

---

### Section3

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. A statistically significant result doesn't always mean a practically important one. Describe a scenario where the result is statistically significant but the effect size is too small to matter for business, and one where non-significance might still warrant action.

#### Responses

1. For example, our outpatient RTT waiting list for our ENT ( Ear, Nose and Throat) service is around 7000 patients. There were recommendations in place to implement changes in ourbooking pathways to improve waiting times, from an average of 40 weeks to 39 weeks. Although this may be a majority of our long waiters, the time and effort that went into adjusting the booking pathway had little to no improvement, especially given the scale of the waiting list, however, this does not move our ENT long waiter position or improve our 52 week waiters. For example, if it had a p value of 0.01, improvement is beneficial for the remaining ENT patients and may not justify the resource allocation; therefore, the benefit is limited. Another non-significance scenario could be an increase in access team validation, which could impact the long waiters and improve overall position. This will still require investigation but may bear fruit as validation is done, clock stops or potential pathways may be identified and closed.

---

## Week 6 Reflections

### Section2

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Where would a tool like `anonympy` sit in your organisation's data pipeline? Which roles would typically configure, run or review it, and why? (MLO1)

2. In this notebook before choosing an anonymisation technique, we classified the columns as numeric, categorical or datetime, similar to the data type classification you carried out in Week 2. Is this classification step ever safe to skip, or does it always need to happen first? Justify your view with reference to anonymisation, validation, or another data management action. (MLO2)

#### Responses

1. Anonympy can be incorporated into our fabric processes and data pipeline to anonymise and pseudonymise patient-level data from our PAS system, Lorenzo. This could be the initial security of our dataset before making it available to the organisation in line with our Information Governance policies. 
RTT contains patient-level data, including patient name, date of birth, postcode, and NHS numbers. We could use anonympy to prepare data for analysis and Power BI development, as well as reporting. This would need to be configured by our data warehouse team, as they have all the correct permissions to implement this and aided by the BI team, whilst me as an Information Manager, can review the data and sign off for organisational use. 


2. I believe this classification step first, identifying the relevant datatype is critical to any development, as the data type may affect its use in future development. In our dataset we have NHS numbers which is a 10 digit numeric field, but can also be used as an identifier. Identifying NHS numbers ensures we provide a consistent method for safeguarding this information. Another example would be the amendment of the clock start date. This change knowingly has an effect on the waiting times. If these are not clearly defined at the outset, this could affect the accuracy and reliability of our reporting. These columns' classification is pre defined via technical specifications provided by NHS England. In a developer’s start to a project, this is always important first. It is still the role of the developer to validate this information prior to the use of any anonymisation technique.

---

### Section3

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Coordinate rounding is a deterministic technique; perturbation adds random noise. If you needed to run a further spatial analysis on the resulting data afterwards, which technique would preserve more analytical value, and what would you lose either way?

#### Responses

1. Coordinate rounding would generate more value in analysis, as this would be more accurate because of the generalisation. Whereas perturbation adds changes to the coordinates. This would directly affect spatial analysis on the results.  I believe both methods have positives and negatives, as rounding method could group patients in our NHS datasets, but make it difficult to differentiate between them. Perturbation adds displacement; running the cell multiple times will produce a different perturbed location after each run. This could eventually give less accurate results once we explore a deep-dive analysis. I think that the method selected depends entirely based on the expected outcome, or what you are trying to achieve, of this analysis.

---

## Week 7 Reflections

### Section_1

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. We removed sunshine duration from Model 1 to create simpler Model 2 with only a tiny performance loss. In your workplace, when would you prioritise model simplicity over maximum accuracy? What stakeholder factors influence this decision?

2. The test-train split confirmed our model generalises well, with only a small performance drop. Describe a workplace scenario where a model might perform well on historical data but fail on future data. What changed?

#### Responses

1. I would prioritise a simple model over a maximum accuracy model. This is because the NHS as a whole is a fast-paced, highly pressurised environment with business decisions made daily around operational performance & capacity. For example, forecasting our performance for RTT, we need to factor in a number of items, such as referrals, demand, additions and removals, specialties, and also capacity. This is because of ease of explanation to the senior management team. Modelling and forecasting is critical to any organisation's contractual planning. A model with the purpose of maximum accuracy could prove difficult to replicate and amend when adjusting for future scenarios, and to explain to my stakeholders. Simplifying a model should be considered, if acceptable and accuracy is not significantly reduced, as reflected in modifications in models 1 & 2. Accuracy is also very important when modelling, as this could affect strategic decisions.

2. I would use the RTT forecasting as a prime example. We may be able to work out a model to identify and predict the future waiting list based on historical data. Operational circumstances may change. For example, I have two services where the two operating surgeons were both away due to unforeseen circumstances, and there was not enough time to provide adequate cover. Whilst this was going on, the organisation was hit with industrial action – strike plans which affected operations due to many staff not attending their shifts. Although a potential model tested well, this would fail due to unforeseen circumstances, and any rerun of a model would need to potentially factor this in for future predictions. Whilst improving capacity, we would still generate a backlog for the specialties in question.

---

### Section_2

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Exponential smoothing requires no external predictors; it learns from historical patterns alone. When would this be advantageous over the regression approach from Section 1, which needed external predictor data? Give an example from your sector.

2. Imagine your volunteer forecast is 30% too low (100 predicted, 130 show up) versus 30% too high (100 predicted, 70 show up). Which error is more costly in your charity context? Does this asymmetry affect how you would set forecast thresholds or build operational buffers?

#### Responses

1. Exponential smoothing is beneficial when it is difficult to retrieve the external predictors. Regression requires these variables, whereas exponential smoothing can learn from the historical data period alone.  Within the NHS, we are required to submit our forecast planning for the next financial year. Our waiting list data could use an exponential smoothing based on historical trends and seasonality. This would produce a quick forecast, however, the waiting list elective activity is affected by NHS strikes by clinical staff. This can be unpredictable at times, potentially straining resources, adding to the backlog, and worsening waiting times. In that case, a regression model would take into consideration variables such as job planning, capacity, staff availability, and more. If wider variables are available, a regression model could be the more appropriate choice if accuracy shows improvement.

2. In this scenario, I believe that underestimating has a further negative impact. If 100 are predicted and 130 show up, there is a strong chance that there would not be enough resources, equipment, or maybe not enough for task allocation. It would also make planned inductions, training, and supervision much more difficult for the charity. However, if we had 100 predicted and 70 show, it would mean less volunteers and more organisational resources available. This could affect forecasted planned activities and tasks. I would build an operational buffer around my forecast to ensure enough resources are available but not too much, as this would make things cost effective, especially for a charity. “Leading organisations widely acknowledge that forecasting is at the heart of the performance management process” (KPMG International, 2007, p. 2).

References (if applicable):
GOV.UK (n.d.) Data Protection.  Available at: https://www.gov.uk/data-protection (Accessed: 19 November 2026).   

KPMG International (2007) Forecasting with confidence: Insights from leading finance functions. Available at: https://assets.kpmg.com/content/dam/kpmg/pdf/2016/07/forecasting-with-confidence.pdf (Accessed: 22 November 2026).
