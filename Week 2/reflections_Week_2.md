# Week 2 Reflections

## Section_1

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. When might you store a price field as a text string instead of a decimal? Describe one specific problem that might arise, such as, in a calculation, a report, or a data import, and provide a brief example.

### Responses

1. In our data warehouse, we store financial data as well as patient data, and in some cases, this is stored financial information from our PLICs system and Income information for SLAM (Service Level Agreement Monitoring). If I were to extract this as a text field and tried to do calculations or mathematical formulas with this it would produce incorrect output or incorrect sums on a financial total, which is detrimental to understanding the organisation's financial position, both expenditure and income. Microsoft (n.d., SUM (Transact-SQL)) explains that the SQL SUM function can only be used with numeric data types.


References (if applicable):

Microsoft (n.d.) SUM (Transact-SQL) – SQL Server. https://learn.microsoft.com/en-us/sql/t-sql/functions/sum-transact-sql

---

## Section_2

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Using this week's distinction between mutable and immutable data, identify one situation in your role where data *should* be protected from change, where accidental modification would cause a problem. Then identify one where it *must* be changeable, where the data needs to be updated to reflect changes and the old value is no longer valid.Does your workplace's current handling of this distinction get the balance right? Justify your view.

### Responses

1. The DM01 diagnostic data is immutable, as it is published and widely used in the Department of Health insights, so we cannot make changes. I would identify our IP (Inpatient) Waiting list as mutable. Even though the script is maintained due to business needs. It requires daily updates from our data warehouse extract files to establish an updated worklist. This will update the necessary information for the operational teams, which includes waiting times, pathway updates, etc.
My organisation approaches this strategically by storing the snapshots and providing read-only access to staff. This business logic is also managed by in-house change control processes. There have been instances where the stored processes in our SQL Agent jobs have failed due to another process failing in the sequence. These processes have caused inaccuracy in our board reporting at times. This raised the necessary reconciliation tasks for the BI team to maintain integrity and accuracy. “Patient records, treatment histories, and diagnostic results must remain unchanged to ensure accuracy and trust. Immutable data ensures that once information is recorded, it cannot be tampered with, offering a reliable and auditable history.”
Tan, L. (2025) Immutable vs. mutable: The data debate that could define your success. Available at: https://estore.flexxon.com/blogs/immutable-storage/immutable-vs-mutable-the-data-debate-that-could-define-your-success

---

## Section_3

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Describe a situation in your workplace where data moves between formats. For example, from a database to a spreadsheet, or from an API to a report. Why are these conversions necessary? What challenges might arise during this conversion? Think about what information can be lost or changed when moving between, for example, a nested format (JSON) and a flat one (CSV).

### Responses

1. In my workplace, we use a system called NETCALL as one of our tools for waiting list validation. This will then send a text message on a weekly basis asking patients whether they would like to stay on the relevant waiting list. Once this process is complete, we get the responses via an API call, which we retrieve the responses in a JSON file, which we then convert to a CSV and upload to our data warehouse via an SSIS package. This transformation is necessary to obtain the relevant format to be used and combined with our other datasets. Whilst on this project, numerous issues prolonged completion of the reporting phase. This was due to issues with the special characters in text fields & numerous date formats.

---

## Section_4

**MLO2:** *Critically reflect upon data management systems and their role in digital and technology solutions*

1. Using this week's normalisation principles, would you defend storing in a medical clinic's appointment datablase the doctor's name in every appointment row, the unnormalised approach? Should it be normalised? Justify your position in terms of what could go wrong, rather than just naming the normal form.

### Responses

1. I would normalise the appointment database and store the clinicians in a fact table that we could join to. In our Lorenzo system, we had this problem where there were many clinicians' names attached to the same generic medical consultant number, which meant we had multiple names attached to one clinician. In our reporting, this flagged numerous data quality issues. This also affected our slot utilisation by clinician, as the numerator and denominator were affected by the split. By creating a fact table apply one table with a primary key that can join, we can apply the one-to-many join. I would also maintain the historical changes for audit purposes.
