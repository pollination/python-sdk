# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: 0.21.2
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


class LicensesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_available_pools(self, **kwargs):  # noqa: E501
        """Get Available Pools  # noqa: E501

        Get license pools available to authenticated user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_pools(async_req=True)
        >>> result = thread.get()

        :param owner: Owner of the project
        :type owner: list[str]
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
        :rtype: LicensePoolList
        """
        kwargs['_return_http_data_only'] = True
        return self.get_available_pools_with_http_info(**kwargs)  # noqa: E501

    def get_available_pools_with_http_info(self, **kwargs):  # noqa: E501
        """Get Available Pools  # noqa: E501

        Get license pools available to authenticated user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_pools_with_http_info(async_req=True)
        >>> result = thread.get()

        :param owner: Owner of the project
        :type owner: list[str]
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
        :rtype: tuple(LicensePoolList, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_available_pools" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'owner' in local_var_params and local_var_params['owner'] is not None:  # noqa: E501
            query_params.append(('owner', local_var_params['owner']))  # noqa: E501
            collection_formats['owner'] = 'multi'  # noqa: E501

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
            '/licenses/pools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicensePoolList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_license_activations(self, pool_id, **kwargs):  # noqa: E501
        """Get Activations  # noqa: E501

        Get the activations for the license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_license_activations(pool_id, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
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
        :rtype: ActivationList
        """
        kwargs['_return_http_data_only'] = True
        return self.get_license_activations_with_http_info(pool_id, **kwargs)  # noqa: E501

    def get_license_activations_with_http_info(self, pool_id, **kwargs):  # noqa: E501
        """Get Activations  # noqa: E501

        Get the activations for the license  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_license_activations_with_http_info(pool_id, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
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
        :rtype: tuple(ActivationList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pool_id'
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
                    " to method get_license_activations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pool_id' is set
        if self.api_client.client_side_validation and ('pool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pool_id` when calling `get_license_activations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']  # noqa: E501

        query_params = []

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
            '/licenses/pools/{pool_id}/activations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_pool_license(self, pool_id, **kwargs):  # noqa: E501
        """Get Pool License  # noqa: E501

        Get the license associated with a pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pool_license(pool_id, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
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
        :rtype: LicensePublic
        """
        kwargs['_return_http_data_only'] = True
        return self.get_pool_license_with_http_info(pool_id, **kwargs)  # noqa: E501

    def get_pool_license_with_http_info(self, pool_id, **kwargs):  # noqa: E501
        """Get Pool License  # noqa: E501

        Get the license associated with a pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pool_license_with_http_info(pool_id, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
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
        :rtype: tuple(LicensePublic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pool_id'
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
                    " to method get_pool_license" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pool_id' is set
        if self.api_client.client_side_validation and ('pool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pool_id` when calling `get_pool_license`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']  # noqa: E501

        query_params = []

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
            '/licenses/pools/{pool_id}/license', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicensePublic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def grant_access_to_pool(self, pool_id, license_pool_access_policy, **kwargs):  # noqa: E501
        """Grant Pool Access  # noqa: E501

        Grant access to the license pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.grant_access_to_pool(pool_id, license_pool_access_policy, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
        :param license_pool_access_policy: (required)
        :type license_pool_access_policy: LicensePoolAccessPolicy
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
        :rtype: LicensePoolPublic
        """
        kwargs['_return_http_data_only'] = True
        return self.grant_access_to_pool_with_http_info(pool_id, license_pool_access_policy, **kwargs)  # noqa: E501

    def grant_access_to_pool_with_http_info(self, pool_id, license_pool_access_policy, **kwargs):  # noqa: E501
        """Grant Pool Access  # noqa: E501

        Grant access to the license pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.grant_access_to_pool_with_http_info(pool_id, license_pool_access_policy, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
        :param license_pool_access_policy: (required)
        :type license_pool_access_policy: LicensePoolAccessPolicy
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
        :rtype: tuple(LicensePoolPublic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pool_id',
            'license_pool_access_policy'
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
                    " to method grant_access_to_pool" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pool_id' is set
        if self.api_client.client_side_validation and ('pool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pool_id` when calling `grant_access_to_pool`")  # noqa: E501
        # verify the required parameter 'license_pool_access_policy' is set
        if self.api_client.client_side_validation and ('license_pool_access_policy' not in local_var_params or  # noqa: E501
                                                        local_var_params['license_pool_access_policy'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `license_pool_access_policy` when calling `grant_access_to_pool`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'license_pool_access_policy' in local_var_params:
            body_params = local_var_params['license_pool_access_policy']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/licenses/pools/{pool_id}/permissions', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicensePoolPublic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def revoke_access_to_pool(self, pool_id, license_pool_policy_subject, **kwargs):  # noqa: E501
        """Delete Pool Access  # noqa: E501

        Revoke access to the license pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.revoke_access_to_pool(pool_id, license_pool_policy_subject, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
        :param license_pool_policy_subject: (required)
        :type license_pool_policy_subject: LicensePoolPolicySubject
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
        :rtype: LicensePoolPublic
        """
        kwargs['_return_http_data_only'] = True
        return self.revoke_access_to_pool_with_http_info(pool_id, license_pool_policy_subject, **kwargs)  # noqa: E501

    def revoke_access_to_pool_with_http_info(self, pool_id, license_pool_policy_subject, **kwargs):  # noqa: E501
        """Delete Pool Access  # noqa: E501

        Revoke access to the license pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.revoke_access_to_pool_with_http_info(pool_id, license_pool_policy_subject, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
        :param license_pool_policy_subject: (required)
        :type license_pool_policy_subject: LicensePoolPolicySubject
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
        :rtype: tuple(LicensePoolPublic, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'pool_id',
            'license_pool_policy_subject'
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
                    " to method revoke_access_to_pool" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pool_id' is set
        if self.api_client.client_side_validation and ('pool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pool_id` when calling `revoke_access_to_pool`")  # noqa: E501
        # verify the required parameter 'license_pool_policy_subject' is set
        if self.api_client.client_side_validation and ('license_pool_policy_subject' not in local_var_params or  # noqa: E501
                                                        local_var_params['license_pool_policy_subject'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `license_pool_policy_subject` when calling `revoke_access_to_pool`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'license_pool_policy_subject' in local_var_params:
            body_params = local_var_params['license_pool_policy_subject']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/licenses/pools/{pool_id}/permissions', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LicensePoolPublic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_license_pool(self, pool_id, license_pool_update, **kwargs):  # noqa: E501
        """Update Pool  # noqa: E501

        Update the license pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_license_pool(pool_id, license_pool_update, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
        :param license_pool_update: (required)
        :type license_pool_update: LicensePoolUpdate
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
        return self.update_license_pool_with_http_info(pool_id, license_pool_update, **kwargs)  # noqa: E501

    def update_license_pool_with_http_info(self, pool_id, license_pool_update, **kwargs):  # noqa: E501
        """Update Pool  # noqa: E501

        Update the license pool  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_license_pool_with_http_info(pool_id, license_pool_update, async_req=True)
        >>> result = thread.get()

        :param pool_id: (required)
        :type pool_id: str
        :param license_pool_update: (required)
        :type license_pool_update: LicensePoolUpdate
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
            'pool_id',
            'license_pool_update'
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
                    " to method update_license_pool" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pool_id' is set
        if self.api_client.client_side_validation and ('pool_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pool_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pool_id` when calling `update_license_pool`")  # noqa: E501
        # verify the required parameter 'license_pool_update' is set
        if self.api_client.client_side_validation and ('license_pool_update' not in local_var_params or  # noqa: E501
                                                        local_var_params['license_pool_update'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `license_pool_update` when calling `update_license_pool`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pool_id' in local_var_params:
            path_params['pool_id'] = local_var_params['pool_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'license_pool_update' in local_var_params:
            body_params = local_var_params['license_pool_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyAuth', 'JWTAuth']  # noqa: E501

        return self.api_client.call_api(
            '/licenses/pools/{pool_id}', 'PUT',
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
