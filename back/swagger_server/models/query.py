# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Query(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: Data=None):  # noqa: E501
        """Query - a model defined in Swagger

        :param data: The data of this Query.  # noqa: E501
        :type data: Data
        """
        self.swagger_types = {
            'data': Data
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Query':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Query of this Query.  # noqa: E501
        :rtype: Query
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> Data:
        """Gets the data of this Query.


        :return: The data of this Query.
        :rtype: Data
        """
        return self._data

    @data.setter
    def data(self, data: Data):
        """Sets the data of this Query.


        :param data: The data of this Query.
        :type data: Data
        """

        self._data = data