from arrays import Array


class Pictures:
    def __init__(self, num_rows, num_cols):
        """
        Creates a 2D array of size num_rows x num_cols.
        :param num_rows: number of rows.
        :param num_cols: number of columns.
        """

        # Creates a 1D array to store an array reference for each row.
        self.rows = Array(num_rows)

        # Creates the 1D arrays for each row of the 2D array.
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2D array.

        :return:
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2D array.

        :return: the number of columns in the 2D array.
        """
        return len(self.rows[0])

    def clear(self, value):
        """
        Clears the array by setting every element to the given value.

        :param value: value to be set.
        """
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j]

        :param index_tuple: the index of position.
        :return: the value.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the element at position [i,j] to value.

        :param index_tuple: the index of position.
        :param value: the value to be set.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        if not (0 <= row < self.num_rows() and 0 <= col < self.num_cols()):
            raise IndexError('Invalid index')
        array_1d = self.rows[row]
        array_1d[col] = value
