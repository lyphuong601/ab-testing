import pandas as pd
from statsmodels.stats.proportion import proportion_confint, proportions_ztest


def ztest(success, trial, alpha=0.05):
    z_score, p_value = proportions_ztest(
        success, nobs=trial, alternative='larger', prop_var=0.5)

    print("H0: Retention rate for Gate30 < Gate40.")
    print("H1: Retention rate for Gate30 > Gate40.\n")
    print(f"Z test statistic is {z_score.round(5)}")
    print(f"p-value for Z test is {p_value:.3f}\n")

    if p_value < alpha:
        print(f"p-value = {p_value:.3f} < {alpha}")
        print("We can reject null hypothesis. Users in Gate30 have higher 1 day retention than Gate40")
    else:
        print(f"p-value = {p_value:.3f} >= {alpha}")
        print("We can't reject null hypothesis. Users in Gate40 have higher retention.")


def conf_int(sucess, obs, alpha=0.05):
    (lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(
        count=sucess, nobs=obs, alpha=alpha)
    print(f'ci 95% for control group: [{lower_con:.6f}, {upper_con:.6f}]')
    print(
        f'ci 95% for treatment group: [{lower_treat:.6f}, {upper_treat:.6f}]')
