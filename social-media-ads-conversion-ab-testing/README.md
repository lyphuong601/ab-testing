# A/B Testing: Social Media Ads Conversion

<p align="center"><img src="img/FB-ads.png" height="200" width="300"></p>

## 📌 Introduction
- Motivation: Use data available, compare click through rate (CTR) and cost per click (CPC) for control and treatment group

## Data Overview:
- Dependent variable: clicks, impressiion, spent, ads campaign id
- Independent variables: control/ treatment indicator

## Technology Used

<ul>
  <li>A/B Testing</li>
  <li>Bootstraping</li>
</ul>

## Conclusion
- KAG Ads company $\bold{should}$ use the new ads version to increase the click through rate and cost per click.
- In this A/B testing experiement, the MDE is set at 1%. To detect a rise of at least 1% in click-through rate, 509 data points are required for each test and control groups. 
- Finally, we can figure out for how many days we need to run the test based on daily traffic. In this experiment I will use Extensive Collection Period (Over 10 days). 

  Assume our site has 100 visitors per day. We found out we need ~1000 users in both test and control to detect an improvement of at least 10%. So we would split the traffic 50/50 for test and control. Each day we would have 50 users in test and 50 in control. And we would run the test for 10 days, i.e. 10*100 = 1000

- Using hypothesis testing, we conclude that treatment group performs better in click through rate and cost per click metrics.

## Contents

<h3>1. Guardian Checks</h3>
- We find that the control mean does not lie within the 95% confidence interval, which means that we've failed our Guardrail Metric. The number of unique users is not equal for each group. 

<h3>3. Sample size, MDE and test duration</h3>
The initial step in crafting an A/B test involves determining its duration, which equates to the necessary number of users for the test. The test sample size is contingent upon three key factors:

+ Test Significance Level: This denotes the likelihood of mistakenly concluding that the new version is superior to the old version. A common value is 0.05.

+ Test Power: This refers to the probability of correctly identifying the new version as better when it genuinely is. Conversely, 1 minus power represents the chance of not implementing a change despite its merit (essentially being overly cautious). A typical value for power is 0.8.

+ Minimum Detectable Effect: This represents the minimum improvement worth detecting. When the test outcome surpasses this threshold, it warrants implementing the change. For instance, a marginal difference of 0.001% might not justify action due to factors such as engineering costs and time constraints.

The larger sample sizes, the lower significance levels, greater power, and smaller minimum detectable effects.

<h3>2. Proportion Z test</h3>
A two proportion Z-test is employed to examine any disparities between the proportions of two populations.

Two Proportion Z-Test Formula (right-tailed) hypothesis:
* $H_0: p_1 < p_2$
* $H_1: p_1 > p_2$

The test statistic z:
$z = \dfrac{p_1 - p_2}{\sqrt{p_{pool}(1-p_{pool})(\dfrac{1}{n_1} + \dfrac{1}{n_2})}}$
where $p_1$ and $p_2$ are the sample proportions, $n_1$ and $n_2$ are the sample sizes,
and where p is the total pooled proportion calculated as: $p_{pool} = \dfrac{(p_1 \cdot n_1 + p_2 \cdot n_2)}{(n_1+n_2)}$

When the p-value associated with the test statistic Z is less than the selected significance level of 0.05, we reject the null hypothesis.

## Projects Completed

1. <a href="https://github.com/lyphuong601/job-postings-data-cleaning">Job Posting Data Cleaning</a>
2. <a href="https://github.com/lyphuong601/data-science/tree/main/Telco-customer-churn">Customer Churn Prediction</a>
3. <a href="https://github.com/lyphuong601/rfm-customer-segmentation"> Customer Segmentation: a K-Means Approach</a>

More projects coming up soon. Do drop a ⭐ if you like it.