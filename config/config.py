import string
import random

class TestData:

    def user_req_body(self):
        r = {"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}
        return r

    def req_create_user(self, num):
        r = self.user_req_body()
        req = []
        for i in range(num):
            ran = ''.join(random.choices(string.ascii_lowercase, k=7))
            r['name'] = "fname_" + ran + " lname_" + ran
            r['email'] = "fname_" + ran + ".lname_" + ran + "@testeemail.com"
            r['status'] = "active"
            if i % 2 == 0:
                r['gender'] = 'male'
            else:
                r["gender"] = 'female'
            req.append(r.copy())
        return [tuple(d.values()) for d in req]


#
#
# td = TestData()
# req = td.req_create_user(2)
