# Forgiveness Requests

```python
forgiveness = client.forgiveness_requests
```

## Class Name

`ForgivenessApi`

# GET

returns

    Ticket{
            id  integer
                title: ID
                readOnly: true
            slug    string($uuid)
                title: Slug
                readOnly: true
            submitter_email string($email)
                title: Your E-Mail
                maxLength: 254
            You will receive an email for all public follow-ups left for this request.

        borrower_name*  string
            title: Borrower name
            maxLength: 100
            minLength: 1

            Borrower Name

        etran_loan* 
            Etran loan{
                slug    string($uuid)
                    title: Slug
                    readOnly: true
                bank_notional_amount*   string($decimal)
                    title: Notional Amount (from Bank Core)
                sba_number* string
                    title: Sba number
                    maxLength: 255
                    minLength: 1
                loan_number*    string
                    title: Loan number
                    maxLength: 255
                    minLength: 1
                entity_name*    string
                    title: Entity name
                    maxLength: 255
                    minLength: 1
                ein*    string
                    title: Ein
                    maxLength: 11
                    minLength: 1
                funding_date    string($date)
                    title: Funding Date
                    forgive_eidl_amount string($decimal)
                    title: EIDL Amount
                forgive_eidl_application_number integer
                    title: EIDL Application Number
                    maximum: 2147483647
                    minimum: -2147483648
                forgive_payroll string($decimal)
                    title: Used on Payroll
                forgive_rent    string($decimal)
                    title: Used on Rent
                forgive_utilities   string($decimal)
                    title: Used on Utilities
                forgive_mortgage    string($decimal)
                    title: Used on Mortgage
                address1    string
                    title: Address 1
                    maxLength: 255
                address2    string
                    title: Address 2
                    maxLength: 255
                dba_name    string
                    title: DBA Name
                    maxLength: 255
                organization    
                    Organization{
                        name*   string
                            title: Organization Name
                            maxLength: 200
                            minLength: 1
                        etran_location_id   string
                            title: Etran Location ID
                            maxLength: 50
                        slug    string($uuid)
                            title: Slug
                            readOnly: true
                    }
                phone_number    string
                    title: Phone Number
                    maxLength: 255
                assign_to_user  integer
                    title: Assign to user
                forgive_fte_at_loan_application integer
                    title: FTE's at time of loan application
                    maximum: 2147483647
                    minimum: -2147483648
                documents   [
                    readOnly: true
                    EtranLoanDocument{
                        slug    string($uuid)
                            title: Slug
                            readOnly: true
                        name*   string
                            title: Name
                            maxLength: 50
                            minLength: 1
                        created_at  string($date-time)
                            title: Created At
                            readOnly: true
                        updated_at  string($date-time)
                            title: Updated At
                            readOnly: true
                        document    string($uri)
                            title: Document
                            readOnly: true
                        url string
                            title: Url
                            readOnly: true
                        etran_loan* string
                            title: Etran loan
                            minLength: 1
                        document_type*
                            EtranLoanDocumentType{
                                id  integer
                                    title: ID
                                    readOnly: true
                                name*   string
                                    title: Name
                                    maxLength: 50
                                    minLength: 1
                                description string
                                    title: Description
                            }
                    }
                ]

                status string
                    title: Status
                    readOnly: true  

                updated string
                    title: Updated
                    readOnly: true

                demographics
                    [EtranLoanDemographic{
                        name*   string
                            title: Principal Name
                            maxLength: 50
                            minLength: 1
                        position*   string
                            title: Position
                            maxLength: 50
                            minLength: 1
                        veteran_status* string
                            title: Veteran Status
                            Enum:
                                [ , 1, 2, 3, 4, X ]
                        gender* string
                            title: Gender
                            Enum:
                                [ , M, F, X ]
                        ethnicity*  string
                            title: Ethnicity
                            Enum:
                                [ , H, N, X ]
                        races*
                            [EtranLoanDemographicRace{
                                race*   string
                                    title: Race
                                    Enum:
                                        [ , 1, 2, 3, 4, 5, X ]
                            }]
                    }]
                forgive_line_6_3508_or_line_5_3508ez    string($decimal)
                    title: Line 6 on 3508 or Line 5 on 3508EZ
                forgive_modified_total  string($decimal)
                    title: Modified Total (Line 8 on 3508)
                forgive_payroll_cost_60_percent_requirement string($decimal)
                    title: Payroll Cost 60% Requirement
                forgive_amount  string($decimal)
                    title: Forgiveness Amount
                forgive_fte_at_forgiveness_application  integer
                    title: FTE's at time of forgiveness application
                    maximum: 2147483647
                    minimum: -2147483648
                forgive_schedule_a_line_1   string($decimal)
                    title: Line 1 from Schedule A
                forgive_schedule_a_line_2   string($decimal)
                    title: Line 2 from Schedule A
                forgive_schedule_a_line_3_checkbox  boolean
                    title: Line 3 Checkbox
                forgive_schedule_a_line_3   string($decimal)
                    title: Total Salary/Hourly Wage Reduction (enter the amount from PPP Schedule A, line 3)
                forgive_schedule_a_line_4   string($decimal)
                    title: Line 4 from Schedule A
                forgive_schedule_a_line_5   string($decimal)
                    title: Line 5 from Schedule A
                forgive_schedule_a_line_6   string($decimal)
                    title: Line 6 from Schedule A
                forgive_schedule_a_line_7   string($decimal)
                    title: Line 7 from Schedule A
                forgive_schedule_a_line_8   string($decimal)
                    title: Line 8 from Schedule A
                forgive_schedule_a_line_9   string($decimal)
                    title: Line 9 from Schedule A
                forgive_schedule_a_line_10  string($decimal)
                    title: Line 10 from Schedule A
                forgive_schedule_a_line_10_checkbox boolean
                    title: Line 10 Checkbox
                forgive_schedule_a_line_11  string($decimal)
                    title: Line 11 from Schedule A
                forgive_schedule_a_line_12  string($decimal)
                    title: Line 12 from Schedule A
                forgive_schedule_a_line_13  string($decimal)
                    title: FTE Reduction Quotient (enter the number from PPP Schedule A, line 13)
                forgive_covered_period_from string($date)
                    title: Forgive covered period from
                forgive_covered_period_to   string($date)
                    title: Forgive covered period to
                forgive_alternate_covered_period_from   string($date)
                    title: Forgive alternate covered period from
                forgive_alternate_covered_period_to string($date)
                    title: Forgive alternate covered period to
                forgive_2_million   boolean
                    title: Borrower (with Affiliates) received PPP loan in excess of $2 million
                forgive_payroll_schedule    string
                    title: Forgive payroll schedule
                    maxLength: 255
                primary_email   string($email)
                    title: Primary Email
                    maxLength: 254
                primary_name    string
                    title: Primary Name
                    maxLength: 255
                ez_form boolean
                    title: Use 3508EZ form
                no_employees    boolean
                    title: The Borrower is a self-employed individual, independent contractor, or sole proprietor who had no employees at the time of the PPP loan application and did not include any employee salaries in the computation of average monthly payroll in the Borrower Application Form (SBA Form 2483)
                no_reduction_in_employees   boolean
                    title: The Borrower did not reduce annual salary or hourly wages of any employee by more than 25 percent during the Covered Period or the Alternative Payroll Covered Period (as defined below) compared to the period between January 1, 2020 and March 31, 2020 (for purposes of this statement, “employees” means only those employees that did not receive, during any single period during 2019, wages or salary at an annualized rate of pay in an amount more than $100,000); ANDThe Borrower did not reduce the number of employees or the average paid hours of employees between January 1, 2020 and the end of the Covered Period. (Ignore reductions that arose from an inability to rehire individuals who were employees on February 15, 2020 if the Borrower was unable to hire similarly qualified employees for unfilled positions on or before December 31, 2020. Also ignore reductions in an employee’s hours that the Borrower offered to restore and the employee refused. See 85 FR 33004, 33007 (June 1, 2020) for more details.
                no_reduction_in_employees_and_covid_impact  boolean
                    title: The Borrower did not reduce annual salary or hourly wages of any employee by more than 25 percent during the Covered Period or the Alternative Payroll Covered Period (as defined below) compared to the period between January 1, 2020 and March 31, 2020 (for purposes of this statement, “employees” means only those employees that did not receive, during any single period during 2019, wages or salary at an annualized rate of pay in an amount more than $100,000); ANDThe Borrower was unable to operate during the Covered Period at the same level of business activity as before February 15, 2020, due to compliance with requirements established or guidance issued between March 1, 2020 and December 31, 2020 by the Secretary of Health and Human Services, the Director of the Centers for Disease Control and Prevention, or the Occupational Safety and Health Administration, related to the maintenance of standards of sanitation, social distancing, or any other work or customer safety requirement related to COVID-19.
                }


            created string($date-time)
                title: Created
                readOnly: true
            assigned_to_user    string
                title: Assigned to user
                readOnly: true
    }

## api_ppp_loan_forgiveness_requests_list

parameters

    :param page:    integer


## api_ppp_loan_forgiveness_requests_read

parameters

    :param slug:    string
    
# DELETE

returns

    None
    
##api_ppp_loan_forgiveness_requests_delete

parameters

    :param slug:    string
    

# POST

returns

    LimitedTicket{
    id  integer
        title: ID
        readOnly: true
    slug    string($uuid)
        title: Slug
        readOnly: true
    etran_loan* 
        Etran loan{
            slug    string($uuid)
                title: Slug
                readOnly: true
            bank_notional_amount*   string($decimal)
                title: Notional Amount (from Bank Core)
            sba_number* string
                title: Sba number
                maxLength: 255
                minLength: 1
            loan_number*    string
                title: Loan number
                maxLength: 255
                minLength: 1
            entity_name*    string
                title: Entity name
                maxLength: 255
                minLength: 1
            ein*    string
                title: Ein
                maxLength: 11
                minLength: 1
            funding_date    string($date)
                title: Funding Date
            forgive_eidl_amount string($decimal)
                title: EIDL Amount
            forgive_eidl_application_number integer
                title: EIDL Application Number
                maximum: 2147483647
                minimum: -2147483648
            forgive_payroll string($decimal)
                title: Used on Payroll
            forgive_rent    string($decimal)
                title: Used on Rent
            forgive_utilities   string($decimal)
                title: Used on Utilities
            forgive_mortgage    string($decimal)
                title: Used on Mortgage
            address1    string
                title: Address 1
                maxLength: 255
            address2    string
                title: Address 2
                maxLength: 255
            dba_name    string
                title: DBA Name
                maxLength: 255
            phone_number    string
                title: Phone Number
                maxLength: 255
            forgive_fte_at_loan_application integer
                title: FTE's at time of loan application
                maximum: 2147483647
                minimum: -2147483648
            demographics
                [EtranLoanDemographic{
                    name*   string
                        title: Principal Name
                        maxLength: 50
                        minLength: 1
                    position*   string
                        title: Position
                        maxLength: 50
                        minLength: 1
                    veteran_status* string
                        title: Veteran Status
                        Enum:
                            [ , 1, 2, 3, 4, X ]
                    gender* string
                        title: Gender
                        Enum:
                            [ , M, F, X ]
                    ethnicity*  string
                        title: Ethnicity
                        Enum:
                            [ , H, N, X ]
                    races*
                        [EtranLoanDemographicRace{
                            race*   string
                                title: Race
                                Enum:
                                    [ , 1, 2, 3, 4, 5, X ]
                        }]
                }]
            forgive_line_6_3508_or_line_5_3508ez    string($decimal)
                title: Line 6 on 3508 or Line 5 on 3508EZ
            forgive_modified_total  string($decimal)
                title: Modified Total (Line 8 on 3508)
            forgive_payroll_cost_60_percent_requirement string($decimal)
                title: Payroll Cost 60% Requirement
            forgive_amount  string($decimal)
                title: Forgiveness Amount
            forgive_fte_at_forgiveness_application  integer
                title: FTE's at time of forgiveness application
                maximum: 2147483647
                minimum: -2147483648
            forgive_schedule_a_line_1   string($decimal)
                title: Line 1 from Schedule A
            forgive_schedule_a_line_2   string($decimal)
                title: Line 2 from Schedule A
            forgive_schedule_a_line_3_checkbox  boolean
                title: Line 3 Checkbox
            forgive_schedule_a_line_3   string($decimal)
                title: Total Salary/Hourly Wage Reduction (enter the amount from PPP Schedule A, line 3)
            forgive_schedule_a_line_4   string($decimal)
                title: Line 4 from Schedule A
            forgive_schedule_a_line_5   string($decimal)
                title: Line 5 from Schedule A
            forgive_schedule_a_line_6   string($decimal)
                title: Line 6 from Schedule A
            forgive_schedule_a_line_7   string($decimal)
                title: Line 7 from Schedule A
            forgive_schedule_a_line_8   string($decimal)
                title: Line 8 from Schedule A
            forgive_schedule_a_line_9   string($decimal)
                title: Line 9 from Schedule A
            forgive_schedule_a_line_10  string($decimal)
                title: Line 10 from Schedule A
            forgive_schedule_a_line_10_checkbox boolean
                title: Line 10 Checkbox
            forgive_schedule_a_line_11  string($decimal)
                title: Line 11 from Schedule A
            forgive_schedule_a_line_12  string($decimal)
                title: Line 12 from Schedule A
            forgive_schedule_a_line_13  string($decimal)
                title: FTE Reduction Quotient (enter the number from PPP Schedule A, line 13)
            forgive_covered_period_from string($date)
                title: Forgive covered period from
            forgive_covered_period_to   string($date)
                title: Forgive covered period to
            forgive_alternate_covered_period_from   string($date)
                title: Forgive alternate covered period from
            forgive_alternate_covered_period_to string($date)
                title: Forgive alternate covered period to
            forgive_2_million   boolean
                title: Borrower (with Affiliates) received PPP loan in excess of $2 million
            forgive_payroll_schedule    string
                title: Forgive payroll schedule
                maxLength: 255
            primary_email   string($email)
                title: Primary Email
                maxLength: 254
            primary_name    string
                title: Primary Name
                maxLength: 255
            ez_form boolean
                title: Use 3508EZ form
            no_employees    boolean
                title: The Borrower is a self-employed individual, independent contractor, or sole proprietor who had no employees at the time of the PPP loan application and did not include any employee salaries in the computation of average monthly payroll in the Borrower Application Form (SBA Form 2483)
            no_reduction_in_employees   boolean
                title: The Borrower did not reduce annual salary or hourly wages of any employee by more than 25 percent during the Covered Period or the Alternative Payroll Covered Period (as defined below) compared to the period between January 1, 2020 and March 31, 2020 (for purposes of this statement, “employees” means only those employees that did not receive, during any single period during 2019, wages or salary at an annualized rate of pay in an amount more than $100,000); ANDThe Borrower did not reduce the number of employees or the average paid hours of employees between January 1, 2020 and the end of the Covered Period. (Ignore reductions that arose from an inability to rehire individuals who were employees on February 15, 2020 if the Borrower was unable to hire similarly qualified employees for unfilled positions on or before December 31, 2020. Also ignore reductions in an employee’s hours that the Borrower offered to restore and the employee refused. See 85 FR 33004, 33007 (June 1, 2020) for more details.
            no_reduction_in_employees_and_covid_impact  boolean
                title: The Borrower did not reduce annual salary or hourly wages of any employee by more than 25 percent during the Covered Period or the Alternative Payroll Covered Period (as defined below) compared to the period between January 1, 2020 and March 31, 2020 (for purposes of this statement, “employees” means only those employees that did not receive, during any single period during 2019, wages or salary at an annualized rate of pay in an amount more than $100,000); ANDThe Borrower was unable to operate during the Covered Period at the same level of business activity as before February 15, 2020, due to compliance with requirements established or guidance issued between March 1, 2020 and December 31, 2020 by the Secretary of Health and Human Services, the Director of the Centers for Disease Control and Prevention, or the Occupational Safety and Health Administration, related to the maintenance of standards of sanitation, social distancing, or any other work or customer safety requirement related to COVID-19.
        }
       
       
## api_ppp_loan_forgiveness_requests_create

parameters
    
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