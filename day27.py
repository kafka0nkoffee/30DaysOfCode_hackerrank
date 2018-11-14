# Day 27: Testing


class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        # complete this function
        return []


class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function
        return [5, 8, 2, 9]

    @staticmethod
    def get_expected_result():
        # complete this function
        seq = TestDataUniqueValues.get_array()
        return minimum_index(seq)


class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        return [5, 2, 7, 2, 9]

    @staticmethod
    def get_expected_result():
        # complete this function
        seq = TestDataExactlyTwoDifferentMinimums.get_array()
        return minimum_index(seq)
