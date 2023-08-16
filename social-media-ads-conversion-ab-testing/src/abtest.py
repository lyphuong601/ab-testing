import pandas as pd
from statsmodels.stats import power as pwr
from statsmodels.stats.proportion import proportion_confint, proportions_ztest, proportion_effectsize
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu


def ztest(sucess, obs, test_side="smaller", alpha=0.05):
    test_stat, p_value = proportions_ztest(
        count=sucess, nobs=obs, alternative=test_side)

    print("H0: CTR for control > treatment")
    print("H1: CTR for control < treatment.\n")
    print(f"Z test statistic is {test_stat:.3f}")
    print(f"p-value for Z test is {p_value:.3f}\n")

    if p_value < alpha:
        print(f"p-value = {p_value:.3f} < {alpha}")
        print("We can reject null hypothesis. CTR in treatment group is larger")
    else:
        print(f"p-value = {p_value:.3f} >= {alpha}")
        print("We can't reject null hypothesis. CTR in control group is larger.")


def conf_int(sucess, obs, alpha=0.05):
    (lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(
        count=sucess, nobs=obs, alpha=alpha)
    print(f'ci 95% for control group: [{lower_con:.6f}, {upper_con:.6f}]')
    print(
        f'ci 95% for treatment group: [{lower_treat:.6f}, {upper_treat:.6f}]')


def hypothesis_test(df_A: pd.DataFrame, df_B: pd.DataFrame, col_name: str) -> None:
    test_stat_A, pvalue_A = shapiro(df_A[col_name])
    print(
        f'Control group: Shapiro Test Stat = {test_stat_A:.4f}, p-value = {pvalue_A:.4f}')

    test_stat_B, pvalue_B = shapiro(df_B[col_name])
    print(
        f'Treatment group: Shapiro Test Stat = {test_stat_B:.4f}, p-value = {pvalue_B:.4f}')

    test_stat_var, pvalue_var = levene(df_A[col_name], df_B[col_name])
    print(
        f'Levene Test Stat = {test_stat_var:.4f}, p-value = {pvalue_var:.4f}')

    print("H0: CTR for control = treatment")
    print("H1: CTR for control != treatment.\n")

    if pvalue_A < 0.05 and pvalue_B < 0.05:
        test_stat, pvalue = mannwhitneyu(df_A[col_name], df_B[col_name])
        print(
            f'Mannwhitneye Test Stat = {test_stat:.4f}, p-value = {pvalue:.4f}')
        print(
            f'H0 hypothesis {"NOT REJECTED" if pvalue > 0.05 else "REJECTED"}')
    else:
        test_stat, pvalue = ttest_ind(df_A[col_name], df_B[col_name], equal_var=(
            True if pvalue_var > 0.05 else False))
        print(f'Ttest Test Stat = {test_stat:.4f}, p-value = {pvalue:.4f}')
        print(
            f'H0 hypothesis {"NOT REJECTED" if pvalue > 0.05 else "REJECTED"}')
