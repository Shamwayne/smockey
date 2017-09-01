import hashlib
from warnings import warn


class MockUser:
    """ A Mock User object for use in website/database testing. This is meant to
    be used in conjunction with the generateMockUsers function to create up to 1000
    MockUser at a time.

    attributes: username (String Type) ,
                email (String Type, if validate==True: uses if_email() to validate),
                gender (String Type, either "Male" or "Female"),
                password (String Type, value ranges between 6-12 random chars)
    """

    def hash512(self, pword):
        """ Hashes a given password using sha512 algorithm """
        unicode_pass = str.encode(pword, "UTF-8")
        hashed_pass = hashlib.sha512(unicode_pass).hexdigest()
        return hashed_pass

    def is_email(self, email):
        """ Validates if a given string is an email address and raises an 
        error if it isn't.

        The current method is to check whether the code has the neccessary symbols
        and also if the string is at least as long as the shortest possible email
        address. Will be refactored with regex expressons later
        """
        if ("@" in email) and ("." in email) and (len(email) > 4):
            return email
        else:
            warn_message = "WARNING: email value '" + email + "' not a valid email address! continuing..."
            warn(warn_message)
            return email

    def __init__(self, username, email, gender, password, validate=True):
        self.username = username
        self.gender = gender
        if validate == True:
            # this checks whether the MockUser should validate  email or encrypt password
            self.email = self.is_email(email)
            self.password = self.hash512(password)
        else:
            self.email = email
            self.password = password

    def __repr__(self):
        mockobj = "<MockUser => username={}, email={}, gender={}, password={} >"
        return mockobj.format(self.username, self.email, self.gender, self.password)


def genMockUsers(number=10, set_validate=True):
    """generates MockUser objects according to the number specified. 
    attributes: number (Integer Type, default=10, max=1000), 
                set_validate (Boolean Type, default=True)

    if no number is specified it defaults to making 10 MockUser Objects.
    However the max number of users it can create at this point in time is 1000 unique
    users, any more above that and it will raise an error.
    """
    if number > 1000:
        warn(
            "WARNING: cannot generate more than 1000 MockUsers at one instance, creating 1000 MockUser Objects instead")
        number = 1000
    users_csv = open("social_users.csv", "r")
    headers = users_csv.readline()  # ignore headers
    print(headers)
    mock_store = []
    for i in range(number):
        raw_data = users_csv.readline()
        data = raw_data.strip().split(sep=",")
        new_user = MockUser(username=data[0], email=data[1], gender=data[2], password=data[3], validate=set_validate)
        mock_store.append(new_user)
    return mock_store


if __name__ == '__main__':
    # a_user = MockUser()
    # b_user = MockUser("Thomas", "tom@tom.com", "Male", "password123")
    # print(b_user)
    # c_user = MockUser("C bear", "cbear.com", "Male", "open_sesame!")
    x = genMockUsers()
    print(x)
    # y = generateMockUsers(100, True)
    # users = generateMockUsers(2500, False)
