# Week 1 Reflections

## Section1

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. How does the notebook format, combining written explanation with live code, compare to tools you currently use at work (e.g. Excel, Word, dashboards)? What are its advantages and limitations? (MLO1)
2. Identify a dataset you work with in your role. Is it closer to raw *data*, an organised *dataset*, or part of a *database*? What would need to change for it to move up a level? Justify your answer (MLO2)
3. Using the METEO dataset as an example, describe one step you could take to move from the DIKUW pyramid *Information* level (a statistic) to the *Knowledge* level (a meaningful insight). What additional context or comparison would you need? (MLO1)

### Responses

1. In the NHS, specifically in my role, I use Excel, Power BI, SQL, and Python as the basis of my analysis work to present my data. The notebook format is very useful because I can document my code and explain what it does in a structured way, giving full visibility into both the coding, the explanation, and the outputs all in one place. I believe this will help stakeholders understand my process and findings.
I can document the steps I have taken to cleanse data, such as the RTT waiting list data. In comparison with a dashboard where the cleansing could happen in Power Query within the dashboard. 
In order to achieve the same results, I would need one source of the truth (consistent data source). I would use Jupyter Notebook to document and track methods of approach whilst continuing to use Power BI service and dashboards for performance monitoring.


2. The RTT waiting list dataset consists numerous fields that are used to aid, assist and track treatment waiting times. This specific dataset is closer to database. In order produce this report as efficiently as possible, it requires numerous derived columns, and connections via a range of identifiers such as primary and foreign keys in our data warehouse. The next stage would categorically be improvement in the data warehouse.
In terms of the three above, this data cannot move further; it can be improved over time to support the reporting function and the needs of the organisation such as new fields, columns, etc and better integration with the appointments table, e.g., (Date of First Future Appointment, Date of First Investigations), and the use of AI to automate manual validation. However, these improvements would need to be carefully implemented,along with NHS England ethhics and guidlines and validation will still require operational oversight.

3. The one step I would take is to conduct some trend analysis and compare month on month, year on year, location, seasonality, and some data quality metrics based on the average sunshine duration against different locations available, to ensure the data is reliable in its entirety. This would then help me identify any data quality issues within the meteo dataset. With these changes and improvements this will allow my data set to evolve from Information to a meaningful insight."Accumulated data lacks the uniformity and homogeneity often implied in pyramid models, misrepresenting the role of evidence and argument in the construction of knowledge and wisdom". (Peters, Michael A,2024,p.7-17)

References (if applicable):
By:Peters, Michael A.In:Psychosociological Issues in Human Resource Management, 2024, volume 12, issue 2, pages 7-17 (11p)Business Source Elite
