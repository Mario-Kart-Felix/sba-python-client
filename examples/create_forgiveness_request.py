from PPPForgivenessSDK.client import Client

# to run file 'create_forgiveness_request.py', make sure python path includes path to sba_ppp_forgiveness-sdk
# , use a valid toke and insure loan information matches a valid loan without a previous forgiveness request
client = Client(
    access_token='{{YOUR_TOKEN_HERE}}',
    vendor_key='{{YOUR_VENDOR_KEY}}',
    environment='sandbox'
)

forgiveness_api = client.forgiveness_requests

# create a new forgiveness request
# etran_loan must pass validation against SBA records based on amounts, full disbursement, ein match, sba number match and amount match
result = forgiveness_api.create(
                                bank_notional_amount='{{BANK_NOTIONAL_AMOUNT_HERE}}',
                                sba_number=int('{{SBA_NUMBER_HERE}}'),
                                loan_number=int('{{LOAN_NUMBER_HERE}}'),
                                entity_name='{{ENTITY_NAME_HERE}}',
                                ein='{{EIN/SSN_HERE}}',
                                funding_date=None,
                                forgive_eidl_amount=None,
                                forgive_eidl_application_number=None,
                                forgive_payroll=None,
                                forgive_rent=None,
                                forgive_utilities=None,
                                forgive_mortgage=None,
                                address1=None,
                                address2=None,
                                dba_name=None,
                                phone_number=None,
                                forgive_fte_at_loan_application=None,
                                demographics=[],
                                forgive_line_6_3508_or_line_5_3508ez=None,
                                forgive_modified_total=None,
                                forgive_payroll_cost_60_percent_requirement=None,
                                forgive_amount=None,
                                forgive_fte_at_forgiveness_application=None,
                                forgive_schedule_a_line_1=None,
                                forgive_schedule_a_line_2=None,
                                forgive_schedule_a_line_3_checkbox=False,
                                forgive_schedule_a_line_3=None,
                                forgive_schedule_a_line_4=None,
                                forgive_schedule_a_line_5=None,
                                forgive_schedule_a_line_6=None,
                                forgive_schedule_a_line_7=None,
                                forgive_schedule_a_line_8=None,
                                forgive_schedule_a_line_9=None,
                                forgive_schedule_a_line_10=None,
                                forgive_schedule_a_line_10_checkbox=False,
                                forgive_schedule_a_line_11=None,
                                forgive_schedule_a_line_12=None,
                                forgive_schedule_a_line_13=None,
                                forgive_covered_period_from=None,
                                forgive_covered_period_to=None,
                                forgive_alternate_covered_period_from=None,
                                forgive_alternate_covered_period_to=None,
                                forgive_2_million=False,
                                forgive_payroll_schedule=None,
                                primary_email=None,
                                primary_name=None,
                                ez_form=False,
                                no_reduction_in_employees=False,
                                no_reduction_in_employees_and_covid_impact=False,
                                forgive_lender_confirmation=False,
                                forgive_lender_decision=None,
                    )


if result['status'] == 201:
    print(result['data'])
else:
    print("An error occurred." + str(result['status']))
    print(result['data'])
