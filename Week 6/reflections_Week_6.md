# Week 6 Reflections

## Section2

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Where would a tool like `anonympy` sit in your organisation's data pipeline? Which roles would typically configure, run or review it, and why? (MLO1)

2. In this notebook before choosing an anonymisation technique, we classified the columns as numeric, categorical or datetime, similar to the data type classification you carried out in Week 2. Is this classification step ever safe to skip, or does it always need to happen first? Justify your view with reference to anonymisation, validation, or another data management action. (MLO2)

### Responses

1. Anonympy can be incorporated into our fabric processes and data pipeline to anonymise and pseudonymise patient-level data from our PAS system, Lorenzo. This could be the initial security of our dataset before making it available to the organisation in line with our Information Governance policies. 
RTT contains patient-level data, including patient name, date of birth, postcode, and NHS numbers. We could use anonympy to prepare data for analysis and Power BI development, as well as reporting. This would need to be configured by our data warehouse team, as they have all the correct permissions to implement this and aided by the BI team, whilst me as an Information Manager, can review the data and sign off for organisational use. 


2. I believe this classification step first, identifying the relevant datatype is critical to any development, as the data type may affect its use in future development. In our dataset we have NHS numbers which is a 10 digit numeric field, but can also be used as an identifier. Identifying NHS numbers ensures we provide a consistent method for safeguarding this information. Another example would be the amendment of the clock start date. This change knowingly has an effect on the waiting times. If these are not clearly defined at the outset, this could affect the accuracy and reliability of our reporting. These columns' classification is pre defined via technical specifications provided by NHS England. In a developer’s start to a project, this is always important first. It is still the role of the developer to validate this information prior to the use of any anonymisation technique.

---

## Section3

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Coordinate rounding is a deterministic technique; perturbation adds random noise. If you needed to run a further spatial analysis on the resulting data afterwards, which technique would preserve more analytical value, and what would you lose either way?

### Responses

1. Coordinate rounding would generate more value in analysis, as this would be more accurate because of the generalisation. Whereas perturbation adds changes to the coordinates. This would directly affect spatial analysis on the results.  I believe both methods have positives and negatives, as rounding method could group patients in our NHS datasets, but make it difficult to differentiate between them. Perturbation adds displacement; running the cell multiple times will produce a different perturbed location after each run. This could eventually give less accurate results once we explore a deep-dive analysis. I think that the method selected depends entirely based on the expected outcome, or what you are trying to achieve, of this analysis.
