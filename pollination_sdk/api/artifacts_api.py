# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.28.1
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


class ArtifactsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_artifact(self, owner, name, key_request, **kwargs):  # noqa: E501
        """Get an Artifact upload link.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_artifact(owner, name, key_request, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param key_request: (required)
        :type key_request: KeyRequest
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
        :rtype: S3UploadRequest
        """
        kwargs['_return_http_data_only'] = True
        return self.create_artifact_with_http_info(owner, name, key_request, **kwargs)  # noqa: E501

    def create_artifact_with_http_info(self, owner, name, key_request, **kwargs):  # noqa: E501
        """Get an Artifact upload link.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_artifact_with_http_info(owner, name, key_request, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param key_request: (required)
        :type key_request: KeyRequest
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
        :rtype: tuple(S3UploadRequest, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'owner',
            'name',
            'key_request'
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
                    " to method create_artifact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `create_artifact`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `create_artifact`")  # noqa: E501
        # verify the required parameter 'key_request' is set
        if self.api_client.client_side_validation and ('key_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_request` when calling `create_artifact`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'key_request' in local_var_params:
            body_params = local_var_params['key_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{owner}/{name}/artifacts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='S3UploadRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_artifact(self, owner, name, **kwargs):  # noqa: E501
        """Delete one or many artifacts by key/prefix  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_artifact(owner, name, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param path: The path to an file within a project folder
        :type path: list[str]
        :param page: Page number starting from 1
        :type page: int
        :param per_page: Number of items per page
        :type per_page: int
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_artifact_with_http_info(owner, name, **kwargs)  # noqa: E501

    def delete_artifact_with_http_info(self, owner, name, **kwargs):  # noqa: E501
        """Delete one or many artifacts by key/prefix  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_artifact_with_http_info(owner, name, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param path: The path to an file within a project folder
        :type path: list[str]
        :param page: Page number starting from 1
        :type page: int
        :param per_page: Number of items per page
        :type per_page: int
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
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'owner',
            'name',
            'path',
            'page',
            'per_page'
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
                    " to method delete_artifact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `delete_artifact`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `delete_artifact`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `delete_artifact`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `delete_artifact`, must be a value less than or equal to `100`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'path' in local_var_params and local_var_params['path'] is not None:  # noqa: E501
            query_params.append(('path', local_var_params['path']))  # noqa: E501
            collection_formats['path'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per-page', local_var_params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{owner}/{name}/artifacts', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def download_artifact(self, owner, name, **kwargs):  # noqa: E501
        """Download an artifact from the project folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_artifact(owner, name, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param path: The path to an file within a project folder
        :type path: str
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
        return self.download_artifact_with_http_info(owner, name, **kwargs)  # noqa: E501

    def download_artifact_with_http_info(self, owner, name, **kwargs):  # noqa: E501
        """Download an artifact from the project folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_artifact_with_http_info(owner, name, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param path: The path to an file within a project folder
        :type path: str
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
            'name',
            'path'
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
                    " to method download_artifact" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `download_artifact`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `download_artifact`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'path' in local_var_params and local_var_params['path'] is not None:  # noqa: E501
            query_params.append(('path', local_var_params['path']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{owner}/{name}/artifacts/download', 'GET',
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

    def list_artifacts(self, owner, name, **kwargs):  # noqa: E501
        """List artifacts in a project folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_artifacts(owner, name, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param path: The path to an file within a project folder
        :type path: list[str]
        :param page: Page number starting from 1
        :type page: int
        :param per_page: Number of items per page
        :type per_page: int
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
        :rtype: list[FileMeta]
        """
        kwargs['_return_http_data_only'] = True
        return self.list_artifacts_with_http_info(owner, name, **kwargs)  # noqa: E501

    def list_artifacts_with_http_info(self, owner, name, **kwargs):  # noqa: E501
        """List artifacts in a project folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_artifacts_with_http_info(owner, name, async_req=True)
        >>> result = thread.get()

        :param owner: (required)
        :type owner: str
        :param name: (required)
        :type name: str
        :param path: The path to an file within a project folder
        :type path: list[str]
        :param page: Page number starting from 1
        :type page: int
        :param per_page: Number of items per page
        :type per_page: int
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
        :rtype: tuple(list[FileMeta], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'owner',
            'name',
            'path',
            'page',
            'per_page'
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
                    " to method list_artifacts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'owner' is set
        if self.api_client.client_side_validation and ('owner' not in local_var_params or  # noqa: E501
                                                        local_var_params['owner'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `owner` when calling `list_artifacts`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `list_artifacts`")  # noqa: E501

        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_artifacts`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'per_page' in local_var_params and local_var_params['per_page'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `per_page` when calling `list_artifacts`, must be a value less than or equal to `100`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'owner' in local_var_params:
            path_params['owner'] = local_var_params['owner']  # noqa: E501
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501

        query_params = []
        if 'path' in local_var_params and local_var_params['path'] is not None:  # noqa: E501
            query_params.append(('path', local_var_params['path']))  # noqa: E501
            collection_formats['path'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'per_page' in local_var_params and local_var_params['per_page'] is not None:  # noqa: E501
            query_params.append(('per-page', local_var_params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{owner}/{name}/artifacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FileMeta]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
