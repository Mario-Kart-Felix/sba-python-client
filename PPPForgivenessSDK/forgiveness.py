import json
from .base_api import BaseApi, UnknownException



class ForgivenessRequestApi(BaseApi):

    def delete(self, slug):
        """

        :param slug:
        :return:
        """

        http_method = "DELETE"
        endpoint = "ppp_loan_forgiveness_requests/{0}/".format(slug)

        uri = self.client.api_uri + endpoint

        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            try:
                return {'status': response.status_code, 'data': json.loads(response.text)}
            except:
                return {'status': response.status_code, 'data': response.text}
        except:
            raise UnknownException # TODO: what about 405?

    def list(self, page=1):
        """

        :param page:
        :return:
        """
        assert isinstance(page, int), "Page must be a valid integer"

        http_method = "GET"
        endpoint = "ppp_loan_forgiveness_requests/"

        uri = self.client.api_uri + endpoint

        params = {'page': page}
        try:
            response = self.execute(http_method=http_method,
                                    url=uri,
                                    query_params=params)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def get(self, slug, sbanumber=None):
        """

        :param slug:
        :return:
        """

        http_method = "GET"
        if sbanumber is None:
            endpoint = "ppp_loan_forgiveness_requests/{0}/".format(slug)
        else:
            endpoint = "ppp_loan_forgiveness_requests/?sba_number={0}".format(sbanumber)

        uri = self.client.api_uri + endpoint

        try:
            response = self.execute(http_method=http_method,
                                    url=uri)

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException

    def create(self, bank_notional_amount, sba_number, loan_number, entity_name, ein, funding_date=None, forgive_eidl_amount=None,
               forgive_eidl_application_number=None, forgive_payroll=None, forgive_rent=None, forgive_utilities=None,
               forgive_mortgage=None, address1=None, address2=None, dba_name=None, phone_number=None,
               forgive_fte_at_loan_application=None, demographics=[], forgive_line_6_3508_or_line_5_3508ez=None,
               forgive_modified_total=None, forgive_payroll_cost_60_percent_requirement=None, forgive_amount=None,
               forgive_fte_at_forgiveness_application=None, forgive_schedule_a_line_1=None, forgive_schedule_a_line_2=None,
               forgive_schedule_a_line_3_checkbox=None, forgive_schedule_a_line_3=None, forgive_schedule_a_line_4=None,
               forgive_schedule_a_line_5=None, forgive_schedule_a_line_6=None, forgive_schedule_a_line_7=None,
               forgive_schedule_a_line_8=None, forgive_schedule_a_line_9=None, forgive_schedule_a_line_10=None,
               forgive_schedule_a_line_10_checkbox=None, forgive_schedule_a_line_11=None, forgive_schedule_a_line_12=None,
               forgive_schedule_a_line_13=None, forgive_covered_period_from=None, forgive_covered_period_to=None,
               forgive_alternate_covered_period_from=None, forgive_alternate_covered_period_to=None, forgive_2_million=None,
               forgive_payroll_schedule=None, primary_email=None, primary_name=None, ez_form=None, no_employees=None,
               no_reduction_in_employees=None, no_reduction_in_employees_and_covid_impact=None, forgive_lender_confirmation=None,
               forgive_lender_decision=None):
        """

        :param bank_notional_amount:
        :param sba_number:
        :param loan_number:
        :param entity_name:
        :param ein:
        :param funding_date:
        :param forgive_eidl_amount:
        :param forgive_eidl_application_number:
        :param forgive_payroll:
        :param forgive_rent:
        :param forgive_utilities:
        :param forgive_mortgage:
        :param address1:
        :param address2:
        :param dba_name:
        :param phone_number:
        :param forgive_fte_at_loan_application:
        :param demographics:
        :param forgive_line_6_3508_or_line_5_3508ez:
        :param forgive_modified_total:
        :param forgive_payroll_cost_60_percent_requirement:
        :param forgive_amount:
        :param forgive_fte_at_forgiveness_application:
        :param forgive_schedule_a_line_1:
        :param forgive_schedule_a_line_2:
        :param forgive_schedule_a_line_3_checkbox:
        :param forgive_schedule_a_line_3:
        :param forgive_schedule_a_line_4:
        :param forgive_schedule_a_line_5:
        :param forgive_schedule_a_line_6:
        :param forgive_schedule_a_line_7:
        :param forgive_schedule_a_line_8:
        :param forgive_schedule_a_line_9:
        :param forgive_schedule_a_line_10:
        :param forgive_schedule_a_line_10_checkbox:
        :param forgive_schedule_a_line_11:
        :param forgive_schedule_a_line_12:
        :param forgive_schedule_a_line_13:
        :param forgive_covered_period_from:
        :param forgive_covered_period_to:
        :param forgive_alternate_covered_period_from:
        :param forgive_alternate_covered_period_to:
        :param forgive_2_million:
        :param forgive_payroll_schedule:
        :param primary_email:
        :param primary_name:
        :param ez_form:
        :param no_employees:
        :param no_reduction_in_employees:
        :param no_reduction_in_employees_and_covid_impact:
        :param forgive_lender_confirmation;
        :param forgive_lender_decision;
        :return:
        """
        http_method = "POST"
        endpoint = "ppp_loan_forgiveness_requests/"

        uri = self.client.api_uri + endpoint

        params = {
            'etran_loan': {
                "bank_notional_amount": bank_notional_amount,
                "sba_number": sba_number,
                "loan_number": loan_number,
                "entity_name": entity_name,
                "ein": ein,
                "funding_date": funding_date,
                "forgive_eidl_amount": forgive_eidl_amount,
                "forgive_eidl_application_number": forgive_eidl_application_number,
                "forgive_payroll": forgive_payroll,
                "forgive_rent": forgive_rent,
                "forgive_utilities": forgive_utilities,
                "forgive_mortgage": forgive_mortgage,
                "address1": address1,
                "address2": address2,
                "dba_name": dba_name,
                "phone_number": phone_number,
                "forgive_fte_at_loan_application": forgive_fte_at_loan_application,
                "demographics": demographics,
                "forgive_line_6_3508_or_line_5_3508ez": forgive_line_6_3508_or_line_5_3508ez,
                "forgive_modified_total": forgive_modified_total,
                "forgive_payroll_cost_60_percent_requirement": forgive_payroll_cost_60_percent_requirement,
                "forgive_amount": forgive_amount,
                "forgive_fte_at_forgiveness_application": forgive_fte_at_forgiveness_application,
                "forgive_schedule_a_line_1": forgive_schedule_a_line_1,
                "forgive_schedule_a_line_2": forgive_schedule_a_line_2,
                "forgive_schedule_a_line_3_checkbox": forgive_schedule_a_line_3_checkbox,
                "forgive_schedule_a_line_3": forgive_schedule_a_line_3,
                "forgive_schedule_a_line_4": forgive_schedule_a_line_4,
                "forgive_schedule_a_line_5": forgive_schedule_a_line_5,
                "forgive_schedule_a_line_6": forgive_schedule_a_line_6,
                "forgive_schedule_a_line_7": forgive_schedule_a_line_7,
                "forgive_schedule_a_line_8": forgive_schedule_a_line_8,
                "forgive_schedule_a_line_9": forgive_schedule_a_line_9,
                "forgive_schedule_a_line_10": forgive_schedule_a_line_10,
                "forgive_schedule_a_line_10_checkbox": forgive_schedule_a_line_10_checkbox,
                "forgive_schedule_a_line_11": forgive_schedule_a_line_11,
                "forgive_schedule_a_line_12": forgive_schedule_a_line_12,
                "forgive_schedule_a_line_13": forgive_schedule_a_line_13,
                "forgive_covered_period_from": forgive_covered_period_from,
                "forgive_covered_period_to": forgive_covered_period_to,
                "forgive_alternate_covered_period_from": forgive_alternate_covered_period_from,
                "forgive_alternate_covered_period_to": forgive_alternate_covered_period_to,
                "forgive_2_million": forgive_2_million,
                "forgive_payroll_schedule": forgive_payroll_schedule,
                "primary_email": primary_email,
                "primary_name": primary_name,
                "ez_form": ez_form,
                "no_employees": no_employees,
                "no_reduction_in_employees": no_reduction_in_employees,
                "no_reduction_in_employees_and_covid_impact": no_reduction_in_employees_and_covid_impact,
                'forgive_lender_confirmation': forgive_lender_confirmation,
                'forgive_lender_decision': forgive_lender_decision,
            }
        }

        headers = {'Content-Type': 'application/json'}
        try:
            response = self.execute(http_method=http_method,
                                    headers=headers,
                                    url=uri,
                                    data=json.dumps(params))

            return {'status': response.status_code,
                    'data': json.loads(response.text)}
        except:
            raise UnknownException
