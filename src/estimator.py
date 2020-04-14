def estimator(data):
    period_type = data['periodType']
    time_to_elapse = data['timeToElapse']
    reported_cases = data['reportedCases']
    hospital_beds = data['totalHospitalBeds']
    income = data['region']['avgDailyIncomeInUSD']
    income_population = data['region']['avgDailyIncomePopulation']

    impact_cases = reported_cases * 10
    severe_cases = reported_cases * 50
    available_beds = 0.35 * hospital_beds

    # calculate the number of days
    def normalize_days(periodtype, time_to_elapse):
        if periodtype == 'days':
            days = time_to_elapse
        elif periodtype == 'weeks':
            days = time_to_elapse * 7
        elif periodtype == 'months':
            days = time_to_elapse * 30
        return days

    def infected_to_date(case):
        days = normalize_days(period_type, time_to_elapse) // 3
        return case * (2 ** days)

    def severe_infections_by_requested_time(case):
        return 0.15 * infected_to_date(case)

