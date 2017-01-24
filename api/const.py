class RequestType(object):
    ASSISTANCE = 'assistance'
    DONATION = 'donation'
    FILE = 'documents'

class RequestActions(object):
    SUBMIT = 'submit'
    APPROVE = 'approve'
    DENY = 'deny'
    CLOSE = 'close'

class RequestStatus(object):
    CREATED = 'Created'
    SUBMITTED = 'Submitted'
    APPROVED = 'Approved'
    CANCELLED = 'Cancelled'
    PAID = 'Paid'

class ResponseType(object):
    SUCCESS = 'success'
    ERROR = 'error'
