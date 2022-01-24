import os
import unittest
from unittest.mock import Mock, patch
import json

expected_reason = json.dumps({'a': 1})
print(expected_reason)

json_mock = Mock()
# print(type(json_mock)) -->
json_type = "<class 'unittest.mock.Mock'>"  # object type Mock
# print(dir(json_mock)) -->
json_mock_dir_list = ['assert_any_call', 'assert_called', 'assert_called_once', 'assert_called_once_with',
                      'assert_called_with', 'assert_has_calls', 'assert_not_called', 'attach_mock', 'call_args',
                      'call_args_list', 'call_count', 'called', 'configure_mock', 'method_calls', 'mock_add_spec',
                      'mock_calls', 'reset_mock', 'return_value', 'side_effect']
mock_dumps = json_mock.dumps({'a': 1})
# print(dir(json_mock)) -->
json_mock_dir_list = ['assert_any_call', 'assert_called', 'assert_called_once', 'assert_called_once_with',
                      'assert_called_with', 'assert_has_calls', 'assert_not_called', 'attach_mock', 'call_args',
                      'call_args_list', 'call_count', 'called', 'configure_mock', 'dumps', 'method_calls',
                      'mock_add_spec', 'mock_calls', 'reset_mock', 'return_value', 'side_effect']
# When you use method that don't exist mock object will create it.
# print(mock_dumps) -->
mock_dumps_result = "<Mock name='mock.dumps()' id='1968026186320'>"  # just creating new Mock Objects
# patch(json_mock.dumps({'a': 1}), {"a": 1}):
# print(mock_dumps)






# print(json_mock.dumps.assert_any_call())
# print(json_mock.dumps.assert_called()) -->
mock_dumps_assert_called = None  # Assert that the mock was called at least once. None else error
# print(json_mock.dumps.assert_called_once()) -->
mock_dumps_assert_called_once = None  # Assert that the mock was called exactly once. None if once else error
# print(json_mock.dumps.assert_called_once_with())
# print(json_mock.dumps.assert_called_with())
# print(json_mock.dumps.assert_has_calls())
# print(json_mock.dumps.assert_not_called())







