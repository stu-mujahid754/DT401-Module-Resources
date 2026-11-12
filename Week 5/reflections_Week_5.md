# Week 5 Reflections

## Section1

- **MLO1:** *Explain the roles and functions of technology solutions within an organisation*
- **MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Identify a project in your organisation where multiple roles, such as project managers, analysts, developers and business stakeholders, needed to collaborate. Using the interest/influence matrix from this notebook, map these roles and stakeholders, and explain how better collaboration between them could have improved the project's outcome.

### Responses

1. A more recent project has been our Preoperative Assessment pathway and Dashboard. Using the matrix above, I would identify the POA service coordinators and preop nurses as high interest and high influence. This is because a majority of the engagement will come from these members of staff. The information analyst, developers, and the admin staff will have high interest but low decision-making, as we are providing the services, bringing everything together whilst maintaining constant communication. The senior operational management have high interest but low day to day interest, as they are not consistently working with the data and mainly focus on the aggregated outputs. There are stakeholders with limited involvement, but who are still necessary, such as the waiting list team, so I would consider this low influence, low interest. Upon reflection, a clear outline and KPI definitions would have supported the reporting requirements and the necessary DQ issues. The data needed to be clean, with the admin staff resolving the DQ issues for effective monitoring, as well as regular feedback.

---

## Section2a

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Define, in your own words, the difference between a data model and a measurement. Using this notebook's regression model as an example, explain how you would apply these concepts in your workplace to understand the profitability of a product, service or project.

### Responses

1. A measurement is a measure or value, and a data model brings together different variables to understand trends and predict specific outcomes. This is highly dependent on the configuration of the model and which model is used. I would apply these concepts to our current Theatre productivity. I would consider theatre utilisation, maximising procedures, average procedure length, and average cases per list as my measurements. 

Based on that, I would use a regression model so we could assess whether higher theatre utilisation is associated with lower cost per procedure. Variables I would consider in this regression model would include specialty, subspecialty, and case mix. 

With all of this in mind, I would use this model to identify financial opportunities and utilisation opportunities to achieve maximum potential.

---

## Section2b

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Would stakeholders in your role care more about a clustering model's accuracy or the interpretability of the segments it produces? Why? How does this affect your choice of model?

### Responses

1. Stakeholders in the NHS would care more about the interpretability of the model than the accuracy, however, accuracy is still important. For example, in RTT, whilst accuracy is very important, stakeholders could identify clusters of patients that need operational input, even if accuracy is not at its peak. Whereas you could have a model that is more accurate, but the clusters do not amount to anything that useful unless interpreted. This could potentially identify patients that require immediate booking in order to improve a specialty's position and waiting times, specifically to target intervention. Therefore, I would choose a clustering model such as K-means where the output groups can be interpreted and translated to stakeholders easily. “K-means is widely used because of its simplicity and efficiency in grouping observations based on similar characteristics 
(Choudhari and Satav, 2026, p. 1)”.

References (if applicable):
Choudhari, P.M. and Satav, K.S. (2026) ‘To study customer analytics using K-means clustering for business growth at Sarth Solar’, International Scientific Journal of Engineering & Management, 5(4), pp. 1–4.

---

## Section3

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. A statistically significant result doesn't always mean a practically important one. Describe a scenario where the result is statistically significant but the effect size is too small to matter for business, and one where non-significance might still warrant action.

### Responses

1. For example, our outpatient RTT waiting list for our ENT ( Ear, Nose and Throat) service is around 7000 patients. There were recommendations in place to implement changes in ourbooking pathways to improve waiting times, from an average of 40 weeks to 39 weeks. Although this may be a majority of our long waiters, the time and effort that went into adjusting the booking pathway had little to no improvement, especially given the scale of the waiting list, however, this does not move our ENT long waiter position or improve our 52 week waiters. For example, if it had a p value of 0.01, improvement is beneficial for the remaining ENT patients and may not justify the resource allocation; therefore, the benefit is limited. Another non-significance scenario could be an increase in access team validation, which could impact the long waiters and improve overall position. This will still require investigation but may bear fruit as validation is done, clock stops or potential pathways may be identified and closed.
