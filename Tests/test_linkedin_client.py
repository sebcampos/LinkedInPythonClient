import pytest
from linkedin_client import LinkedInClient
from Logger import set_up_logger
import random

logger = set_up_logger("testing-logger")

test_url = \
    "https://www.linkedin.com/voyager/api/search/hits?decorationId=com.linkedin.voyager.deco.jserp.WebJobSearchHitWithSalary-25&count=25&filters=List(locationFallback-%3EUnited%20States,geoUrn-%3Eurn%3Ali%3Afs_geo%3A103644278,resultType-%3EJOBS)&keywords=tester&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&q=jserpFilters&queryContext=List(primaryHitType-%3EJOBS,spellCorrectionEnabled-%3Etrue)&start=0&topNRequestedFlavors=List(HIDDEN_GEM,IN_NETWORK,SCHOOL_RECRUIT,COMPANY_RECRUIT,SALARY,JOB_SEEKER_QUALIFIED,PRE_SCREENING_QUESTIONS,SKILL_ASSESSMENTS,ACTIVELY_HIRING_COMPANY,TOP_APPLICANT)"


def test_login():
    client = LinkedInClient()
    r = client.login()
    assert r[0].status_code == 200
    print(r.content)



def test_jobsearch():
    client = LinkedInClient()
    r = client.login()
    random_start = random.randint(0, 300)
    print(f"Random num: {random_start}")
    paging, elements = client.get_jobs("devops engineer", random_start)
    print(f"Suggestion: {elements[0].hitInfo.querySuggestionsComponent}\n\n")
    for element in elements[1:]:
        job = element.hitInfo.jobPostingResolutionResult
        company = job.companyDetails.get('com.linkedin.voyager.deco.jserp.WebJobPostingWithCompanyName', None)
        company = company['companyResolutionResult']['name'] if company is not None else company
        print(f"Title: {job.title}\nJob State: {job.jobState}\nWork From Home: {job.workRemoteAllowed}\nSalary: {job.formattedSalaryDescription}\nCompany: {company}\nLocation: {job.formattedLocation}\n\n")
    assert True
