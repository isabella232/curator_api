# import logging
# from curator.actions.parentclasses import ActionClass
# from curator.exceptions import ActionError, ConfigurationError, MissingArgument
# from curator.helpers.index import chunk_index_list, verify_index_list
# from curator.helpers.utils import to_csv

# class IndexSettings(ActionClass):
#     def __init__(self, ilo, index_settings={}, ignore_unavailable=False,
#         preserve_existing=False):
#         """
#         :arg ilo: A :class:`curator.indexlist.IndexList` object
#         :arg index_settings: A dictionary structure with one or more index
#             settings to change.
#         :arg ignore_unavailable: Whether specified concrete indices should be 
#             ignored when unavailable (missing or closed)
#         :arg preserve_existing: Whether to update existing settings. If set to 
#             ``True`` existing settings on an index remain unchanged. The default
#             is ``False``
#         """
#         verify_index_list(ilo)
#         if not index_settings:
#             raise MissingArgument('Missing value for "index_settings"')
#         #: Instance variable.
#         #: The Elasticsearch Client object derived from `ilo`
#         self.client     = ilo.client
#         #: Instance variable.
#         #: Internal reference to `ilo`
#         self.index_list = ilo
#         #: Instance variable.
#         #: Internal reference to `index_settings`
#         self.body = index_settings
#         #: Instance variable.
#         #: Internal reference to `ignore_unavailable`
#         self.ignore_unavailable = ignore_unavailable
#         #: Instance variable.
#         #: Internal reference to `preserve_settings`
#         self.preserve_existing = preserve_existing

#         self.loggit     = logging.getLogger('curator.actions.index_settings')
#         self._body_check()

#     def _body_check(self):
#         # The body only passes the skimpiest of requirements by having 'index'
#         # as the only root-level key, and having a 'dict' as its value
#         if len(self.body) == 1:
#             if 'index' in self.body:
#                 if isinstance(self.body['index'], dict):
#                     return True
#         raise ConfigurationError(
#             'Bad value for "index_settings": {0}'.format(self.body))

#     def _static_settings(self):
#         return [
#             'number_of_shards',
#             'shard',
#             'codec',
#             'routing_partition_size',
#         ]

#     def _dynamic_settings(self):
#         return [
#             'number_of_replicas',
#             'auto_expand_replicas',
#             'refresh_interval',
#             'max_result_window',
#             'max_rescore_window',
#             'blocks',
#             'max_refresh_listeners',
#             'mapping',
#             'merge',
#             'translog',
#         ]

#     def _settings_check(self):
#         # Detect if even one index is open.  Save all found to open_index_list.
#         open_index_list = []
#         open_indices = False
#         for idx in self.index_list.indices:
#             if self.index_list.index_info[idx]['state'] == 'open':
#                 open_index_list.append(idx)
#                 open_indices = True
#         for k in self.body['index']:
#             if k in self._static_settings():
#                 if not self.ignore_unavailable:
#                     if open_indices:
#                         raise ActionError(
#                             'Static Setting "{0}" detected with open indices: '
#                             '{1}. Static settings can only be used with closed '
#                             'indices.  Recommend filtering out open indices, '
#                             'or setting ignore_unavailable to True'.format(
#                                 k, open_index_list
#                             )
#                         )
#             elif k in self._dynamic_settings():
#                 # Dynamic settings should be appliable to open or closed indices
#                 # Act here if the case is different for some settings.
#                 pass
#             else:
#                 self.loggit.warn(
#                     '"{0}" is not a setting Curator recognizes and may or may '
#                     'not work.'.format(k)
#                 )

#     def do_dry_run(self):
#         """
#         Log what the output would be, but take no action.
#         """
#         self.show_dry_run(self.index_list, 'indexsettings', **self.body)

#     def do_action(self):
#         self._settings_check()
#         # Ensure that the open indices filter applied in _settings_check()
#         # didn't result in an empty list (or otherwise empty)
#         self.index_list.empty_list_check()
#         self.loggit.info(
#             'Applying index settings to indices: '
#             '{0}'.format(self.index_list.indices)
#         )
#         try:
#             index_lists = chunk_index_list(self.index_list.indices)
#             for l in index_lists:
#                 response = self.client.indices.put_settings(
#                     index=to_csv(l), body=self.body, 
#                     ignore_unavailable=self.ignore_unavailable,
#                     preserve_existing=self.preserve_existing
#                 )
#                 self.loggit.debug('PUT SETTINGS RESPONSE: {0}'.format(response))
#         except Exception as e:
#             self.report_failure(e)
