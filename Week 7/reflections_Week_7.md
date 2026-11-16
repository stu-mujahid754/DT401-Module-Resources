# Week 7 Reflections

## Section_1

**MLO3:** *Select and apply appropriate data-gathering methods for a given data analysis scenario*

1. We removed sunshine duration from Model 1 to create simpler Model 2 with only a tiny performance loss. In your workplace, when would you prioritise model simplicity over maximum accuracy? What stakeholder factors influence this decision?

2. The test-train split confirmed our model generalises well, with only a small performance drop. Describe a workplace scenario where a model might perform well on historical data but fail on future data. What changed?

### Responses

1. I would prioritise a simple model over a maximum accuracy model. This is because the NHS as a whole is a fast-paced, highly pressurised environment with business decisions made daily around operational performance & capacity. For example, forecasting our performance for RTT, we need to factor in a number of items, such as referrals, demand, additions and removals, specialties, and also capacity. This is because of ease of explanation to the senior management team. Modelling and forecasting is critical to any organisation's contractual planning. A model with the purpose of maximum accuracy could prove difficult to replicate and amend when adjusting for future scenarios, and to explain to my stakeholders. Simplifying a model should be considered, if acceptable and accuracy is not significantly reduced, as reflected in modifications in models 1 & 2. Accuracy is also very important when modelling, as this could affect strategic decisions.

2. I would use the RTT forecasting as a prime example. We may be able to work out a model to identify and predict the future waiting list based on historical data. Operational circumstances may change. For example, I have two services where the two operating surgeons were both away due to unforeseen circumstances, and there was not enough time to provide adequate cover. Whilst this was going on, the organisation was hit with industrial action – strike plans which affected operations due to many staff not attending their shifts. Although a potential model tested well, this would fail due to unforeseen circumstances, and any rerun of a model would need to potentially factor this in for future predictions. Whilst improving capacity, we would still generate a backlog for the specialties in question.
