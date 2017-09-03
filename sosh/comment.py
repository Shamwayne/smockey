import os
from datetime import datetime
from random import randint
from warnings import warn


class MockComment:
    def __init__(self, content, timestamp=datetime.now()):
        self.timestamp = timestamp
        self.content = content

    def __repr__(self):
        return "<MockPost => timestamp:{}, \n content:{} >".format(self.timestamp, self.content)


class MockUserComment(MockComment):
    def __init__(self, content, timestamp=datetime.now(), user_id=randint(0, 100)):
        super().__init__(content, timestamp)
        self.user_id = user_id

    def __repr__(self):
        return "<MockUserComment => timestamp:{}, \n content:{}, user_id:{} >".format(self.timestamp, self.content,
                                                                                      self.user_id)


class MockTopicComment(MockUserComment):
    def __init__(self, content, timestamp=datetime.now(), user_id=randint(0, 100), topic_id=randint(0, 10)):
        super().__init__(content, timestamp, user_id)
        self.topic_id = topic_id

    def __repr__(self):
        return "<MockTopicComment => timestamp:{}, \n content:{}, user_id:{}, topic_id:{} >".format(self.timestamp,
                                                                                                    self.content,
                                                                                                    self.user_id,
                                                                                                    self.topic_id)


def genMockComment(mock_type, number=10):
    if number > 100:
        warn(
            "WARNING: cannot generate more than 100 PostObjects at one instance, creating 100 Objects instead")
        number = 100
    COMMENT_SOURCE = os.path.join(os.path.dirname(__file__), "post_text_data.txt")
    post_data = open(COMMENT_SOURCE, "r")
    mock_store = []
    mock_type = mock_type.lower()
    for i in range(number):
        content = post_data.readline().strip()
        if mock_type == "mockcomment":
            new_post = MockComment(content, datetime.now())
        elif mock_type == "mockusercomment":
            new_post = MockUserComment(content, datetime.now(), randint(0, 100))
        elif mock_type == "mocktopiccomment":
            new_post = MockTopicComment(content, datetime.now(), randint(0, 100), randint(0, 10))
        else:
            raise IOError("Mock Object Type '" + mock_type + "' not recognised")
        mock_store.append(new_post)
    return mock_store


if __name__ == '__main__':
    mk = MockComment("Hello World")
    mk1 = MockUserComment("What up!")
    mk2 = MockTopicComment(content="Salutations Friend!", user_id=5, topic_id=3)

    print(mk, "\n", mk1, "\n", mk2)
