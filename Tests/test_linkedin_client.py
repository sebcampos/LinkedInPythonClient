import pytest
from linkedin_client import LinkedInClient
from Logger import set_up_logger


logger = set_up_logger("testing-logger")


test_url = \
    "https://www.linkedin.com/voyager/api/search/hits?decorationId=com.linkedin.voyager.deco.jserp.WebJobSearchHitWithSalary-25&count=25&filters=List(locationFallback-%3EUnited%20States,geoUrn-%3Eurn%3Ali%3Afs_geo%3A103644278,resultType-%3EJOBS)&keywords=tester&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&q=jserpFilters&queryContext=List(primaryHitType-%3EJOBS,spellCorrectionEnabled-%3Etrue)&start=0&topNRequestedFlavors=List(HIDDEN_GEM,IN_NETWORK,SCHOOL_RECRUIT,COMPANY_RECRUIT,SALARY,JOB_SEEKER_QUALIFIED,PRE_SCREENING_QUESTIONS,SKILL_ASSESSMENTS,ACTIVELY_HIRING_COMPANY,TOP_APPLICANT)"

def test_login():
    client = LinkedInClient()
    r, part1, client_page_instance = client.login()
    assert r.status_code == 200
    print(r.content)
    print(client_page_instance)
    print(part1)


def test_jobsearch():
    client = LinkedInClient()
    r, part1, client_page_instance = client.login()
    # TODO Captcha check
    if "Security Verification" in r.content.decode():
        print("Captcha check")
        pytest.skip("Captcha detected")
    paging, elements = client.get_jobs("automation", 0)
    assert True

