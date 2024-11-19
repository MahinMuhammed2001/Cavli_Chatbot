def filter_companies_by_field(data, field, keyword):
    """Filter companies by field and keyword, with case-insensitive substring matching."""
    filtered_companies = []
    for company in data:
        field_value = company.get(field, "").lower()  #  case-insensitive comparison
        if keyword.lower() in field_value:
            filtered_companies.append(company)
    return filtered_companies

def format_company_info(companies):
    """Formats the company information for display."""
    return "\n".join(
        f"Company: {company['company_name']}\n"
        f"Industry: {company['industry_category']}\n"
        f"Address: {company['address']}\n"
        f"Email: {company['email']}\n"
        f"Phone: {company['phone']}\n"
        f"Website: {company['website']}\n" for company in companies
    )
