# from curator.defaults.settings import snapshot_actions
# from voluptuous import All, Any, Boolean, Coerce, Optional, Range, Required
# from six import string_types, text_type

# ### Schema information ###

# def aliases(**kwargs):
#     # This setting is used by the alias filtertype and is required
#     return { Required('aliases'): Any(list, *string_types) }

# def allocation_type(**kwargs):
#     return { Optional('allocation_type', default='require'): All(
#         Any(*string_types), Any('require', 'include', 'exclude')) }

# def count(**kwargs):
#     # This setting is only used with the count filtertype and is required
#     return { Required('count'): All(Coerce(int), Range(min=1)) }

# def date_from(**kwargs):
#     # This setting is only used with the period filtertype.
#     return { Optional('date_from'): Any(*string_types) }

# def date_from_format(**kwargs):
#     # This setting is only used with the period filtertype.
#     return { Optional('date_from_format'): Any(*string_types) }

# def date_to(**kwargs):
#     # This setting is only used with the period filtertype.
#     return { Optional('date_to'): Any(*string_types) }

# def date_to_format(**kwargs):
#     # This setting is only used with the period filtertype.
#     return { Optional('date_to_format'): Any(*string_types) }

# def direction(**kwargs):
#     # This setting is only used with the age filtertype.
#     return { Required('direction'): Any('older', 'younger') }

# def disk_space(**kwargs):
#     # This setting is only used with the space filtertype and is required
#     return { Required('disk_space'): Any(Coerce(float)) }

# def epoch(**kwargs):
#     # This setting is only used with the age filtertype.
#     return { Optional('epoch', default=None): Any(Coerce(int), None) }

# def exclude(**kwargs):
#     # This setting is available in all filter types.
#     if 'exclude' in kwargs and kwargs['exclude']:
#         val = True
#     else: # False by default
#         val = False
#     # pylint: disable=no-value-for-parameter
#     return { Optional('exclude', default=val): Any(bool, All(Any(*string_types), Boolean())) }

# def field(**kwargs):
#     # This setting is only used with the age filtertype.
#     if 'required' in kwargs and kwargs['required']:
#         return { Required('field'): Any(*string_types) }
#     else:
#         return { Optional('field'): Any(*string_types) }

# def intersect(**kwargs):
#     # This setting is only used with the period filtertype when using field_stats
#     # i.e. indices only.
#     # pylint: disable=no-value-for-parameter
#     return { Optional('intersect', default=False): Any(bool, All(Any(*string_types), Boolean())) }

# def key(**kwargs):
#     # This setting is only used with the allocated filtertype.
#     return { Required('key'): Any(*string_types) }

# def kind(**kwargs):
#     # This setting is only used with the pattern filtertype and is required
#     return {
#         Required('kind'): Any('prefix', 'suffix', 'timestring', 'regex')
#     }

# def max_num_segments(**kwargs):
#     return {
#         Required('max_num_segments'): All(Coerce(int), Range(min=1))
#     }

# def pattern(**kwargs):
#     return {
#         Optional('pattern'): Any(*string_types)
#     }

# def period_type(**kwargs):
#     # This setting is only used with the period filtertype.
#     return { Optional('period_type', default='relative'): Any('relative', 'absolute') }

# def range_from(**kwargs):
#     return { Optional('range_from'): Coerce(int) }

# def range_to(**kwargs):
#     return { Optional('range_to'): Coerce(int) }

# def reverse(**kwargs):
#     # Only used with space filtertype
#     # Should be ignored if `use_age` is True
#     # pylint: disable=no-value-for-parameter
#     return { Optional('reverse', default=True): Any(bool, All(Any(*string_types), Boolean())) }

# def source(**kwargs):
#     # This setting is only used with the age filtertype, or with the space
#     # filtertype when use_age is set to True.
#     if 'action' in kwargs and kwargs['action'] in snapshot_actions():
#         valuelist = Any('name', 'creation_date')
#     else:
#         valuelist = Any('name', 'creation_date', 'field_stats')

#     if 'required' in kwargs and kwargs['required']:
#         return { Required('source'): valuelist }
#     else:
#         return { Optional('source'): valuelist }

# def state(**kwargs):
#     # This setting is only used with the state filtertype.
#     return { Optional('state', default='SUCCESS'): Any(
#         'SUCCESS', 'PARTIAL', 'FAILED', 'IN_PROGRESS') }

# def stats_result(**kwargs):
#     # This setting is only used with the age filtertype.
#     return {
#         Optional('stats_result', default='min_value'): Any(
#             'min_value', 'max_value')
#     }

# def timestring(**kwargs):
#     # This setting is only used with the age filtertype, or with the space
#     # filtertype if use_age is set to True.
#     if 'required' in kwargs and kwargs['required']:
#         return { Required('timestring'): Any(*string_types) }
#     else:
#         return { Optional('timestring', default=None): Any(None, *string_types) }

# def threshold_behavior(**kwargs):
#     # This setting is only used with the space filtertype and defaults to 'greater_than'.
#     return { Optional('threshold_behavior', default='greater_than'): Any('greater_than', 'less_than') }

# def unit(**kwargs):
#     # This setting is only used with the age filtertype, or with the space
#     # filtertype if use_age is set to True.
#     return {
#         Required('unit'): Any(
#             'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years'
#         )
#     }

# def unit_count(**kwargs):
#     # This setting is only used with the age filtertype, or with the space
#     # filtertype if use_age is set to True.
#     return { Required('unit_count'): Coerce(int) }

# def unit_count_pattern(**kwargs):
#     # This setting is used with the age filtertype to define, whether
#     # the unit_count value is taken from the configuration or read from
#     # the index name via a regular expression
#     return { Optional('unit_count_pattern'): Any(*string_types) }

# def use_age(**kwargs):
#     # Use of this setting requires the additional setting, source.
#     # pylint: disable=no-value-for-parameter
#     return { Optional('use_age', default=False): Any(bool, All(Any(*string_types), Boolean())) }

# def value(**kwargs):
#     # This setting is only used with the pattern filtertype and is a required
#     # setting. There is a separate value option associated with the allocation
#     # action, and the allocated filtertype.
#     return { Required('value'): Any(*string_types) }

# def week_starts_on(**kwargs):
#     return {
#         Optional('week_starts_on', default='sunday'): Any(
#             'Sunday', 'sunday', 'SUNDAY', 'Monday', 'monday', 'MONDAY', None
#         )
#     }
