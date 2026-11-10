# Week 3 Reflections

## Section1

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Sometimes 100% completeness or accuracy isn't achievable or cost-effective. What completeness or accuracy threshold would you accept for different business scenarios you encounter in your workplace (e.g., operational reporting vs. strategic planning)?

### Responses

1. In terms of reporting, we aim for a 99% accuracy threshold, especially when it comes to reporting our waiting list, to provide as much information as possible. There are many critical fields required to produce the RTT Waiting List, such as clock start date, RTT treatment status, referral type, clinical priority code, and RTT week number for tracking. Any inaccuracy in any field could affect clinical and operational decision making. In terms of strategic planning, such as forecasting demand and assembling our trajectories. We allow a tolerance of 95% completeness, as this does not necessarily affect the model in terms of forecasting. In terms of our mandatory submissions, there are cases where we are expected to populate 100% of the fields to comply with the NHS contractual obligations. Completness thresholds should be a case by case scenario among the dataset size, as the percentage matters for the dataset. The accurate recording and reporting of referral to treatment (RTT) waiting times information is extremely important. Patients can and do use this information to inform their choice of where to be referred and also to understand how long they might expect to wait before starting their treatment."The accurate recording and reporting of referral to treatment (RTT) waiting times 
information is extremely important."(NHS England, 2022, p. 4).

References (if applicable):
NHS ENGLAND, 2021. Recording and reporting referral to treatment (RTT) waiting times for consultant-led elective care. London: NHS England. Available from: https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2021/05/Recording-and-Reporting-guidance-April_2021.pdf

---

## Section2

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Which FAIR principle would most improve data sharing in your workplace? What barriers prevent implementing this principle? (MLO2)

2. What role do data management systems play in your workplace's digital and technology solutions? Using an example from your workplace, what are the strenths and challenges you find with the system? Justify your view with reference to one challenge you have encountered implementing, managing, or using it. (MLO1, MLO2)

### Responses

1. Data sharing in the NHS would improve ease of access (accessibility). Our operational and clinical colleagues require access to data in a timely manage to aid in the assistance of running the services efficiently and effectively. Ensuring everyone has access to the relevant reports would reduce the burden of ad hoc requests that we, the Information/BI Team receive.
This would need to be balance alongside row level security ensuring staff only have access to the necessary information related to their job role and senior approval is granted based on job description. The barriers preventing this implementation would be an additional process, inconsistences around job roles, delayed access and potentially an increase of burden of the Information/BI Team. I’d recommend a Lakehouse of all potential patient identifiable data with an automated access approval flow to ensure less reliance on my team and full accountability & governance of the operational teams.


2. Our systems support our operational reporting through our data warehouse. This supports our Power BI reports which support a range of reports for every aspect of the Trust. One of the strengths is that we have our data centralised so querying makes things so easy over a range of systems. This provides consistent reporting and  a single source of the truth. A challenge that I have faced SQL agent jobs failing because of an earlier process that has failed. This has affected our integrated performance reporting which is used to steer direction over operation decisions. This issue was identified, investigated, and resolved. However, regardless of automation, data warehouse monitoring is just as important. The data warehouse is dependent on numerous daily checks, and SQL alerts. The data warehouse is the centre of our data repository, but its reliability depends on our daily runs being successful. “No matter how well you tune your data warehouse, reliability of data is tantamount to any successful project. And even simple discrepancies can cause serious repercussions when attempting to make well-founded business decisions based on the warehouse data. Krill, P. (1998)”

References (if applicable):

Krill, P. (1998) ‘Data warehouses have need for clean data’, InfoWorld, 16 March. Available at: https://research.ebsco.com/c/m7mrx2/search/details/4mjzqctlkb

---

## Section3

- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*
- **MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Identify a business question in your workplace that requires joining data. Using the join types we have seen in Part 2, which is appropriate, and why would the wrong choice produce a misleading answer?

### Responses

1. One question that is frequently asked on the RTT waiting list, is how many patients on the PTL have multiple DNA’s (Did Not Attend) and consecutive DNA’s. This is because there is NHS guidance ruling that a patient awaiting their first appointment that has DNA’d consecutively is allowed to be discharged back to the GP. This is a measure in place to aid waiting list reduction.  I would join a temp table of the outpatient appointments by DNA and aggregate a count based on the patientpathwayid and LEFT JOIN on to the RTT PTL. This would give me the full PTL and the aggregate DNA count in one single line. However, if I was to use for an INNER JOIN, this would give me only those records that have DNA’s linked by patientpathwayid and exclude everything else. This would be a misrepresentation of the waiting list size and reduce the accuracy of the PTL. According to NHS England (2022, p. 6), a patient who does not attend their first appointment on an RTT pathway may have their RTT clock nullified and be returned to primary care, provided the relevant clinical and communication requirements are met.



References (if applicable):NHS England (2022) Re-stating RTT Rules: Referral to Treatment Rules Guidance v1.3.
