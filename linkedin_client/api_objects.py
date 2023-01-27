class BaseClass:
    string_rep: str
    string_rep2: str

    def __str__(self):
        return self.string_rep2

    def __repr__(self):
        return self.string_rep


class Element(BaseClass):
    targetPageInstance: object
    DSrecipeType: object
    hitInfo: object
    trackingId: object

    def __init__(self, element_dict: dict):
        self.targetPageInstance = element_dict.get('targetPageInstance', None)
        self.DSrecipeType = element_dict.get('$recipeType', None)
        hitInfo = HitInfo(element_dict['hitInfo'])
        if hitInfo.querySuggestionsComponent is not None:
            print(hitInfo)
        self.hitInfo = hitInfo
        self.trackingId = element_dict['trackingId']
        self.string_rep = "Element"
        self.string_rep2 = str({i: type(v) for i, v in element_dict.items()})


class Elements(tuple):
    def __init__(self, elements: list):
        elements = (Element(element) for element in elements)
        super().__init__(self, elements)



class Paging(BaseClass):
    total: int
    count: int
    start: int
    links: list

    def __init__(self, paging_dict: dict):
        self.total = paging_dict['total']
        self.count = paging_dict['count']
        self.start = paging_dict['start']
        self.links = paging_dict['links']
        self.string_rep = str(paging_dict)


class JobPostingResolutionResult(BaseClass):
    dashEntityUrn: str
    companyDetails: dict
    jobState: str
    formattedSalaryDescription: str
    title: str
    entityUrn: str
    workRemoteAllowed: bool
    briefBenefitsDescription: str
    applyMethod: dict
    savingInfo: dict
    new: bool
    formattedLocation: str
    dashJobPostingCardUrn: object
    workplaceTypes: list
    expireAt: int
    listedAt: int
    jobPostingId: int
    DSrecipeType: str
    sourceDomain: str

    def __init__(self, job_posting_dict: dict):
        self.dashEntityUrn = job_posting_dict['dashEntityUrn']
        self.companyDetails = job_posting_dict['companyDetails']
        self.jobState = job_posting_dict['jobState']
        self.formattedSalaryDescription = job_posting_dict['formattedSalaryDescription']
        self.title = job_posting_dict['title']
        self.entityUrn = job_posting_dict['entityUrn']
        self.workRemoteAllowed = job_posting_dict['workRemoteAllowed']
        self.briefBenefitsDescription = job_posting_dict['briefBenefitsDescription']
        self.applyMethod = job_posting_dict['applyMethod']
        self.savingInfo = job_posting_dict['savingInfo']
        self.new = job_posting_dict['new']
        self.formattedLocation = job_posting_dict['formattedLocation']
        self.dashJobPostingCardUrn = job_posting_dict['dashJobPostingCardUrn']
        self.workplaceTypes = job_posting_dict['workplaceTypes']
        self.expireAt = job_posting_dict['expireAt']
        self.listedAt = job_posting_dict['listedAt']
        self.jobPostingId = job_posting_dict['jobPostingId']
        self.DSrecipeType = job_posting_dict['$recipeType']
        self.sourceDomain = job_posting_dict.get('sourceDomain', None)
        self.string_rep = ", ".join(i for i in job_posting_dict.keys())
        self.string_rep2 = "\n".join(str(i)+" "+str(self.__getattribute__(str(i))) for i in self.__dir__() if not i.startswith("__"))

class QuerySuggestionsComponent(BaseClass):
    def __init__(self, query_suggestion: dict):
        suggestions = tuple(i['keywords'] for i in query_suggestion)
        self.string_rep2 = ",".join(suggestions)


class HitInfo(BaseClass):
    key: str
    encryptedBiddingParameters: object
    topNRelevanceReasonsInjectionResult: object
    sponsored: object
    jobPosting: object  # urn
    DSrecipeType: object
    jobPostingResolutionResult: JobPostingResolutionResult
    querySuggestionsComponent: QuerySuggestionsComponent = None

    def __init__(self, hit_info_dict: dict):
        self.key = next(i for i in hit_info_dict.keys())
        querySuggestionsComponent = hit_info_dict[self.key].get("suggestions", None)
        if querySuggestionsComponent is not None:
            self.querySuggestionsComponent = QuerySuggestionsComponent(querySuggestionsComponent)
        self.encryptedBiddingParameters = hit_info_dict[self.key].get('encryptedBiddingParameters', None)
        self.topNRelevanceReasonsInjectionResult = hit_info_dict[self.key].get('topNRelevanceReasonsInjectionResult',
                                                                               None)
        self.sponsored = hit_info_dict[self.key].get('sponsored', None)
        self.jobPosting = hit_info_dict[self.key].get('jobPosting', None)
        self.DSrecipeType = hit_info_dict[self.key].get('$recipeType', None)
        job_posting_resolution_result = hit_info_dict[self.key].get('jobPostingResolutionResult', None)
        self.jobPostingResolutionResult = JobPostingResolutionResult(
            job_posting_resolution_result) if job_posting_resolution_result is not None else None
        self.string_rep = str(hit_info_dict)
        self.string_rep2 = "HitInfo"
