import re
import json
from requests import Session
import urllib.parse

from .api_objects import Elements, Paging
from .credentials import username, password

url = "https://www.linkedin.com"
login_url = "https://www.linkedin.com/uas/login-submit"
jobs_url = "https://platform.linkedin.com/litms/allowlist/voyager-web-jobs"
hits_url = "https://www.linkedin.com/voyager/api/search/hits"


class LinkedInClient(Session):
    """Linked in Scraping Client"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_csrf_token = None
        self.csrf_token = None
        self.set_login_csrf_param()
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        self.headers.update(headers)

    def set_login_csrf_param(self) -> str:
        r = self.get(
            url,
            headers={"X-CSRF-Token": "fetch"}
        )
        self.login_csrf_token = re.search(r'"loginCsrfParam" value="(.*?)"', r.content.decode()).groups()[0]

    def login(self):
        # TODO sometimes blocked by captcha, workaround is to login with private browser and solve captcha
        r = self.post(
            login_url,
            data= \
                {
                    "loginCsrfParam": self.login_csrf_token,
                    "session_key": username,
                    "session_password": password,
                }
        )
        data_str = r.content.decode().replace("&quot;", '"')
        code_data = tuple(i[0].replace("&#92;", "\\") for i in re.findall(r'<code.*>((.|\n|\t)+?)</code>', data_str))
        part1 = tuple(json.loads(i) for i in code_data[:-1])
        client_page_instance = code_data[-1].strip()
        self.csrf_token = self.cookies.get("JSESSIONID").replace('"', '')
        self.headers.update({"csrf-token": self.csrf_token})
        return r, part1, client_page_instance

    def get_jobs(self, keywords, start, filters=None, origin=None, q=None, query_context=None, top_n_requested=None, decoration_id=None, count=50) -> tuple:
        decoration_id = "com.linkedin.voyager.deco.jserp.WebJobSearchHitWithSalary-50" if decoration_id is None else decoration_id
        origin = "JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE" if origin is None else origin
        filters = "List(locationFallback->United States,geoUrn->urn:li:fs_geo:103644278,resultType->JOBS)" if filters is None else filters
        q = "jserpFilters" if q is None else q
        query_context = "List(primaryHitType->JOBS,spellCorrectionEnabled->true)" if query_context is None else query_context
        top_n_requested = "List(HIDDEN_GEM,IN_NETWORK,SCHOOL_RECRUIT,COMPANY_RECRUIT,SALARY,JOB_SEEKER_QUALIFIED,PRE_SCREENING_QUESTIONS,SKILL_ASSESSMENTS,ACTIVELY_HIRING_COMPANY,TOP_APPLICANT)" if top_n_requested is None else top_n_requested
        parameters = \
            {
                "decorationId": decoration_id,
                "count": count,
                "filters": filters,
                "keywords": keywords,
                "origin": origin,
                "q": q,
                "queryContext": query_context,
                "start": start,
                "topNRequestedFlavors": top_n_requested,
            }
        parameters = urllib.parse.urlencode(parameters, safe='(),', quote_via=urllib.parse.quote)
        r = self.get(hits_url, params=parameters)
        if r.status_code != 200:
            assert False
        r = r.json()
        print(r.keys())
        paging = Paging(r['paging'])
        elements = Elements(r['elements'])
        return paging, elements