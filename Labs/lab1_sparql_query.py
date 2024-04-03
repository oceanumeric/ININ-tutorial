"""
Lab1: SPARQL Query
Author: oceanumeric
Date: 03-04-2024
Description: This script is used to query the data from the RDF file using SPARQL query.
Students who are curious to learn about SPARQL query can use this script as a reference.
"""
import time
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF


def query_cpc(cpc_code: str, start_year: int, end_year):
    
    # Create a SPARQLWrapper object and set the endpoint
    sparql = SPARQLWrapper("https://data.epo.org/linked-data/query")
    # use json as the return format
    sparql.setReturnFormat(JSON)
    
    
    sparql_query = f"""
    PREFIX cpc: <http://data.epo.org/linked-data/def/cpc/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX vcard: <http://www.w3.org/2006/vcard/ns#> 
    PREFIX patent: <http://data.epo.org/linked-data/def/patent/>
    
    SELECT *
    WHERE {{
        ?publn rdf:type patent:Publication;
            patent:applicantVC ?applicant;
            patent:publicationAuthority ?auth;
            patent:publicationNumber ?publnNum;
            patent:publicationKind ?kind;
            patent:publicationDate ?publnDate;
            patent:application ?application.
        ?application patent:classificationCPCInventive ?cpcCode.
        ?applicant vcard:fn ?name.
        ?applicant vcard:hasAddress ?address.
        ?address patent:countryCode ?country.
        ?cpcCode skos:broader ?cpcCodeB1.
        ?cpcCodeB1 skos:broader ?cpcCodeB2.
        ?cpcCodeB2 skos:broader ?cpcCodeB3.
        FILTER (?cpcCodeB3 = <http://data.epo.org/linked-data/def/cpc/{cpc_code}>)
        FILTER (?publnDate >= xsd:date('{start_year}-01-01'))
        FILTER (?publnDate <= xsd:date('{end_year}-01-01'))
    }}
    LIMIT 70000
    """
    # Set the query
    sparql.setQuery(sparql_query)
    results = sparql.query().convert()  # get the results
    qr_df = pd.json_normalize(results['results']['bindings'])
    
    # only keep columns that names contains '.value'
    qr_df = qr_df[[col for col in qr_df.columns if '.value' in col]]
    
    # delete '.value' from the column names
    qr_df.columns = [col.replace('.value', '') for col in qr_df.columns]
    
    return qr_df


if __name__ == "__main__":
    # test the basic query
    cpc_code = 'B60K'
    # start_year = 2014
    # end_year = 2015
    # foo = query_cpc(cpc_code, start_year, end_year)
    # print(foo.shape)
    # # save the result to a csv file
    # foo.to_csv(f'../data/patent_{cpc_code}_{start_year}.csv', index=False)
    
    # do for loop from 2014 to 2024
    h01m_df = pd.DataFrame()
    for year in range(2014, 2025):
        foo = query_cpc(cpc_code, year, year+1)
        h01m_df = pd.concat([h01m_df, foo], axis=0)
        # save the result to a csv file
        h01m_df.to_csv(f'../data/patent_{cpc_code}_2014_2024.csv', index=False)
        print(f"Year {year} done! with total {h01m_df.shape[0]} patents.")
        # sleep for 5 seconds
        time.sleep(5)