# coding: utf-8

"""
    Pollination Server

    Pollination Server OpenAPI Defintion  # noqa: E501

    The version of the OpenAPI document: v0.9.1
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pollination_sdk.api_client import ApiClient
from pollination_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RegistriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_package(self, owner, type, name, digest, **kwargs):  # noqa: E501
        """Get Package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_package(owner, type, name, digest, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param type: (required)
        :type type: str
        :param name: (required)
        :type name: str
        :param digest: (required)
        :type digest: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.get_package_with_http_info(owner, type, name, digest, **kwargs)  # noqa: E501

    def get_package_with_http_info(self, owner, type, name, digest, **kwargs):  # noqa: E501
        """Get Package  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_package_with_http_info(owner, type, name, digest, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param type: (required)
        :type type: str
        :param name: (required)
        :type name: str
        :param digest: (required)
        :type digest: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'owner',
            'type',
            'name',
            'digest'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_package" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `get_package`")  # noqa: E501
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in local_var_params or  # noqa: E501
                                                        local_var_params['type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `type` when calling `get_package`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `get_package`")  # noqa: E501
        # verify the required parameter 'digest' is set
        if self.api_client.client_side_validation and ('digest' not in local_var_params or  # noqa: E501
                                                        local_var_params['digest'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `digest` when calling `get_package`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']  # noqa: E501
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501
        if 'digest' in local_var_params:
            path_params['digest'] = local_var_params['digest']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/x-tar'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OptionalAuth']  # noqa: E501

        return self.api_client.call_api(
            '/registries/{owner}/{type}/{name}/{digest}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_registry_index(self, owner, **kwargs):  # noqa: E501
        """Get Registry Index  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registry_index(owner, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RepositoryIndex
        """
        kwargs['_return_http_data_only'] = True
        return self.get_registry_index_with_http_info(owner, **kwargs)  # noqa: E501

    def get_registry_index_with_http_info(self, owner, **kwargs):  # noqa: E501
        """Get Registry Index  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registry_index_with_http_info(owner, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(RepositoryIndex, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'owner'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_registry_index" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `get_registry_index`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OptionalAuth']  # noqa: E501

        return self.api_client.call_api(
            '/registries/{owner}/index.json', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RepositoryIndex',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def post_operator(self, owner, package, **kwargs):  # noqa: E501
        """Push an Operator to the registry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_operator(owner, package, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param package: (required)
        :type package: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.post_operator_with_http_info(owner, package, **kwargs)  # noqa: E501

    def post_operator_with_http_info(self, owner, package, **kwargs):  # noqa: E501
        """Push an Operator to the registry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_operator_with_http_info(owner, package, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param package: (required)
        :type package: file
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'owner',
            'package'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_operator" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `post_operator`")  # noqa: E501
        # verify the required parameter 'package' is set
        if self.api_client.client_side_validation and ('package' not in local_var_params or  # noqa: E501
                                                        local_var_params['package'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `package` when calling `post_operator`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'package' in local_var_params:
            local_var_files['package'] = local_var_params['package']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CompulsoryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/registries/{owner}/operators', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def post_recipe(self, owner, package, **kwargs):  # noqa: E501
        """Push an Recipe to the registry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_recipe(owner, package, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param package: (required)
        :type package: file
        :param authorization:
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.post_recipe_with_http_info(owner, package, **kwargs)  # noqa: E501

    def post_recipe_with_http_info(self, owner, package, **kwargs):  # noqa: E501
        """Push an Recipe to the registry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_recipe_with_http_info(owner, package, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param package: (required)
        :type package: file
        :param authorization:
        :type authorization: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'owner',
            'package',
            'authorization'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_recipe" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `post_recipe`")  # noqa: E501
        # verify the required parameter 'package' is set
        if self.api_client.client_side_validation and ('package' not in local_var_params or  # noqa: E501
                                                        local_var_params['package'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `package` when calling `post_recipe`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'package' in local_var_params:
            local_var_files['package'] = local_var_params['package']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['CompulsoryAuth']  # noqa: E501

        return self.api_client.call_api(
            '/registries/{owner}/recipes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
