# Loan Documents

```python
loan_docs = client.loan_documents
```

## Class Name

`LoanDocumentsApi`


# POST

returns
    
    LimitedEtranLoanDocument{
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
    document_type*  integer
        title: Document type
    url string
        title: Url
        readOnly: true
    etran_loan* string
        title: Etran loan
        minLength: 1
    }

## api_ppp_loan_documents_create

parameters

        :param name: string
        :param document_type: integer
        :param etran_loan: string
        :param document: string
        
    
