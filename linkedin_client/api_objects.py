class BaseClass:
    string_rep: str

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
        self.string_rep = str(element_dict)


class Elements(BaseClass):
    items = ()

    def __init__(self, elements: list):
        self.string_rep = str(elements)
        for element in elements:
            self.items += (Element(element),)


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
        self.string_rep = str(job_posting_dict)



class QuerySuggestionsComponent:
    def __init__(self, query_suggestion: dict):
        suggestions = tuple(i['keywords'] for i in query_suggestion)
        self.string_rep = ",".join(suggestions)


class HitInfo(BaseClass):
    key: str
    encryptedBiddingParameters: object
    topNRelevanceReasonsInjectionResult: object
    sponsored: object
    jobPosting: object  # urn
    DSrecipeType: object
    suggestions: dict
    jobPostingResolutionResult: JobPostingResolutionResult

    def __init__(self, hit_info_dict: dict):
        self.key = next(i for i in hit_info_dict.keys())
        suggestions = hit_info_dict[self.key].get("suggestions", None)
        if suggestions is not None:
            self.suggestions = QuerySuggestionsComponent(suggestions)
        self.encryptedBiddingParameters = hit_info_dict[self.key].get('encryptedBiddingParameters', None)
        self.topNRelevanceReasonsInjectionResult = hit_info_dict[self.key].get('topNRelevanceReasonsInjectionResult',None)
        self.sponsored = hit_info_dict[self.key].get('sponsored', None)
        self.jobPosting = hit_info_dict[self.key].get('jobPosting', None)
        self.DSrecipeType = hit_info_dict[self.key].get('$recipeType', None)
        job_posting_resolution_result = hit_info_dict[self.key].get('jobPostingResolutionResult', None)
        self.jobPostingResolutionResult = JobPostingResolutionResult(job_posting_resolution_result) if job_posting_resolution_result is not None else None
        self.string_rep = str(hit_info_dict)

