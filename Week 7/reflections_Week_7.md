# Week 7 Reflections

## Section_1

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. We removed sunshine duration from Model 1 to create simpler Model 2 with only a tiny performance loss. In your workplace, when would you prioritise model simplicity over maximum accuracy? What stakeholder factors influence this decision?

2. The test-train split confirmed our model generalises well, with only a small performance drop. Describe a workplace scenario where a model might perform well on historical data but fail on future data. What changed?

### Responses

1. I would prioritise a simple model over a maximum accuracy model. This is because the NHS as a whole is a fast-paced, highly pressurised environment with business decisions made daily around operational performance & capacity. For example, forecasting our performance for RTT, we need to factor in a number of items, such as referrals, demand, additions and removals, specialties, and also capacity. This is because of ease of explanation to the senior management team. Modelling and forecasting is critical to any organisation's contractual planning. A model with the purpose of maximum accuracy could prove difficult to replicate and amend when adjusting for future scenarios, and to explain to my stakeholders. Simplifying a model should be considered, if acceptable and accuracy is not significantly reduced, as reflected in modifications in models 1 & 2. Accuracy is also very important when modelling, as this could affect strategic decisions.

2. I would use the RTT forecasting as a prime example. We may be able to work out a model to identify and predict the future waiting list based on historical data. Operational circumstances may change. For example, I have two services where the two operating surgeons were both away due to unforeseen circumstances, and there was not enough time to provide adequate cover. Whilst this was going on, the organisation was hit with industrial action – strike plans which affected operations due to many staff not attending their shifts. Although a potential model tested well, this would fail due to unforeseen circumstances, and any rerun of a model would need to potentially factor this in for future predictions. Whilst improving capacity, we would still generate a backlog for the specialties in question.

---

## Section_2

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. Exponential smoothing requires no external predictors; it learns from historical patterns alone. When would this be advantageous over the regression approach from Section 1, which needed external predictor data? Give an example from your sector.

2. Imagine your volunteer forecast is 30% too low (100 predicted, 130 show up) versus 30% too high (100 predicted, 70 show up). Which error is more costly in your charity context? Does this asymmetry affect how you would set forecast thresholds or build operational buffers?

### Responses

1. Exponential smoothing is beneficial when it is difficult to retrieve the external predictors. Regression requires these variables, whereas exponential smoothing can learn from the historical data period alone.  Within the NHS, we are required to submit our forecast planning for the next financial year. Our waiting list data could use an exponential smoothing based on historical trends and seasonality. This would produce a quick forecast, however, the waiting list elective activity is affected by NHS strikes by clinical staff. This can be unpredictable at times, potentially straining resources, adding to the backlog, and worsening waiting times. In that case, a regression model would take into consideration variables such as job planning, capacity, staff availability, and more. If wider variables are available, a regression model could be the more appropriate choice if accuracy shows improvement.

2. In this scenario, I believe that underestimating has a further negative impact. If 100 are predicted and 130 show up, there is a strong chance that there would not be enough resources, equipment, or maybe not enough for task allocation. It would also make planned inductions, training, and supervision much more difficult for the charity. However, if we had 100 predicted and 70 show, it would mean less volunteers and more organisational resources available. This could affect forecasted planned activities and tasks. I would build an operational buffer around my forecast to ensure enough resources are available but not too much, as this would make things cost effective, especially for a charity. “Leading organisations widely acknowledge that forecasting is at the heart of the performance management process” (KPMG International, 2007, p. 2).

References (if applicable):
GOV.UK (n.d.) Data Protection.  Available at: https://www.gov.uk/data-protection (Accessed: 19 November 2026).   

KPMG International (2007) Forecasting with confidence: Insights from leading finance functions. Available at: https://assets.kpmg.com/content/dam/kpmg/pdf/2016/07/forecasting-with-confidence.pdf (Accessed: 22 November 2026).
