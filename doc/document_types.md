# Document Types

```python
doc_types = client.document_types
```

## Class Name

`DocumentTypeApi`


# GET
returns

    EtranLoanDocumentType {
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

##api_ppp_loan_document_types_list

parameters

    :param page:    integer


##api_ppp_loan_document_types_read

parameters

    :param id:    integer
